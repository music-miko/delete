import psycopg2

# Replace with your ElephantSQL connection string
DATABASE_URL = "postgres://dkpooiwa:m5zv9E9zxlWmqSmV4JpvTAq8AwGgfXA3@manny.db.elephantsql.com/dkpooiwa"

try:
    # Connect to the ElephantSQL database
    connection = psycopg2.connect(DATABASE_URL)
    cursor = connection.cursor()

    # Query to retrieve all table names from the 'public' schema
    cursor.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public';
    """)
    tables = cursor.fetchall()

    # Drop all tables
    for table in tables:
        table_name = table[0]
        cursor.execute(f"DROP TABLE IF EXISTS {table_name} CASCADE;")
        print(f"Table '{table_name}' has been deleted.")

    # Commit the changes
    connection.commit()
    print("All tables in the database have been deleted successfully.")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print("Database connection closed.")
