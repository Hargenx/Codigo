# Aplicações de Cloud, IoT e Indústria 4.0 — Mini-Lab em Python (Colab)

**Disciplina:** Aplicações de Cloud, IoT e Indústria 4.0  
**Aula:** Introdução a Protocolos (MQTT/HTTP) + Visualização e Análise  
**Instrutor(a):** _Raphael Mauricio Sanches de Jesus_ · **Turma:** _Nova América_ · **Data:** _08/09/2025_

---

## Objetivos de Aprendizagem

- Compreender o fluxo **dispositivo → protocolo → processamento → visualização**.
- Publicar e assinar telemetria via **MQTT** usando um broker público.
- Enviar payload **HTTP/REST** e interpretar respostas.
- Construir **gráficos** e checagens simples de **regras/alertas** sobre os dados.
- Exercitar variações (QoS, retained, tópicos, agregação de leituras).

## Pré-requisitos

- Python básico (listas/dicionários, funções).
- Noções de rede e JSON.

## Mapa da Aula

1) Setup
2) Sensor simulado
3) MQTT (sub/pub)
4) Visualização
5) HTTP
6) Exercícios

um **simulador de sensor**;
**MQTT** usando um **broker público** (sem precisar abrir portas);
um envio **HTTP/REST** simples para visualizar o payload;
**gráficos** e **pequenas análises**;
uma seção final com **desafios/exercícios**.

Você pode copiar e colar os blocos abaixo direto no Colab.
(Se não usar Colab, funciona igual no Jupyter local.)

---

## 1) Setup rápido

```python
!pip -q install paho-mqtt pandas matplotlib requests
```

---

## 2) Gerador de telemetria (sensor simulado)

```python
import time, random, json, uuid
from dataclasses import dataclass, asdict

@dataclass
class Telemetry:
    device_id: str
    ts: float
    temperature: float
    humidity: float

def read_sensor(device_id="sensor-001"):
    """Gera medidas simuladas."""
    return Telemetry(
        device_id=device_id,
        ts=time.time(),
        temperature=round(random.uniform(20, 30), 2),
        humidity=round(random.uniform(40, 70), 2),
    )

def to_json(obj):
    return json.dumps(asdict(obj), ensure_ascii=False)
```

---

## 3) Configuração MQTT (tópico único por turma)

> Usamos um broker público. Se o primeiro estiver instável na sua rede, troque pelo alternativo.

```python
import os, random

# Brokers públicos comuns (port 1883 - sem TLS)
BROKERS = [
    ("test.mosquitto.org", 1883),          # 1
    ("mqtt.eclipseprojects.io", 1883),     # 2 (alternativo)
]

# gere um tópico exclusivo para a aula, para evitar colisão com outros usuários do broker público
CLASS_ID = str(uuid.uuid4())[:8]  # troque por algo da turma, se quiser: "turma-2025-09"
TOPIC = f"aula_iot/{CLASS_ID}/telemetry"

BROKER_HOST, BROKER_PORT = BROKERS[0]  # mude para BROKERS[1] se necessário

BROKER_HOST, BROKER_PORT, TOPIC
```

---

## 4) Assinante (Subscriber) — roda em segundo plano

> Este bloco cria um cliente MQTT que **escuta** o tópico e guarda tudo em `received_rows`.

```python
import threading
import paho.mqtt.client as mqtt

received_rows = []   # aqui vamos acumulando as leituras recebidas
subscriber_client = None
stop_flag = False

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode("utf-8"))
        received_rows.append(payload)
        # evita memória infinita
        if len(received_rows) > 2000:
            del received_rows[:len(received_rows)-2000]
    except Exception as e:
        print("parse error:", e)

def start_subscriber():
    global subscriber_client, stop_flag
    stop_flag = False
    c = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=f"sub-{uuid.uuid4()}")
    c.on_message = on_message
    c.connect(BROKER_HOST, BROKER_PORT, keepalive=60)
    c.subscribe(TOPIC)
    c.loop_start()
    subscriber_client = c
    print(f"[SUB] conectado em {BROKER_HOST}:{BROKER_PORT}, tópico '{TOPIC}'")

def stop_subscriber():
    global subscriber_client, stop_flag
    stop_flag = True
    if subscriber_client:
        subscriber_client.loop_stop()
        subscriber_client.disconnect()
        subscriber_client = None
        print("[SUB] parado.")

start_subscriber()
```

---

## 5) Publicador (Publisher) — envia N mensagens

