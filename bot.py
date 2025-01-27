from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb+srv://karan69:karan69@cluster0.gfw7e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Update with your connection string if needed

# Specify the database and collection name
db_name = "cluster0"  # Replace with your database name
collection_name = "Curse"  # Replace with your collection name

# Access the database and collection
db = client[db_name]
collection = db[collection_name]

# Delete all documents in the collection
result = collection.delete_many({})

print(f"Deleted {result.deleted_count} documents from the collection '{collection_name}'.")
