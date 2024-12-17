import csv
import json
from pymongo import MongoClient

# Establish a connection to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# Load the CSV file
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]

# Convert the data to JSON format
json_data = json.dumps(data)

# Insert the data into the MongoDB collection
collection.insert_many(json.loads(json_data))

# Close the MongoDB client
client.close()