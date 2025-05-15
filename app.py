from flask import Flask, render_template, redirect, request, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'noe_sikkert_her'


# Funkjson for å koble til databasen
def get_db_connection():
    return mysql.connector.connect(
        user="adriatikveseli",
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
    username = request.form['username']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if username exists first
    cursor.execute("SELECT * FROM test WHERE username=%s", (username,))
    user = cursor.fetchone()

    if not user:
        cursor.close()
        conn.close()
        return "Brukeren finnes ikke. <a href='/createacc'>Opprett en konto først</a>"

    # Check if password is correct
    cursor.execute("SELECT * FROM test WHERE username=%s AND password=%s", (username, password))
    valid_user = cursor.fetchone()
    cursor.close()
    conn.close()

    if valid_user:
        session['username'] = username
        return redirect(url_for('timeliste'))
    else:
        return "Feil passord. <a href='/'>Prøv igjen</a>"


    
    
@app.route('/createacc', methods=['GET', 'POST'])
def createacc():
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
            session['username'] = username
            return redirect(url_for('timeliste'))
        except mysql.connector.errors.IntegrityError:
            return "Brukernavn finnes allerede. <a href='/createacc'>Prøv igjen</a>"
    return render_template('createacc.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


    
@app.route('/registrer_timer', methods=['POST'])
def registrer_timer():
    prosjekt = request.form['prosjekt']
    arbeidsleder = request.form['arbeidsleder']
    prosent = request.form['prosent']
    timer = request.form['timer']
    type_timer = request.form['type_timer']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO timelister (prosjekt, arbeidsleder, prosent, timer, type_timer)
        VALUES (%s, %s, %s, %s, %s)
    """, (prosjekt, arbeidsleder, prosent, timer, type_timer))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('timeliste', registrert='true'))




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
