%python

empresa1 = spark.createDataFrame(
    [
        ("Joao Santos", 2000),
        ("Carlos Fernandez", 3400)
    ], ["Funcionario", "Salario"])
display(empresa1)
empresa1.printSchema()

#Setando o local de armazenamento dos arquivos parquet 

%python
parquetpath = "dbfs://FileStore/tables/delta/schema_evolution/parquet"

#Criando arquivos parquet com base no primeiro dataframe

%python
(
    empresa1
        .write
        .format('parquet')
        .save('/FileStore/tables/delta/schema_evolution/parquet')     
)
spark.read.parquet(oarquetpath).show()

#Criando o segundo dataframe com dados, acrescentando novos campos(Setor, comissao)

%python

empresa2 = spark.createDataFrame(
    [
        ("Financeiro", 240),
        ("Marketing", 540),
    ], ['Setor', 'Comissao'])
display(empresa2)
empresa2.printschema()

#Apesar de colocar "append" no parquet, não houve evolução do esquema, as colunas foram substituidas

%python
empresa2.write.mode("append").parquet(parquetpath)
spark.read.parquet(parquetpath).show()

#Vamos gerar o Schema Evolution com as tabelas delta

%python
deltapath = "/FileStore/tables/delta/schema_evolution/delta"
(
    empresa1
    .write
    .format("delta")
    .save("/FileStore/tables/delta/schema_evolution/delta")
)
spark.read.format("delta").load(deltapath).show()

#Vamos realizar um merge entre os dataframes, note que agora conseguirá realizar a junção entre os schemas. Os dados inexistentes foram acrescidos de nulos. 

%python
(
    empresa2
    .write
    .format("delta")
    .mode('append')
    .option("mergeSchema", "true")
    .save(deltapath)
)
spark.read.format("delta").load(deltapath).show()

%python
empresa3 = spark.createDataFrame(
    [
        ("Sandra Lemos", 672),
        ("Carla Soares", 966),
    ],
    ["Funcionário", "Comissao"]
)

#Vamos acrescentar dados mais dados e verificar a inclusao apenas de alguns campos

%Python
(
    empresa3
    .write
    .format("delta")
    .mode("append")
    .option("mergeSchema", "true")
    .save(deltapath)
)
spark.read.format("delta").load(deltapath).show()

#Vamos sobreescrever toda a tabela, perceba as mudanças dos campos que ficaram e dos registros. "option=overwriteschema, mode=overwrite"

%python
(
    empresa3
    .write
    .format("delta")
    .mode("overwrite")
    .option("mergeSchema", "true")
    .save(deltapath)
)
spark.read.format("delta").load(deltapath).show()

#Vamos criar uma tabela delta com referencia aos parquet(delta) criados

%sql
CREATE TABLE tab_empresa(
    Funcionario STRING,
    Comissao long
    )
USING delta
LOCATION "/FileStore/tables/delta/schema_evolution/delta"

#Vamos listar o historico gerado de todas as nossas mudanças

%sql
DESCRIBE HISTORY '/FileStore/tables/delta/schema_evolution/delta'

#Listando todas as versões que podemos utilizar

%sql
SELECT * FROM delta. "/FileStore/tables/delta/schema_evolution/delta" VERSION AS OF 4
