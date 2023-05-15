import os

from flask import (
    Flask, render_template, request, flash,
    redirect, url_for, send_from_directory,
    make_response
)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(12)

@app.route("/")
def index():

    return render_template('base.html')


if __name__ == "__main__":
    app.run()
