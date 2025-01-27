from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb+srv://karan69:karan69@cluster0.gfw7e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Update with your connection string if necessary

# Specify the database name
db_name = "Cluster0"  # Replace with your database name
db = client[db_name]

# List all collections in the database
collections = db.list_collection_names()

# Loop through each collection and drop it
for collection_name in collections:
    db[collection_name].drop()
    print(f"Collection '{collection_name}' has been deleted.")

# Confirm the operation
if not db.list_collection_names():
    print(f"All collections in the database '{db_name}' have been deleted.")
else:
    print(f"Some collections could not be deleted.")

# Close the connection
client.close()
