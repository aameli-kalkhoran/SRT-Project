#####Amin-Farnoosh
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

###connecting the app to the database
db = mysql.connector.connect(
    host="localhost",
    user="aameli",
    password="P@ssw0rd1234",
    database="srtproject"
)
#####routing
@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
