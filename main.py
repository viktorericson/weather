import requests
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



@app.route('/', methods=['POST','GET'])
def home():
    url =  "http://api.weatherapi.com/v1/forecast.json?key=83231fabfb3e4682933162709222002&q={}&days=1&aqi=no&alerts=no"
    city = request.form.get("city")

    r= requests.get(url.format(city)).json()

    weather1={
        "city":city,
        "temperature": r["current"]["temp_c"],
        "icon": r["current"]["condition"]["icon"]
    }
    weather=[weather1]
    return render_template('base.html',weather=weather)

if __name__ == "__main__":
    app.run()