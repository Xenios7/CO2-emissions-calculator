import psycopg2

try:
    # Connect to your PostgreSQL database
    connection = psycopg2.connect(
        dbname="carbon_footprint",
        user="xenios",
        password="xenios99251488",
        host="localhost",
        port="5432"
    )
    print("✅ Connection successful!")

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"PostgreSQL version: {db_version[0]}")

except Exception as error:
    print(f"❌ Error: {error}")

finally:
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print("🔌 Connection closed.")
