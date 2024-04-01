<<<<<<< HEAD
#####Amin-Farnoosh
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

###connecting the app to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ashkan@1234",
    database="srt"
)
#####routing
@app.route('/')
def index():
    return "Hello, World!"
=======
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'seneca'

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Ashkan@123456',
    'database': 'srt'
}

def get_user_id_by_username(username):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] if result else None

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('signup'))
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        hashed_password = generate_password_hash(request.form['password'])
        
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
            (username, email, hashed_password)
        )
        conn.commit()
        cursor.close()
        conn.close()

        session['user_id'] = cursor.lastrowid
        
        flash('User successfully signed up!', 'success')
        return redirect(url_for('index'))
    return render_template('signup.html')

@app.route('/car_maintenance', methods=['GET', 'POST'])
def car_maintenance():
    if 'user_id' not in session:
        return redirect(url_for('signup'))

    if request.method == 'POST':
        username = request.form['username']
        user_id = get_user_id_by_username(username)
        if user_id is None:
            flash('User does not exist!', 'error')
            return redirect(url_for('car_maintenance'))

        cost = request.form['cost']
        description = request.form['description']
        date = request.form['date']
        
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO car_maintenance (user_id, cost, description, date) VALUES (%s, %s, %s, %s)",
            (user_id, cost, description, date)
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash('Information successfully updated!', 'success')
        return redirect(url_for('index'))
    return render_template('car_maintenance.html')

@app.route('/drinks', methods=['GET', 'POST'])
def drinks():
    if 'user_id' not in session:
        return redirect(url_for('signup'))

    if request.method == 'POST':
        username = request.form['username']
        user_id = get_user_id_by_username(username)
        if user_id is None:
            flash('User does not exist!', 'error')
            return redirect(url_for('drinks'))

        cost = request.form['cost']
        type = request.form['type']
        date = request.form['date']
        
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO drinks (user_id, cost, type, date) VALUES (%s, %s, %s, %s)",
            (user_id, cost, type, date)
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash('Information successfully updated!', 'success')
        return redirect(url_for('index'))
    return render_template('drinks.html')

@app.route('/other_costs', methods=['GET', 'POST'])
def other_costs():
    if 'user_id' not in session:
        return redirect(url_for('signup'))

    if request.method == 'POST':
        username = request.form['username']
        user_id = get_user_id_by_username(username)
        if user_id is None:
            flash('User does not exist!', 'error')
            return redirect(url_for('other_costs'))

        cost = request.form['cost']
        description = request.form['description']
        date = request.form['date']
        
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO other_costs (user_id, cost, description, date) VALUES (%s, %s, %s, %s)",
            (user_id, cost, description, date)
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash('Information successfully updated!', 'success')
        return redirect(url_for('index'))
    return render_template('other_costs.html')

@app.route('/results')
def results():
    if 'user_id' not in session:
        return redirect(url_for('signup'))
        
    user_id = session['user_id']
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    user_data = cursor.fetchall()

    cursor.execute("SELECT * FROM car_maintenance WHERE user_id = %s", (user_id,))
    maintenance_data = cursor.fetchall()

    cursor.execute("SELECT * FROM drinks WHERE user_id = %s", (user_id,))
    drinks_data = cursor.fetchall()

    cursor.execute("SELECT * FROM other_costs WHERE user_id = %s", (user_id,))
    other_costs_data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('results.html', user_data=user_data, maintenance_data=maintenance_data, drinks_data=drinks_data, other_costs_data=other_costs_data)
>>>>>>> cf4336d (update2)

if __name__ == '__main__':
    app.run(debug=True)
