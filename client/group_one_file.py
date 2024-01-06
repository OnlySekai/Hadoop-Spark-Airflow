from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
sc = SparkContext.getOrCreate(
    SparkConf().setMaster("spark://spark-master:7077"))
spark = SparkSession.builder.appName('app').getOrCreate()
#combine all transaction files into one file
df = spark.read.csv('hdfs://namenode:9000/transaction*.csv',
                    header=True, inferSchema=True)
df.coalesce(1).write.format("csv").option("header", "true").save('hdfs://namenode:9000/group-trx.csv')
