#removendo o parquet e arquivos delta e vamos recriar a tabela de compras 
%fs rm -r /user/hive/warehouse/compras

#Carregando os dados do arquivo json
%python

dfcliente = spark.read.json("/FileStore/tables/cliente/clientes.json");
dfcliente.printSchema()
dfcliente.show()

%python
df = spark.read \
    .format('delta') \
    .option('versionAsOf', '1') \
    .load("/user/hive/warehouse/compras")
df.show()

#Contando a quantidade de registros na terceira versão via sql

%sql
SELECT count(*) FROM compras VERSION AS OF 3

#Contando a quantidade de registros na terceira versao via SQL - Outra forma de realizar a tarefa

%sql 
SELECT count(*) FROM compras@v3

select * from delta. '/user/hive/warehouse/compras@v3'


#Descrevendo o historico dos dados para verificar a quantidade de versões

%sql 
DESCRIBE HISTORY '/user/hive/warehouse/compras'

#vamos reinserir o registro com id = 1 que eliminamos, uma forma de realizar o delta time travel
insert into compras
select * from compras as version as of 1
where id = 1

#exibindo os dados atualizados apos o retorno da versão 1, ou seja o registro deletado foi restaurado 

%sql
select * from compras 


#mostrando as versões antes e depois do insert 