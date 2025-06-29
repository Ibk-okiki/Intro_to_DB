#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',             # 🔁 Change to your MySQL username
            password='your_password' # 🔁 Change to your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database (IF NOT EXISTS avoids failure if already exists)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as err:
        # Handle connection or execution errors
        print(f"Error while connecting to MySQL: {err}")

    finally:
        # Properly close resources
        if 'cursor' in locals():
            cursor.close()
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
    
