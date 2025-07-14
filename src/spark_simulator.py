# spark_simulator.py
# This module will simulate Spark jobs(word count, aggregation etc.)

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split

def run_word_count():

    # Creating a SparkSession
    spark = SparkSession.builder.appName("SpotInstanceSimulation").getOrCreate()

    # Loading sample CSV we have
    df = spark.read.csv("data/sample_data.csv", header = True, inferSchema = True)

    # Splitting text into words
    words_df = df.select(
        explode(split(df.text, " ")).alias("word")
    )


    # Counting Words
    word_count_df = words_df.groupBy("word").count()


    # Result
    word_count_df.show()

    # Stopping Spark Session
    spark.stop()

if __name__ == "__main__":
    run_word_count()
    