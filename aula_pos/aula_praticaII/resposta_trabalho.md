# **Trabalho de Pós – Integração Spark SQL, EDA, ML, Word Cloud e Complexidade**

> **Como usar:** crie um notebook no Google Colab e cole cada bloco (Markdown ou Código) na ordem. As linhas com `!pip install` ficam comentadas; descomente se precisar instalar.

---

## 1) Setup — Instalação de dependências (Colab)

```python
# Se estiver no Google Colab, descomente conforme necessário:
# !pip install -q pyspark==3.5.2
# !pip install -q findspark
# !pip install -q wordcloud
# !pip install -q matplotlib pandas numpy scikit-learn
```

---

## 2) Imports principais

```python
import os, sys, time, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Spark
try:
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col, sum as sum_, avg, expr, countDistinct, struct, desc, percentile_approx
    from pyspark.ml.feature import VectorAssembler
    from pyspark.ml.regression import DecisionTreeRegressor
    from pyspark.ml.evaluation import RegressionEvaluator
    from pyspark.ml import Pipeline
    spark_available = True
except Exception as e:
    print("⚠️ Pyspark não está disponível. Instale e reinicie o runtime, se necessário.")
    spark_available = False

# Wordcloud (opcional)
try:
    from wordcloud import WordCloud
    wordcloud_available = True
except Exception as e:
    print("⚠️ wordcloud não está disponível. Instale para habilitar a nuvem de palavras.")
    wordcloud_available = False

# Keras (opcional)
try:
    import tensorflow as tf
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error, mean_absolute_error
    keras_available = True
except Exception as e:
    print("⚠️ TensorFlow/Keras não estão disponíveis. Ignore a seção de RNA ou instale.")
    keras_available = False

print("Spark disponível:", spark_available)
print("Wordcloud disponível:", wordcloud_available)
print("Keras disponível:", keras_available)
```

---

## 3) Iniciar sessão Spark

```python
if spark_available:
    spark = SparkSession.builder.appName("TrabalhoPOS").getOrCreate()
    print(spark)
else:
    spark = None
```

---

## 4) Carregar dados (California Housing em `sample_data`)

```python
def find_california_path():
    # Paths comuns no Colab
    paths = [
        "/content/sample_data/california_housing_train.csv",
        "/content/sample_data/california_housing_test.csv"
    ]
    for p in paths:
        if os.path.exists(p):
            return p
    return None

dataset_path = find_california_path()
print("Dataset encontrado:", dataset_path)

if spark and dataset_path:
    df = spark.read.csv(dataset_path, header=True, inferSchema=True)
    df.printSchema()
    df.show(5)
    df.describe().show()
else:
    print("⚠️ Spark ou dataset não disponível. Verifique a instalação/paths.")
```

---

## 5) EDA com Spark SQL (views & consultas)

```python
if spark and dataset_path:
    df.createOrReplaceTempView("hab")

    print("Média do valor das casas:")
    spark.sql("SELECT AVG(median_house_value) AS mean_mhv FROM hab").show()

    print("Mediana aproximada do valor das casas:")
    spark.sql("""
        SELECT percentile_approx(median_house_value, 0.5) AS median_mhv
        FROM hab
    """).show()

    print("Contagem de 'bairros' (proxy: pares únicos lat/long):")
    # usar struct para contar o par latitude/longitude
    spark.sql("""
        SELECT COUNT(DISTINCT struct(latitude, longitude)) AS bairros_unicos
        FROM hab
    """).show()

    print("Área mais populosa (por lat/long):")
    spark.sql("""
        SELECT latitude, longitude, SUM(population) AS pop_total
        FROM hab
        GROUP BY latitude, longitude
        ORDER BY pop_total DESC
        LIMIT 1
    """).show()

    print("Lat/Long com maior idade média das casas:")
    spark.sql("""
        SELECT latitude, longitude, AVG(housing_median_age) AS idade_media
        FROM hab
        GROUP BY latitude, longitude
        ORDER BY idade_media DESC
        LIMIT 1
    """).show()
else:
    print("⚠️ EDA via Spark SQL não executado (Spark/dataset ausentes).")
```

---

## 6) Visualizações (Matplotlib)

```python
if spark and dataset_path:
    pdf = df.select("median_house_value","median_income","latitude","longitude").dropna().toPandas()

    # Boxplot do valor das casas
    plt.figure()
    plt.boxplot(pdf["median_house_value"], vert=True, labels=["median_house_value"])
    plt.title("Distribuição de median_house_value")
    plt.show()

    # Scatter latitude vs longitude (cor: renda média)
    plt.figure()
    sc = plt.scatter(pdf["longitude"], pdf["latitude"], c=pdf["median_income"], s=10)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Mapa (lat/long) colorido por median_income")
    plt.colorbar(sc, label="median_income")
    plt.show()
else:
    print("⚠️ Visualizações não executadas (Spark/dataset ausentes).")
```

---

## 7) Nuvem de Palavras (opcional)

