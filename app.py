from flask import Flask, render_template, redirect, request, url_for
import mysql.connector 

app = Flask(__name__) 

# Function to connect to the database
def get_db_connection():
    return mysql.connector.connect(
        user="adriatik",
        password="Adriatik.123",
        database="restaurant",
        host="10.2.4.76",
        port=3306
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user")  
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', user=users)  


@app.route('/userlist')
def userlist():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user")  
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('userlist.html', users=users)




@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    conn = get_db_connection()
    cursor = conn.cursor()
        
    cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password))  
    conn.commit()
    
    cursor.close()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
