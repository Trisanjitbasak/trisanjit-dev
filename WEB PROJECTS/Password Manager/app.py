from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="password",
    port = "3306"
)

# Create cursor object
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    password = request.form['password']
    # Authenticate the password
    if password == 'admin123':
        return redirect(url_for('dashboard'))
    else:
        return "Incorrect password. Please try again."

@app.route('/dashboard')
def dashboard():
    # Fetch passwords from the database
    cursor.execute("SELECT * FROM passwords")
    passwords = cursor.fetchall()
    return render_template('dashboard.html', passwords=passwords)

@app.route('/add_password', methods=['POST'])
def add_password():
    new_website = request.form['new_website']
    new_password = request.form['new_password']
    # Insert new password into the database
    sql = "INSERT INTO passwords (website, password) VALUES (%s, %s)"
    val = (new_website, new_password)
    cursor.execute(sql, val)
    db.commit()
    return redirect(url_for('dashboard'))

@app.route('/edit_password/<int:id>', methods=['GET', 'POST'])
def edit_password(id):
    if request.method == 'POST':
        new_website = request.form['new_website']
        new_password = request.form['new_password']
        # Update the password entry
        sql = "UPDATE passwords SET website = %s, password = %s WHERE id = %s"
        val = (new_website, new_password, id)
        cursor.execute(sql, val)
        db.commit()
        return redirect(url_for('dashboard'))
    else:
        return render_template('edit_password.html')

@app.route('/remove_password/<int:id>', methods=['POST'])
def remove_password(id):
    # Remove password from the database
    sql = "DELETE FROM passwords WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    db.commit()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
