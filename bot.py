from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb+srv://abdulrahaman001:databaseKomi@komi.mosqcfj.mongodb.net/?retryWrites=true&w=majority&appName=KOmi" #pdate with your connection string if necessary

# Specify the database name
db_name = "KOmi"  # Replace with your database name
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
