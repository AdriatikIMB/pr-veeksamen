from flask import Flask , render_template, redirect, request, url_for 
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
    return render_template('index.html')  # Show the index page

@app.route('/timeliste')
def timeliste():

    
    return render_template('timeliste.html')  # Show the timeliste page

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        phone = request.form['phone']
        

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO test (username, password, phone) VALUES (%s, %s, %s)", (username, password, phone))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('timeliste'))  # Redirect back to timeliste page after form submission

if __name__ == '__main__':
    app.run(debug=True)
