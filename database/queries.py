import sqlite3

# Connect to the SQLite database (or create if it doesn't exist)
DATABASE_NAME = "carbon_footprint.db"

def create_tables():
    """Create tables if they do not exist."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        transport TEXT,
        distance REAL,
        energy REAL,
        diet TEXT,
        transport_emissions REAL,
        energy_emissions REAL,
        diet_emissions REAL,
        total_emissions REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recommendations (
        category TEXT PRIMARY KEY,
        message TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_emissions(data):
    """Insert emissions data into the database."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO emissions (transport, distance, energy, diet, transport_emissions, energy_emissions, diet_emissions, total_emissions)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, data)

    conn.commit()
    conn.close()

def fetch_recommendations(category):
    """Fetch recommendations based on category."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT message FROM recommendations WHERE category = ?", (category,))
    result = cursor.fetchone()
    
    conn.close()
    return result[0] if result else "No recommendations available."

# Initialize the tables when the module is loaded
create_tables()
