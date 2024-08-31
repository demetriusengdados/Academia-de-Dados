#%md

#Primeiro Script, trabalhando com carga de dados e ajuste de de registros no delta lake e carregando arquivos json

#%python
dfcliente = spark.read.json("/FileStore/tables/cliente/clientes.json");
dfcliente.printschema()
dfcliente.show()


#Cria Tabela temporaria e exibi a saida

#%python
dfcliente.createOrReplaceTempView("compras_view");
saida = spark.sql("SELECT * FROM compras_view")
saida.show()


#carrega os dados no delta lake gerando uma tabela chamada compras, note USING DELTA
#%scala 

val scrisql = "CREATE OR REPLACE TABLE compras (id STRING, date_order STRING, customer STRING, product STRING, unit INTEGER, price DOUBLE) using delta PARTITIONED BY (date_order)";
spark.sql(scrisql); 


#Lista os arquivos do delta lake que estará vazia 

#%scala
spark.sql("select * from compras").show()


#Criando um merge para carregar os dados da tabela temporaria no delta lake 

#%scala
val mergedados = "Merge into compras" +
    "using compras_view as cmp_view" +
    "On compras.id = cmp_view.id" + 
    "WHEN MATCHED  THEN" +
    "UPDATE SET compras.product = cmp_view_product," +
    "compras.price = cmp_view.price" + 
    'WHEN NOT MATCHED THEN INSERT *';

spark.sql(mergedados);

#Exibe os dados que foram carregados com o merge 

#%scala
spark.sql("select * from compras").show();


#Atualiza os dados do id=4 com o comando update
#%scala 
val atualiza_dados = "udpate compras" +
        "set product" = "Geladeira" +
        "where id = 4";
spark.sql(atualiza_dados);

#Exibe os dados que foram carregados, note a atualização no id = 4

#%scala
spark.sql('select * from compras').show();

#Eliminação do registro cujo id = 4
#%scala

val deletaregistro = 'delete from compras where id = 1';
spark.sql(deletaregistro);

#Exibe os dado que foram carregados 

#%scala
spark.sql('select * from compras').show();

