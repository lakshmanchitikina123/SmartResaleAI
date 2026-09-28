import sqlite3


DATABASE_NAME = "database.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def create_tables():

    connection = get_connection()
    cursor = connection.cursor()

    # ==========================================
    # PRODUCTS TABLE
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT NOT NULL,

            category TEXT NOT NULL,

            brand TEXT,

            condition TEXT NOT NULL,

            description TEXT,

            location TEXT NOT NULL,

            price REAL NOT NULL,

            predicted_price REAL,

            seller_name TEXT,

            seller_contact TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)


    # ==========================================
    # ENQUIRIES TABLE
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS enquiries (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            product_id INTEGER NOT NULL,

            buyer_name TEXT NOT NULL,

            buyer_contact TEXT NOT NULL,

            message TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (product_id)
            REFERENCES products(id)

        )
    """)


    connection.commit()
    connection.close()


if __name__ == "__main__":

    create_tables()

    print("Database created successfully!")
    print("Tables created:")
    print("1. products")
    print("2. enquiries")