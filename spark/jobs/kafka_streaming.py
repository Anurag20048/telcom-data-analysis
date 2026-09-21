from pyspark.sql import SparkSession
from pyspark.sql.functions import col,from_json,window,count
from pyspark.sql.types import StructType,StructField,StringType,IntegerType
spark=SparkSession.builder.appName("TelecomKafkaStreaming").getOrCreate()
schema=StructType([StructField("event_id",StringType()),StructField("event_type",StringType()),StructField("customer_id",IntegerType()),StructField("event_time",StringType()),StructField("source",StringType())])
raw=spark.readStream.format("kafka").option("kafka.bootstrap.servers","kafka:29092").option("subscribe","telecom-events").option("startingOffsets","earliest").load()
events=raw.selectExpr("CAST(value AS STRING) AS json_value").select(from_json(col("json_value"),schema).alias("e")).select("e.*").withColumn("event_time",col("event_time").cast("timestamp"))
metrics=events.withWatermark("event_time","10 minutes").groupBy(window("event_time","5 minutes"),"event_type").agg(count("*").alias("event_count"))
metrics.writeStream.outputMode("append").format("console").option("truncate","false").start().awaitTermination()