```python
import paho.mqtt.client as mqtt
import time

def publish_n_messages(n=20, delay_s=0.5, device_id="sensor-001"):
    c = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=f"pub-{uuid.uuid4()}")
    c.connect(BROKER_HOST, BROKER_PORT, keepalive=60)
    c.loop_start()
    for i in range(n):
        t = read_sensor(device_id=device_id)
        payload = to_json(t)
        c.publish(TOPIC, payload, qos=0, retain=False)
        print(f"[PUB] {TOPIC} ← {payload}")
        time.sleep(delay_s)
    c.loop_stop()
    c.disconnect()
    print("[PUB] concluído.")

publish_n_messages(n=30, delay_s=0.3)
```

---

## 6) Visualização rápida (tabela + gráfico)

```python
import pandas as pd
import matplotlib.pyplot as plt

def df_from_received():
    if not received_rows:
        return pd.DataFrame()
    df = pd.DataFrame(received_rows)
    df = df.sort_values("ts")
    df["datetime"] = pd.to_datetime(df["ts"], unit="s")
    return df

df = df_from_received()
display(df.tail(5))

if not df.empty:
    plt.figure(figsize=(10,4))
    plt.plot(df["datetime"], df["temperature"], label="temperature")
    plt.plot(df["datetime"], df["humidity"], label="humidity")
    plt.title("Telemetria recebida (últimos pontos)")
    plt.xlabel("tempo")
    plt.ylabel("valor")
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("Ainda não há dados — rode o publisher novamente.")
```

---

## 7) Mini “regras”/alertas (exemplo simples de análise)

```python
ALERTS = []

def check_rules(df, t_thresh=28.0, h_thresh=65.0):
    alerts = []
    for _, row in df.iterrows():
        if row["temperature"] >= t_thresh:
            alerts.append({"ts": row["ts"], "rule": "temp alta", "value": row["temperature"]})
        if row["humidity"] >= h_thresh:
            alerts.append({"ts": row["ts"], "rule": "umidade alta", "value": row["humidity"]})
    return alerts

df = df_from_received()
if not df.empty:
    ALERTS = check_rules(df)
    print(f"{len(ALERTS)} alertas.\nExemplos:")
    for a in ALERTS[-5:]:
        print(a)
else:
    print("Sem dados para checar regras.")
```

---

## 8) REST/HTTP de forma simples (sem servidor)

> Como o Colab não recebe conexões externas, só **mostramos o payload** e simulamos um POST para um **eco** público (`httpbin.org`) — para o(a) aluno(a) ver como seria o envio via REST.

```python
import requests

payload = asdict(read_sensor())
print("Payload JSON:", payload)

# Envia para httpbin (um serviço que devolve o que você mandou)
r = requests.post("https://httpbin.org/post", json=payload, timeout=10)
print("Status:", r.status_code)
print("Trecho de resposta:", r.json()["json"])
```

> Se você quiser, depois mostre como trocar a URL por um endpoint real (ex.: API da instituição).

---

## 9) (Opcional) Enviar para ThingSpeak (plano free)

> Só rode se você tiver uma **Write API Key**.

```python
THINGSPEAK_KEY = ""  # cole aqui sua Write API Key

import time, requests
if THINGSPEAK_KEY:
    for i in range(3):
        t = read_sensor()
        data = {"api_key": THINGSPEAK_KEY, "field1": t.temperature, "field2": t.humidity}
        res = requests.post("https://api.thingspeak.com/update", data=data, timeout=10)
        print("update_id:", res.text)
        time.sleep(15)  # limite do plano gratuito
else:
    print("Defina THINGSPEAK_KEY para testar o envio.")
```

---

## 10) Reiniciar o assinante ou mudar de tópico (se precisar)

```python
stop_subscriber()       # para o assinante atual
# (opcional) mudar BROKER_HOST/PORT/TOPIC aqui
start_subscriber()      # inicia novamente
```

---

## 11) Desafios / Exercícios para a turma

> **Nível 1 – aquecimento**

1. **Trocar o tópico**: crie `TOPIC = f"aula_iot/{CLASS_ID}/grupo1"` (ou outro sufixo) e repita a demo.
2. **Adicionar campo novo** em `Telemetry` (ex.: `pressure`), publicar e **ver no DataFrame**.
3. **Aumentar a taxa**: no publisher, reduza `delay_s` e observe o gráfico.

**Nível 2 – MQTT**
4\. No `publish_n_messages`, mude para `qos=1` e observe comportamento (confirmação do broker).
5\. Faça o **publisher** enviar mensagens **retidas** (`retain=True`) e note o efeito quando o subscriber se conecta depois.

