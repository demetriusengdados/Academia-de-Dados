#%sql

DROP TABLE IF EXISTS hotel; 

CREATE TABLE hotel 
USING parquet
PARTITIONED BY (Categoria)
SELECT _c0 as Ordem, _c1 as Tipo, _c2 as Situacao, _c3 as Tip_local, _c4 as Categoria, _c5 as Tipo_local2, _c6 as Tipo_local3, _c7 as Acomodacao, _c8 as Cidade,
_c9 as Pais, _c10 as Endereco, _c11 as Latitude, _c12 as Longitude, _c13 as Provincia, _c14 as CEP, _c15 as UF, _c16 as Data_estadia, _c17, as Revisao_texto, _c18 as Revisao_titulo,
c_19 as Revisao_cidade, _c20 as Endereco_web, _c21 as Comentario_usuario, _c22 as Resumo, _c23 as Comentario2, _c24 as Comentario3, _c25 as Comentario4
FROM csv. 'dbfs:/FileStore/tables/hotel/Datafiniti_Hotel_Reviews_jun19.csv'

#%sql

#Fazendo uma contagem das principais categorias e comentarios

SELECT Categoria,Comentario2,Comentario3, count(*) as TOTAL
FROM hotel
GROUP BY Categoria, Comentario2, Comentario3
ORDER BY Categoria, Total DES;

#%sql 

#Criando a tabela delta

DROP TABLE IF EXISTS hotel;

CREATE TABLE hotel
using delta
PARTITIONED BY (categoria)
SELECT _c0 as Ordem, _c1 as Tipo, _c2 as Situacao, _c3 as Tip_local, _c4 as Categoria, _c5 as Tipo_local2, _c6 as Tipo_local3, _c7 as Acomodacao, _c8 as Cidade,
_c9 as Pais, _c10 as Endereco, _c11 as Latitude, _c12 as Longitude, _c13 as Provincia, _c14 as CEP, _c15 as UF, _c16 as Data_estadia, _c17, as Revisao_texto, _c18 as Revisao_titulo,
c_19 as Revisao_cidade, _c20 as Endereco_web, _c21 as Comentario_usuario, _c22 as Resumo, _c23 as Comentario2, _c24 as Comentario3, _c25 as Comentario4
FROM csv. 'dbfs:/FileStore/tables/hotel/Datafiniti_Hotel_Reviews_jun19.csv'

#%sql

#Otimizando a consulta da tabela delta com o campo Pais, é importante que busque o campo que melhor otimiza

OPTIMIZE hotel ZORDER BY (Pais);

#Executando a consulta otimizada na tabela delta
Select Categoria, Comentario2, Comentario3, count(*) as Total
From hotel
GROUP BY Categoria, Comentario2, Comentario3
ORDER BY Categoria, Total Desc;
