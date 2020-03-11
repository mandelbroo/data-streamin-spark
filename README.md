1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

I has optimized the amount of rows processed per second.

2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

spark.sql.shuffle.partitions - number of partitions to use when shuffling data for joins or aggregations.

spark.default.parallelism - total number of cores on all executor nodes.

spark.streaming.kafka.maxRatePerPartition - maximum rate at which data will be read from each Kafka partition.
