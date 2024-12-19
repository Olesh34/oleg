from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('gifts.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    gifts = conn.execute('SELECT * FROM gifts').fetchall()
    conn.close()
    return render_template('index.html', gifts=gifts)

if __name__ == '__main__':
    app.run(debug=True)