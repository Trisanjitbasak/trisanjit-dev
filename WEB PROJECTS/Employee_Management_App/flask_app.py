# Import necessary libraries
import pandas as pd
import mysql.connector
from flask import Flask, render_template, request

# Clear the console
# os.system('cls')

# Establish a connection to the MySQL server
app = Flask(__name__)
app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''
app.config['MYSQL_PORT'] = ''
"""
conn = mysql.connector.connect(
    host = app.config['MYSQL_HOST'],
    user = app.config['MYSQL_USER'],
    passwd = app.config['MYSQL_PASSWORD'],
    database = app.config['MYSQL_DB'],
    port = app.config['MYSQL_PORT'],
)
"""

cursor = conn.cursor()

# Try to use the existing database, if it doesn't exist then create a new one
try:
    cursor.execute("use Company_Database_app;")
except:
    cursor.execute("create database Company_Database_app")

# Print the options for the user
@app.route('/')
def index():
    return render_template('index.html')

# Get the user's choice
@app.route('/choose', methods=['POST'])
def choose():
    a = int(request.form['choice'])
    if a == 1:
        return render_template('employees.html')
    elif a == 2:
        return render_template('branch.html')
    else:
        return render_template('index.html')

# Employee Table
@app.route('/employee_table')
def employee_table():
    cursor.execute("select * from employee;")
    data = cursor.fetchall()
    table = pd.DataFrame(data, columns=['first_name', 'last_name', 'email_id', 'phone_number', 'Address', 'Company', 'salary'])
    table_html = table.to_html(index=False)
    return table_html

@app.route('/add_employee', methods=['POST'])
def add_employee():
    # Get the details of the new employee from the user
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    phno = request.form['phno']
    add = request.form['add']
    comp = request.form['comp']
    sal = int(request.form['sal'])
    # Insert the new employee into the database
    try:
        cursor.execute("""INSERT INTO EMPLOYEE VALUES(%s, %s, %s, %s, %s, %s, %s)""",(fname, lname, email, phno, add, comp, sal))
        conn.commit()
    except:
        return "Invalid input"    
    return render_template('employees.html')

@app.route('/remove_employee', methods=['POST'])
def remove_employee():
    fname1 = request.form['fname']
    # Remove the employee from the database
    cursor.execute("""DELETE FROM employee WHERE first_name=%s""",(fname1,))
    conn.commit()
    return render_template('employees.html')

@app.route('/create_employee_table', methods=['POST'])
def create_employee_table():
    try:
        # Try to create the employee table
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
    except:
        return "table already exists"
    return "Employee table created successfully"

# Branch Table
@app.route('/branch_table')
def branch_table():
    cursor.execute("select * from branch")
    data = cursor.fetchall()
    table = pd.DataFrame(data, columns=['bcode', 'district', 'city', 'state'])
    return render_template('branch_table.html', table=table.to_html(index=False))

@app.route('/add_branch', methods=['POST']) 
def add_branch():
    bcode=0
    cursor.execute("""INSERT INTO BRANCH VALUES(%s, %s, %s, %s)""",(bcode, district, city, state))
    conn.commit()
    return "Branch added successfully"

@app.route('/remove_branch', methods=['POST']) 
def remove_branch(): 
    bcode1 = int(request.form['bcode'])
    cursor.execute("""DELETE FROM branch WHERE branch_code=%s""",(bcode1,)) 
    conn.commit() 
    return "Branch removed successfully"

@app.route('/create_branch_table', methods=['POST']) 
def create_branch_table(): 
    try:
        cursor.execute("""CREATE TABLE branch( 
                       branch_code INT, 
                       district VARCHAR(1000), 
                       city VARCHAR(1000), 
                       state VARCHAR(1000) 
                       );""") 
        conn.commit(); 
    except: 
        return "table already exists" 
        return "Branch table created successfully"      
if __name__ == '__main__':
    app.run(debug=True)
cursor.close() 
conn.close()  
