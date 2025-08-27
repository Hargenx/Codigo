# **Trabalho de Pós-Graduação – Integração de Ciência de Dados com PySpark, Machine Learning e Análise Exploratória**

## **Objetivo Geral**

Aplicar conceitos de ciência de dados, aprendizado de máquina e processamento distribuído utilizando **PySpark** e **bibliotecas Python** para realizar análise, modelagem e avaliação de dados, integrando técnicas aprendidas nas duas apresentações.

---

## **1. Introdução**

O trabalho deve iniciar com uma **breve fundamentação teórica** (máx. 1 página) abordando:

* **Big Data e Apache Spark** – arquitetura básica, RDDs, transformações e ações.
* **Machine Learning** – visão geral sobre Árvores de Decisão e Redes Neurais Artificiais.
* **Complexidade Computacional** – importância na escolha de algoritmos eficientes.
* **Visualização de Dados** – papel na extração de insights.

---

## **2. Base de Dados**

O aluno deverá:

1. Utilizar o conjunto **`california_housing_train.csv`** (já disponível no Colab) ou outro dataset público.
2. Carregar os dados no **PySpark DataFrame**.
3. Explorar com:

   * `.printSchema()`
   * `.show(5)`
   * `.describe()`

---

## **3. Análise Exploratória de Dados (EDA)**

1. Criar **visão temporária** no Spark SQL.
2. Executar consultas para:

   * Média e mediana do valor das casas.
   * Bairros únicos e área mais populosa.
   * Latitude/longitude com maior idade média das casas.
3. Exportar algum resultado para Pandas e gerar:

   * **Boxplot** de distribuição de valores.
   * **Nuvem de Palavras** (usando descrições ou variáveis textuais, caso existam).

---

## **4. Modelagem Preditiva**

1. Escolher uma **variável alvo** (ex.: `median_house_value`).
2. Treinar dois modelos:

   * **Árvore de Decisão** (Spark MLlib ou sklearn).
   * **Rede Neural Artificial** (TensorFlow/Keras).
3. Comparar desempenho com:

   * **Regressão**: MAE, MSE, RMSE.
   * **Classificação** (caso faça discretização do alvo): acurácia, precisão, recall, F1-score.

---

## **5. Complexidade e Otimização**

1. Criar exemplos de funções com **O(1)**, **O(n)** e **O(n²)**.
2. Comparar execução com e sem vetorização (NumPy).
3. Discutir brevemente o impacto dessas escolhas no contexto de Big Data.

---

## **6. Entrega**

O relatório final deve conter:

* **Introdução** (fundamentos teóricos).
* **Metodologia** (passo a passo da análise).
* **Resultados** (prints, gráficos, tabelas).
* **Discussão** (comparação de modelos, implicações práticas).
* **Conclusão** (síntese e possíveis melhorias).
