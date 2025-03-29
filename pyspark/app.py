from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession


if __name__ == '__main__':

    spark = SparkSession.builder \
        .appName("BigQueryExample") \
        .config("spark.jars.packages", "com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.32.0") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .config("spark.sql.session.timeZone", "UTC") \
        .config("credentialsFile", "/mnt/c/projeto_tim/tim-bigdata-dev-ca1f-e540108b3c2d1.json") \
        .config("viewsEnabled", "true") \
        .config("cacheExpirationTimeInMinutes", "30") \
        .getOrCreate()

    df = spark.read.format("bigquery") \
        .option("table", "tim-bigdata-dev-ca1f:trusted_redes_sdk.tb_base_sdk_padrao_cristofer") \
        .load()

    df.show(5)

    # # Create a SparkContext with the desired configuration
    # conf = SparkConf()
    # conf.setAppName("My app")
    # conf.set("spark.executor.memory", "1g")
    # sc = SparkContext(conf=conf)

    # # Do something to prove it works
    # rdd = sc.parallelize(range(1000))
    # rdd.takeSample(False, 5)
    # # Stop the context
    # sc.stop()