```python
if spark and dataset_path and wordcloud_available:
    pdf = df.select("median_income").dropna().toPandas()
    # rótulos sintéticos com base na mediana da renda
    labels = ["renda_alta" if v > pdf["median_income"].median() else "renda_baixa"
              for v in pdf["median_income"]]
    texto = " ".join(labels)

    wc = WordCloud(width=800, height=400, background_color="white").generate(texto)
    plt.figure(figsize=(10,5))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title("Nuvem de Palavras — faixas de renda (sintético)")
    plt.show()
else:
    print("⚠️ Nuvem não gerada (wordcloud/Spark/dataset ausentes).")
```

---

## 8) Modelagem — Árvore de Decisão (Spark ML)

```python
if spark and dataset_path:
    features = ["longitude","latitude","housing_median_age","total_rooms",
                "total_bedrooms","population","households","median_income"]
    cols = features + ["median_house_value"]
    df_model = df.select(*cols).dropna()

    assembler = VectorAssembler(inputCols=features, outputCol="features")
    dt = DecisionTreeRegressor(featuresCol="features",
                               labelCol="median_house_value",
                               maxDepth=8, seed=42)
    pipe = Pipeline(stages=[assembler, dt])

    train, test = df_model.randomSplit([0.8, 0.2], seed=42)
    model = pipe.fit(train)
    pred = model.transform(test)

    evaluator_rmse = RegressionEvaluator(labelCol="median_house_value",
                                         predictionCol="prediction",
                                         metricName="rmse")
    evaluator_mae  = RegressionEvaluator(labelCol="median_house_value",
                                         predictionCol="prediction",
                                         metricName="mae")
    rmse = evaluator_rmse.evaluate(pred)
    mae  = evaluator_mae.evaluate(pred)

    print("DecisionTreeRegressor → RMSE:", rmse, " | MAE:", mae)

    # Importância de atributos
    try:
        tree_model = model.stages[-1]
        importances = list(zip(features, tree_model.featureImportances.toArray()))
        importances_sorted = sorted(importances, key=lambda x: x[1], reverse=True)
        print("Importâncias de atributos (decrescente):")
        for feat, imp in importances_sorted:
            print(f"{feat}: {imp:.4f}")
    except Exception as e:
        print("Não foi possível obter importâncias:", e)
else:
    print("⚠️ Modelagem Spark ML não executada (Spark/dataset ausentes).")
```

---

## 9) Modelagem — Rede Neural (Keras, opcional)

```python
if spark and dataset_path and keras_available:
    features = ["longitude","latitude","housing_median_age","total_rooms",
                "total_bedrooms","population","households","median_income"]
    cols = features + ["median_house_value"]
    pdf = df.select(*cols).dropna().toPandas()

    X = pdf[features].values
    y = pdf["median_house_value"].values

    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

    model = Sequential([
        Dense(64, activation="relu", input_shape=(X.shape[1],)),
        Dense(32, activation="relu"),
        Dense(1)
    ])
    model.compile(optimizer="adam", loss="mse")
    model.fit(X_tr, y_tr, epochs=20, batch_size=64, verbose=0)

    y_pred = model.predict(X_te).ravel()
    rmse = mean_squared_error(y_te, y_pred, squared=False)
    mae  = mean_absolute_error(y_te, y_pred)
    print("Keras MLP → RMSE:", rmse, " | MAE:", mae)
else:
    print("⚠️ Modelagem Keras não executada (Spark/Keras/dataset ausentes).")
```

---

## 10) Complexidade e Vetorização

```python
import time

def O1(lst):
    start = time.perf_counter()
    _ = lst[0] if lst else None
    return time.perf_counter() - start

def On(n):
    start = time.perf_counter()
    s = 0
    for i in range(n):
        s += i
    return time.perf_counter() - start

def On2(n):
    start = time.perf_counter()
    c = 0
    for i in range(n):
        for j in range(n):
            c += 1
    return time.perf_counter() - start

def soma_loop(n):
    s = 0
    for i in range(n):
        s += i
    return s

def soma_numpy(n):
    return np.sum(np.arange(n))

lst = list(range(100))
t_O1  = O1(lst)
t_On  = On(10**6)      # Ajuste para runtime
t_On2 = On2(600)       # Ajuste para não demorar em excesso

print(f"O(1): {t_O1:.6f}s, O(n): {t_On:.6f}s, O(n^2): {t_On2:.6f}s")

n = 10**7
t = time.perf_counter(); soma_loop(n); t_loop = time.perf_counter()-t
t = time.perf_counter(); soma_numpy(n); t_np   = time.perf_counter()-t
print(f"Soma com loop: {t_loop:.4f}s  |  Soma com NumPy: {t_np:.4f}s")
```

---

## 11) Conclusões (preencha)

```markdown
### Conclusões
- Comparação **DT vs RNA**:
- Atributos mais relevantes e interpretação:
- Limitações do pipeline:
- Próximos passos (normalização, tuning, CV, engenharia de atributos, etc.):
```

<https://colab.research.google.com/drive/19EehzAPlXXRlhuTf4D-FOStaqopIymyZ?usp=sharing>
