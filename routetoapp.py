@app.route('/signup')
def show_signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    # Retrieve form data
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    # Insert into database (ensure to handle SQL injection)
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
    db.commit()
    return redirect(url_for('index'))