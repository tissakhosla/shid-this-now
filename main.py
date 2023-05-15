import os
import sqlite3
import time
from flask import Flask, render_template, request, g
from crud import Crud

DATABASE = 'sheds.db'
SECRET_KEY = os.urandom(12)

app = Flask(__name__)
app.config.from_object(__name__)
db = Crud(app.config['DATABASE'])

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/logs")
def logs():
    return render_template('logs.html', logs=db.readLogs())

@app.route("/exes")
def exes():
    return render_template('exes.html')

@app.route('/save', methods=['POST'])
def save():
    db.createLogEntry(
        (request.json['text'],
        request.json['start'],
        request.json['end'])
    )

    return {'success': True}

if __name__ == "__main__":
    app.run()
