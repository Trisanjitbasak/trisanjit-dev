# Import necessary libraries
import pandas as pd
import mysql.connector
from flask import Flask, render_template, request

# Clear the console
# os.system('cls')

# Establish a connection to the MySQL server
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
conn = mysql.connector.connect(
    host = app.config['MYSQL_HOST'],
    user = app.config['MYSQL_USER'],
    passwd = app.config['MYSQL_PASSWORD'],
    auth_plugin='mysql_native_password'
)
cursor = conn.cursor()

# Try to use the existing database, if it doesn't exist then create a new one
try:
    cursor.execute("use Company_database_app;")
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

@app.route('/employees')
def employees():
    cursor.execute("SELECT * FROM employee")
    data = cursor.fetchall()
    return render_template('employees.html', data=data)

@app.route('/add_employee', methods=['POST'])
def add_employee():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    phno = request.form['phno']
    add = request.form['add']
    comp = request.form['comp']
    sal = int(request.form['sal'])

    try:
        cursor.execute("INSERT INTO EMPLOYEE VALUES(%s, %s, %s, %s, %s, %s, %s)", (fname, lname, email, phno, add, comp, sal))
        conn.commit()
    except:
        return "Invalid input"

    return render_template('employees.html')

@app.route('/remove_employee', methods=['POST'])
def remove_employee():
    fname1 = request.form['fname']
    cursor.execute("DELETE FROM employee WHERE first_name=%s", (fname1,))
    conn.commit()
    return render_template('employees.html')

@app.route('/create_employee_table', methods=['POST'])
def create_employee_table():
    try:
        cursor.execute("""
                       CREATE TABLE employee(
                           first_name VARCHAR(1000),
                           last_name VARCHAR(1000),
                           email VARCHAR(1000),
                           phone_number VARCHAR(1000),
                           address VARCHAR(1000),
                           company VARCHAR(1000),
                           salary INT
                       );
                       """)
        conn.commit()
    except:
        return "table already exists"

    return "Employee table created successfully"

# Branch Table
@app.route('/branch_table')
def branch_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS branch( 
                       branch_code INT, 
                       district VARCHAR(1000), 
                       city VARCHAR(1000), 
                       state VARCHAR(1000) 
                       );""") 
    conn.commit(); 
    cursor.execute("select * from branch")
    data = cursor.fetchall()
    table = pd.DataFrame(data, columns=['bcode', 'district', 'city', 'state'])
    return render_template('branch.html', table=table.to_html(index=False))

@app.route('/add_branch', methods=['POST']) 
def add_branch():
    bcode = request.form['bcode']
    district = request.form['district']
    city = request.form['city']
    state = request.form['state']
    bcode=0
    cursor.execute("""INSERT INTO BRANCH VALUES(%s, %s, %s, %s)""",(bcode, district, city, state))
    conn.commit()
    return render_template('branch.html')

@app.route('/remove_branch', methods=['POST']) 
def remove_branch(): 
    bcode1 = int(request.form['bcode'])
    cursor.execute("""DELETE FROM branch WHERE branch_code=%s""",(bcode1,)) 
    conn.commit() 
    return "Branch removed successfully"
   
if __name__ == '__main__':
    app.run(debug=True)
cursor.close() 
conn.close()  
