%fs ls /databricks-datasets/structured-streaming/events/

#Exibindo o conteúdo de 1 arquivo json

%python
#Lendo um arquivo JSON
dataf3 = spark.read.json("/databricks-datasets/structured-streaming/events/file-1.json")
dataf3.show()

#Criando um banco de dados em separado e uma tabela delta que irá receber os dados do json em streaming

%sql
CREATE DATABASE IF NOT EXISTS db_stream;
USE db_strean;
DROP TABLE IF EXISTS db_stream.tab_stream;
CREATE TABLE db_stream.tab_stream(
    action STRING,
    time STRING
)
USING delta
LOCATION "/tmp/delta/events"

#Executando a carga na pasta do Delta Lake, onde serão armazenadas os dados

%python
from pyspark.sql.functions import *
from pyspark.sql.types import *

#Streaming reads and append into delta table(Start!)
read_schema = StructType([
    StructField("action", StringType(), False),
    StructField("time", StringType(), True)
])
df2 = (spark.readStream
       .option("maxFilesPerTrigger", 1)
       .schema(read_schema)
       .json("/databricks-datasets/structured-streaming/events/"))
(df2.writeStream
 .format(delta)
 .outputMode("append")
 .option("checkpointLocation", "/tmp/delta/checkpoint")
 .option("path", '/tmp/delta/events').start())

#Exibindo os dados em tempo real oriunda da tabela delta 
%sql

select distinct action, count(*) from db_stream.tab_stream
    group by action

#Listando os hsitoricos registrados na tabela delta

%sql
DESCRIBE HISTORY '/tmp/delta/events'

