from flask import Flask
app= Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello Flask"

@app.route('/hi')
def hi():
    return  "hi Python"

if __name__ == "__main__":
    app.run(debug=True, threaded=True, port=5000, host='0.0.0.0')


'''
export FLASK_APP=start.py
flask run

'''