**Nível 3 – análise**
6\. Calcule **média móvel** (ex.: janela 5) para `temperature` e plote junto no gráfico.
7\. Crie uma **regra de alerta** de “variação brusca” (ex.: `abs(delta_temp) > 2.5` entre leituras consecutivas).

**Nível 4 – REST**
8\. Construa um **payload agregando** 10 leituras e poste para `httpbin.org/post` (um array de leituras).
9\. (Casa) Substitua o `httpbin` por uma **API real** sua (ou do laboratório) e valide a autenticação com `headers`.

**Nível 5 – extra (para grupos curiosos)**
10\. Publique em **dois tópicos** diferentes (ex.: `/sala1` e `/sala2`) e compare no gráfico.
11\. Projete um **mini-protocolo** no payload (ex.: `"type":"telemetry" | "alert" | "config"`), e trate no subscriber.

---

## 12) Explicação didática (o porquê de cada parte)

**Simulador**: evita hardware e foca no fluxo de dados.
**MQTT (broker público)**: demonstra _publish/subscribe_ sem infra local.
**HTTP (httpbin)**: mostra o modelo de **request/response** e JSON.
**Gráficos e regras**: dá senso de “produto” e materializa insights.
**Desafios**: permitem que cada grupo avance no seu ritmo e mostre criatividade.

---

## 13) Plano de aula sugerido (50–80 min)

1. **5 min** – visão geral e objetivo.
2. **15 min** – MQTT: start\_subscriber → publish\_n\_messages → gráfico.
3. **10 min** – HTTP: mostrar payload e POST no httpbin.
4. **10 min** – análise: regras simples + gráfico.
5. **10–30 min** – **desafios em grupos** (cada grupo escolhe 2–3).
6. **5 min** – socialização dos resultados.

Boa! Esse erro no E5 ocorre porque o DataFrame tem a coluna **`datetime`** (tipo `Timestamp` do pandas), que **não é serializável em JSON**. Há duas maneiras fáceis de resolver:

## ✅ Correção rápida (recomendado): enviar só colunas “primitivas”

Use apenas as colunas numéricas/strings do payload (sem `datetime`):

```python
import requests

df = df_from_received()
if len(df) >= 10:
    # Escolha apenas colunas serializáveis (ajusta se você adicionou 'pressure')
    cols = [c for c in ["device_id", "ts", "temperature", "humidity", "pressure"] if c in df.columns]
    df2 = df.sort_values("ts").tail(10)[cols].copy()

    # Garante tipos nativos (float/str)
    for c in ["ts", "temperature", "humidity", "pressure"]:
        if c in df2.columns:
            df2[c] = df2[c].astype(float)

    body = {"batch": df2.to_dict(orient="records")}
    r = requests.post("https://httpbin.org/post", json=body, timeout=10)
    print("Status:", r.status_code)
    echo = r.json().get("json", {})
    print("Echo json (chaves):", list(echo.keys()))
    print("Qtd itens ecoados:", len(echo.get("batch", [])))
else:
    print("Precisa de ao menos 10 leituras — publique mais.")
```

## 🛠️ Alternativa: serializar você mesmo (convertendo tipos automaticamente)

Se quiser enviar **qualquer** coluna (inclusive `datetime`), converta tudo para string ao serializar:

```python
import json, requests

df = df_from_received()
if len(df) >= 10:
    df2 = df.sort_values("ts").tail(10).copy()
    # Se tiver a coluna datetime, transforma em ISO 8601
    if "datetime" in df2.columns:
        df2["datetime"] = df2["datetime"].dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    body = {"batch": df2.to_dict(orient="records")}
    payload = json.dumps(body, default=str)  # <- converte objetos não-JSON para string
    r = requests.post(
        "https://httpbin.org/post",
        data=payload,
        headers={"Content-Type": "application/json"},
        timeout=10
    )
    print("Status:", r.status_code)
    echo = r.json().get("json", {})
    print("Echo json (chaves):", list(echo.keys()))
    print("Qtd itens ecoados:", len(echo.get("batch", [])))
else:
    print("Precisa de ao menos 10 leituras — publique mais.")
```

> Dica: como regra geral, **não inclua objetos do pandas** (Timestamp, NA, etc.) diretamente no `json=` do `requests`. Ou **filtre para tipos primitivos** (str/int/float/bool/list/dict) ou **serialize você mesmo** com `json.dumps(..., default=str)` + `headers`.
