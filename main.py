'''routes for shed log'''

import os
from flask import Flask, render_template, request
from xcsv import cxs
from crud import Crud

DATABASE = 'sheds.db'
SECRET_KEY = os.urandom(12)
X_LIST = cxs('exes.csv')

app = Flask(__name__)
app.config.from_object(__name__)
db = Crud(app.config['DATABASE'])


@app.route("/", methods=['GET', 'POST'])
def home():
    '''handle main hud'''
    if request.method == 'GET':
        c = 0
    if request.method == 'POST':
        a = request.form['ctl']
        c = int(request.form['current_x'])
        if a == 'prev':
            c = (c - 1) % len(X_LIST)
        if a == 'next':
            c = (c + 1) % len(X_LIST)
    return render_template('home.html', exes=X_LIST, v=c)

@app.route("/logs")
def logs():
    return render_template('logs.html', logs=db.readLogs())

@app.route("/exes")
def exes():
    return render_template('exes.html', exes=X_LIST)

@app.route('/save', methods=['POST'])
def save():
    '''save timelog'''
    db.createLogEntry((
        request.json['text'], request.json['start'], request.json['end']))

    return {'success': True}
