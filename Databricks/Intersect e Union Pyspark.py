from pyspark.sql import SparkSession
from pyspark.sql.functions import array, lit
from pyspark.sql.functions import array_union, array_intersect

# Criar uma SparkSession
spark = SparkSession.builder.appName("ArrayExample").getOrCreate()

# Criar DataFrame com arrays arr1 e arr2
data = [
    (['a', 'b', 'c'], ['b', 'c', 'd']),
    (['a', 'd'], ['e', 'd', 'f']),
    (['g', 'h'], ['i', 'h']),
    (['a', 'b', 'f'], ['f', 'g', 'h']),
    (['x', 'y', 'z'], ['x', 'z']),
    # Repetindo dados para ter 20 linhas
    (['a', 'b', 'c'], ['b', 'c', 'd']),
    (['a', 'd'], ['e', 'd', 'f']),
    (['g', 'h'], ['i', 'h']),
    (['a', 'b', 'f'], ['f', 'g', 'h']),
    (['x', 'y', 'z'], ['x', 'z']),
    (['a', 'b', 'c'], ['b', 'c', 'd']),
    (['a', 'd'], ['e', 'd', 'f']),
    (['g', 'h'], ['i', 'h']),
    (['a', 'b', 'f'], ['f', 'g', 'h']),
    (['x', 'y', 'z'], ['x', 'z']),
    (['a', 'b', 'c'], ['b', 'c', 'd']),
    (['a', 'd'], ['e', 'd', 'f']),
    (['g', 'h'], ['i', 'h']),
    (['a', 'b', 'f'], ['f', 'g', 'h']),
    (['x', 'y', 'z'], ['x', 'z']),
]

columns = ['arr1', 'arr2']

df = spark.createDataFrame(data, columns)

df.show(truncate=False)

# Aplicar array_union e array_intersect
df_result = df.withColumns({
    "arr_union": array_union(df.arr1, df.arr2),
    "arr_intersect": array_intersect(df.arr1, df.arr2)
})

df_result.show(truncate=False)