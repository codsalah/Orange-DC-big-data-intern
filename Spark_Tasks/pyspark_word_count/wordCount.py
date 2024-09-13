from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode, count, col
from pyspark.sql.types import StringType

spark = SparkSession.builder \
    .appName("WordCount") \
    .master("local[*]") \
    .getOrCreate()


input_path = "./Spark_Tasks/pyspark_word_count/Input/The_Book_of_Boba_Fett.txt"
output_path = "./Spark_Tasks/pyspark_word_count/output"
df = spark.read.text(input_path)

# Split each line into words and create a new DataFrame with a single column "word"
words_df = df.select(explode(split(col("value"), "\\s+")).alias("word"))

# Count the occurrences of each word
word_count_df = words_df.groupBy("word").agg(count("word").alias("count"))

# Show result
word_count_df.show()

# Save the output to a file
word_count_df.write.csv(output_path, mode="overwrite")

# Stop the Session
spark.stop()