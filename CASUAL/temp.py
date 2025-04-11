import mysql.connector
from flask import Flask, render_template, request

# Clear the console
# os.system('cls')

# Establish a connection to the MySQL server
app = Flask(__name__)
"""
conn = mysql.connector.connect(
    host = "",
    port = "",
    user = "",
    passwd = "",
    database = "",
    auth_plugin="",
)
"""
cursor = conn.cursor(buffered=True)

cursor.execute(""" CREATE TABLE employee(
                        first_name VARCHAR(1000),
                        last_name VARCHAR(1000),
                        email VARCHAR(1000),
                        phone_number VARCHAR(1000),
                        address VARCHAR(1000),
                        company VARCHAR(1000),
                        salary int
                        );""")
conn.commit();
