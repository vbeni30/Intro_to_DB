# MySQLServer.py

import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (without specifying database)
        connection = mysql.connector.connect(
            host='localhost',      # replace with your host if different
            user='root',           # replace with your MySQL username
            password='your_password'  # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except mysql.connector.Error as e:   # <-- Specific exception handling
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
