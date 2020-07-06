from flask import Flask
app= Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello Flask"

@app.route('/hi')
def hi():
    return  "hi Python"



'''
export FLASK_APP=start.py
flask run

'''