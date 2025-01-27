import psycopg2

# Replace with your CockroachDB connection string
DATABASE_URL = "postgresql://ghost:sQ1ZMBNvaoAv9H92ViPpOA@thorn-octopus-5107.j77.aws-us-east-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&sslrootcert=/home/ubuntu/.postgresql/root.crt"

cursor = None  # Ensure cursor is defined before the try block
connection = None

try:
    # Connect to the CockroachDB database
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
    print("All tables in the CockroachDB database have been deleted successfully.")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Ensure cursor and connection are closed properly
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print("Database connection closed.")
