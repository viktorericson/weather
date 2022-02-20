import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')


Hej
hasattr


if __name__ == "__main__":
    app.run()