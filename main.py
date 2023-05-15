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
def index():
    return render_template('base.html')

@app.route('/save', methods=['POST'])
def save():
    print(request.json)
    db.createLogEntry(
        (request.json['text'],
        request.json['start'],
        request.json['end'])
    )

    return {'success': True}

if __name__ == "__main__":
    app.run()
