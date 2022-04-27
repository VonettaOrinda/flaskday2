from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    ls=["Massage", "Full body Scrub", "Waxing","Sauna","Pedicure","Manicure","Hair Dressing"]
    return render_template('services.html',names=ls)





