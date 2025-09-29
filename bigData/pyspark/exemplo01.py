from pyspark.sql import SparkSession
# Inicialize a sessão Spark
spark = SparkSession.builder \
      .appName("Exemplo Spark SQL no Colab") \
          .getOrCreate()
# Carrega um arquivo CSV, JSON, Parquet, etc.
dados = [(1, 'Raphael', 40),
         (2, 'Caroline', 31),
         (3, 'Vinicius', 48)]

df = spark.createDataFrame(dados, ['id', 'nome', 'idade'])
# Criar uma visão temporária
df.createOrReplaceTempView("pessoas")
consulta = "SELECT MAX(idade) AS max_idade FROM pessoas"
resultado = spark.sql(consulta)
max_idade = resultado.first()['max_idade']
print(f"A idade máxima é: {max_idade}")
spark.stop()