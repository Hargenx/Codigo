import json
from itertools import islice, cycle
from pathlib import Path
import pandas as pd

# --- 0) Entrada (caminho baseado no arquivo) ---
BASE_DIR = Path(__file__).resolve().parent
json_path = (BASE_DIR.parent / "data" / "bonus.json").resolve()

print(f"Lendo JSON em: {json_path}")
if not json_path.exists():
    raise FileNotFoundError(f"Arquivo não encontrado: {json_path}")

# --- 1) Ler JSON: Series {nome: salario} OU dict com listas ---
try:
    # Ex.: {"Alice": 2000, ...}
    dados = pd.read_json(json_path, typ="series")
    df = pd.DataFrame(list(dados.items()), columns=["Nome", "Salário"])
except ValueError:
    # Fallback: {"Nome":[...], "Salário":[...]}
    with open(json_path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    if set(raw.keys()) >= {"Nome", "Salário"}:
        df = pd.DataFrame(raw)[["Nome", "Salário"]]
    else:
        raise ValueError(
            "Formato do JSON não reconhecido. Esperado: series (nome->salário) "
            "ou dict com chaves 'Nome' e 'Salário'."
        )

# --- 2) Bônus (10%) ---
df["Bônus"] = (df["Salário"] * 0.10).round(2)

# --- 3) Cargo -> 'Título do Cargo' (ajusta ao tamanho do DF) ---
cargos_base = [
    "Gerente", "Assistente", "Diretor", "Analista",
    "Estagiário", "Estagiário", "Analista", "Diretor",
    "Gerente", "Diretor"
]
df["Cargo"] = list(islice(cycle(cargos_base), len(df)))
df = df.rename(columns={"Cargo": "Título do Cargo"})

# --- 4) Média salarial por título (desc) ---
media_por_cargo = (
    df.groupby("Título do Cargo", as_index=False)["Salário"]
      .mean()
      .rename(columns={"Salário": "Média Salarial"})
      .sort_values("Média Salarial", ascending=False)
)

# --- 5) DF final ordenado por Nome (crescente) ---
df_final = (
    df.sort_values("Nome")[["Nome", "Salário", "Bônus", "Título do Cargo"]]
      .reset_index(drop=True)
)

# --- 6) Exibir ---
print("DataFrame final (ordenado por Nome):")
print(df_final.to_string(index=False))

print("\nMédia salarial por Título do Cargo (desc):")
print(media_por_cargo.to_string(index=False))

# --- 7) Persistência (opcional) ---
out_dir = BASE_DIR.parent / "data" / "out"
out_dir.mkdir(parents=True, exist_ok=True)
df_final.to_csv(out_dir / "funcionarios_final.csv", index=False, encoding="utf-8")
media_por_cargo.to_csv(out_dir / "media_salarial_por_titulo.csv", index=False, encoding="utf-8")


import matplotlib.pyplot as plt
# Calcular a média dos salários por título do cargo
agregado = df.groupby('Título do Cargo')['Salário'].mean().reset_index()
agregado.rename(columns={'Salário': 'Média de Salário'}, inplace=True)
# Gráfico 1: Salário por Funcionário
plt.figure(figsize=(10, 6))
plt.bar(df['Nome'], df['Salário'])
plt.title('Salário por Funcionário')
plt.xlabel('Funcionário')
plt.ylabel('Salário (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt
# Configurar estilo do Seaborn (opcional)
sns.set_theme(style="darkgrid")
# Criar um gráfico de barras da média salarial por título do cargo
plt.figure(figsize=(10, 6))
sns.barplot(x='Média de Salário', y='Título do Cargo', data=agregado, palette="viridis", hue="Título do Cargo", legend=False)
plt.xlabel('Média de Salário')
plt.ylabel('Título do Cargo')
plt.title('Média de Salário por Título do Cargo')
plt.show()

import altair as alt
# Criar um gráfico de barras interativo da média salarial por título do cargo
chart = alt.Chart(agregado).mark_bar().encode(
    x='Média de Salário:Q',
    y=alt.Y('Título do Cargo:N', sort='-x'),
    tooltip=['Título do Cargo:N', 'Média de Salário:Q']
).properties(
    title='Média de Salário por Título do Cargo'
)
chart.interactive().show()
import webbrowser
chart = chart.properties(width=700, height=350).interactive()
chart.save("media_por_cargo_altair.html")
webbrowser.open("media_por_cargo_altair.html")


import plotly.express as px
# Criar um gráfico de barras interativo da média salarial por título do cargo
fig = px.bar(agregado, x='Média de Salário', y='Título do Cargo', text='Média de Salário',orientation='h', title='Média de Salário por Título do Cargo')
fig.update_traces(marker_color='skyblue', texttemplate='%{text:.2s}', textposition='inside')
fig.update_layout(xaxis_title='Média de Salário', yaxis_title='Título do Cargo')
fig.write_html("media_por_cargo.html", auto_open=True)



