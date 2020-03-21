from pyspark.sql import SparkSession
from pyspark.sql import Row
spark = SparkSession \
    .builder \
    .appName("asd") \
    .master('spark://spark-master:7077') \
    .config("hive.metastore.uris", "thrift://hive-metastore:9083") \
    .enableHiveSupport() \
    .getOrCreate()