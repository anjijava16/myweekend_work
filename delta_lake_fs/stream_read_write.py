


scala> val streamingDf = spark.readStream.format("rate").load()
streamingDf: org.apache.spark.sql.DataFrame = [timestamp: timestamp, value: bigint]

scala> val stream = streamingDf.select($"value" as "id").writeStream.format("delta").option("checkpointLocation", "/tmp/checkpoint1").start("/tmp/delta-table1")
stream: org.apache.spark.sql.streaming.StreamingQuery = org.apache.spark.sql.execution.streaming.StreamingQueryWrapper@22448db4

2023-04-15 10:33:54,967 WARN hadoop.MemoryManager: Total allocation exceeds 95.00% (906,992,014 bytes) of heap memory
Scaling row group sizes to 96.54% for 7 writers
2023-04-15 10:33:54,978 WARN hadoop.MemoryManager: Total allocation exceeds 95.00% (906,992,014 bytes) of heap memory
Scaling row group sizes to 84.47% for 8 writers
2023-04-15 10:33:54,980 WARN hadoop.MemoryManager: Total allocation exceeds 95.00% (906,992,014 bytes) of heap memory
Scaling row group sizes to 75.08% for 9 writers
2023-04-15 10:33:54,981 WARN hadoop.MemoryManager: Total allocation exceeds 95.00% (906,992,014 bytes) of heap memory
Scaling row group sizes to 67.58% for 10 writers
2023-04-15 10:33:55,364 WARN hadoop.MemoryManager: Total allocation exceeds 95.00% (906,992,014 bytes) of heap memory
Scaling row group sizes to 75.08% for 9 writers
2023-04-15 10:33:55,369 WARN hadoop.MemoryManager: Total allocation exceeds 95.00% (906,992,014 bytes) of heap memory
Scaling row group sizes to 84.47% for 8 writers
2023-04-15 10:33:55,372 WARN hadoop.MemoryManager: Total allocation exceeds 95.00% (906,992,014 bytes) of heap memory
Scaling row group sizes to 96.54% for 7 writers


val stream2 = spark.readStream.format("delta").load("/tmp/delta-table1").writeStream.format("console").start()
