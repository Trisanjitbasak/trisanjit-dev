from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin123'
app.config['MYSQL_DB'] = 'coaching'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        student = request.form.get('student')
        if student:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO students (name) VALUES (%s)", [student])
            mysql.connection.commit()
    cur = mysql.connection.cursor()
    cur.execute("SELECT name FROM students")
    students = [row[0] for row in cur.fetchall()]
    return render_template('index.html', students=students)

@app.route('/student/<name>', methods=['GET', 'POST'])
def student(name):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        month = request.form.get('month')
        cur.execute("UPDATE payments SET status = 'Paid' WHERE student = %s AND month = %s", (name, month))
        mysql.connection.commit()
    cur.execute("SELECT month, status FROM payments WHERE student = %s", [name])
    payments = {row[0]: row[1] for row in cur.fetchall()}
    return render_template('student.html', name=name, payments=payments)

if __name__ == '__main__':
    app.run(debug=True)
