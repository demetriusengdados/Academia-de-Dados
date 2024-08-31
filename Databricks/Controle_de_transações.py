#Criação das tabelas TB_AUTOR, TB_LIVRO, e a associativa TB_LIVRO_AUTOR

#%scala

val Tscrisql = 'CREATE OR REPLACE TABLE TB_AUTOR (ID_AUTOR DOUBLE, NOME STRING, SEXO STRING, DATA_NASCIMENTO STRING) USING DELTA;'
spark.sql(Tscrisql);

val Tscrisql1 = 'CREATE OR REPLACE TABLE TB_LIVRO (ID_LIVRO DOUBLE, ISBN STRING, TITULO STRING, EDICAO DOUBLE, PRECO DOUBLE, QTDE_ESTOQUE DOUBLE) USING DELTA;'
spark.sql(Tscrisql1);

val Tscrisql3 = 'CREATE OR REPLACE TABLE TB_LIVRO_AUTOR (ID_LIVRO_AUTOR DOUBLE, ID_LIVRO DOUBLE, ID_AUTOR DOUBLE) USING DELTA;'
spark.sql(Tscrisql3);

#Inserção de registros na tabela tb_autor

%scala 

val scrisql = 'Insert into TB_AUTOR (ID_AUTOR, NOME, SEXO, DATA_NASCIMENTO) values (1, 'Joao', 'M', '01/01/1970');'
spark.sql(scrisql);
val scrisql1 = 'Insert into TB_AUTOR (ID_AUTOR, NOME, SEXO, DATA_NASCIMENTO) values (2, 'Maria', 'F', '25/11/1975');'
spark.sql(scrisql1);
val scrisql2 = 'Insert into TB_AUTOR (ID_AUTOR, NOME, SEXO, DATA_NASCIMENTO) values (3, 'Sandra', 'F', '14/11/1978');'
spark.sql(scrisql2);
val scrisql3 = 'Insert into TB_AUTOR (ID_AUTOR, NOME, SEXO, DATA_NASCIMENTO) VALUES (4, 'Tereza', 'F', '21/11/1978');'
spark.sql(scrisql3);

#Inserção de registros na tabela TB_LIVRO

#%scala
val Lscrisql = 'Insert into TB_LIVRO (ID_LIVRO, ISBN, TITULO, EDICAO, PRECO, QTDE_ESTOQUE) values (1, '1234567890', 'Banco de Dados', 2,10,407);'
spark.sql(Lscrisql);
val Lscrisql1 = 'Insert into TB_LIVRO (ID_LIVRO, ISBN, TITULO, EDICAO, PRECO, QTDE_ESTOQUE) values (2, '2345678901', 'Redes de Computadore', 1,10,60);'
spark.sql(Lscrisql1);
val Lscrisql2 = 'Insert into TB_LIVRO (ID_LIVRO, ISBN, TITULO, EDICAO, PRECO, QTED_ESTOQUE) values (3, '3456789012', 'Interface Homem Maquina', 3,10,10);'
spark.sql(Lscrisql2);


#Inserção de registros na tabela TB_LIVRO_AUTOR
#%scala
val LAscrisql = "Insert into TB_AUTOR_LIVRO (ID_LIVRO_AUTOR, ID_LIVRO, ID_AUTOR) values (1, 1, 1);"
spark.sql(LAscrisql);
val LAscrisql1 = "Insert into TB_AUTOR_LIVRO (ID_LIVRO_AUTOR, ID_LIVRO, ID_AUTOR) values (2, 1, 2);"
spark.sql(LAscrisql1);
val LAscrisql2 = "Insert into TB_AUTOR_LIVRO (ID_LIVRO_AUTOR, ID_LIVRO, ID_AUTOR) values (3, 2, 3);"
spark.sql(LAscrisql2);
val LAscrisql3 = "Insert into TB_AUTOR_LIVRO (ID_LIVRO_AUTOR, ID_LIVRO, ID_AUTOR) values (4, 3, 2);"
spark.sql(LAscrisql3);
val LAscrisql4 = "Insert into TB_AUTOR_LIVRO (ID_LIVRO_AUTOR, ID_LIVRO, ID_AUTOR) values (5, 3, 3);"
spark.sql(LAscrisql4);

#Selecionando os registros, ligando todas as tabelas 

#%sql
SELECT TB_LIVRO.TITULO, TB_LIVRO.ISBN, TB_LIVRO.PRECO, TB_AUTOR.NOME, TB_AUTOR.DATA_NASCIMENTO FROM TB_LIVRO
    INNER JOIN TB_LIVRO_AUTOR ON TB_LIVRO.ID_LIVRO = TB_LIVRO_AUTOR.ID_LIVRO
    INNER JOIN TB_AUTOR ON TB_AUTOR.ID_AUTOR = TB_LIVRO_AUTOR.ID_AUTOR


#Criando uma check constrains para a tabela TB_AUTOR, somente permitindo a inserção de 4 registros
#%sql 

ALTER TABLE TB_AUTOR DROP CONSTRAINT validIds;
ALTER TABLE TB_AUTOR ADD CONSTRAINT validIds CHECK (ID_AUTOR > 0 AND ID_AUTOR < 5);
SHOW TBLPROPERTIES TB_AUTOR;


#Verificando se a check constraint irá funcionar executando um insert
#%scala
val scrisql = "Insert into TB_AUTOR (ID_AUTOR, NOME, SEXO, DATA_NASCIMENTO) values (5, 'Joao', 'M', '01/01/1970');"
spark.sql(scrisql);


