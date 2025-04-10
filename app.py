from flask import Flask , render_template, redirect, request, url_for
import mysql.connector

app = Flask(__name__)

# Funkjson for å koble til databasen
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
    return render_template('index.html') 


@app.route('/timeliste')
def timeliste():
    return render_template('timeliste.html') 

@app.route('/ansatt_timeliste')
def ansatt_timeliste():

    return render_template('ansatt_timeliste.html')  


@app.route('/submit', methods=['POST'])
def submit():
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        phone = request.form['phone']
        
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO test (username, password, phone) VALUES (%s, %s, %s)", (username, password, phone))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('timeliste')) 
    except mysql.connector.errors.IntegrityError:
        print("Brukernavn finnes allerede. Vennligst velg et annet.")
        return redirect(url_for('timeliste'))




if __name__ == '__main__':
    app.run(debug=True)
