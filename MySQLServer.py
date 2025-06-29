#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error
import os
import sys

def create_database():
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',            # 🔁 Replace with your MySQL username
            password='your_password'  # 🔁 Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        # Clean up and close resources
        if 'cursor' in locals():
            cursor.close()
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
    
