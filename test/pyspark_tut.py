from pyspark.sql import SparkSession
from pyspark.sql.functions import col, translate

spark = SparkSession.builder.appName('test').getOrCreate()

df = spark.read.option('header', 'True').option('inferSchema', 'True').csv(r'dataset\googleplaystore.csv')

# df.show()
# print(df.columns)
# print(df.printSchema())

# Drop columns 'Content Rating', 'Android Ver' 'Last Updated', 'Current Ver'
df = df.drop('Content Rating', 'Android Ver', 'Last Updated', 'Current Ver')

# Changing the datatype of the column
df.show(1)
df = df.withColumn('Rating', col('Rating').cast('float'))\
    .withColumn('Reviews', col('Reviews').cast('int'))\
    .withColumn('Price', col('Price').cast('int'))\
    .withColumn('Size', col('Size').cast('int'))\

# print(df.printSchema())
# df.show()

# Creating it to temp_view
df.createOrReplaceTempView('appdata')

# Applying SQL on appdata

# 1. Selecting top 10 Apps
spark.sql(
    "Select App from appdata order by Installs desc limit 10"
).show()