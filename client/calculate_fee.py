from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
sc = SparkContext.getOrCreate(
    SparkConf().setMaster("spark://spark-master:7077"))
spark = SparkSession.builder.appName('app').getOrCreate()
df = spark.read.csv('hdfs://namenode:9000/transaction*.csv',
                    header=True, inferSchema=True)
df.cache()
#count 
df_fee = df.groupBy('from').sum('gasPrice').withColumnRenamed(
    'sum(gasPrice)', 'fee').orderBy('fee', ascending=False)
# save to hdfs
df_fee.repartition(1).write.csv('hdfs://localhost:9000/fee.csv', header=True)
df_fee.write.csv('hdfs://namenode:9000/a_fee.csv')
