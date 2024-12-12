from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("Data Processing").getOrCreate()

# Load the dataset into a DataFrame
df = spark.read.csv("path/to/data.csv", header=True, inferSchema=True)

# Display the schema of the DataFrame
print(df.schema)

# Calculate the total count of records
total_count = df.count()
print("Total Records:", total_count)

# Calculate the average value of a column (e.g., "column_name")
avg_value = df.select("column_name").agg({"column_name": "avg"}).collect()[0][0]
print("Average Value:", avg_value)

# Generate a report by grouping the data by a column (e.g., "category")
report = df.groupBy("category").count().collect()
for row in report:
    print(f"Category: {row['category']}, Count: {row['count']}")

# Save the report to a CSV file
df.groupBy("category").count().write.csv("report.csv", header=True)

# Stop the SparkSession
spark.stop()