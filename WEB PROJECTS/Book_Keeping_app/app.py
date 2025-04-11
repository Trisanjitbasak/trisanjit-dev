from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'book_keeping'
mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        company_name = request.form['company_name']
        journal_text = request.form['journal_text']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO journal_entries (company_name, journal_text) VALUES (%s, %s)", (company_name, journal_text))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))  # Redirect to avoid form resubmission on refresh
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM journal_entries ORDER BY id DESC")  # Show latest entries first
    entries = cur.fetchall()
    cur.close()
    
    return render_template('index.html', entries=entries)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_entry(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM journal_entries WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
