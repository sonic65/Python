from flask import *
app= Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello Flask"

@app.route('/hi')
def hi():
    return  "hi Python"

# redirect
@app.route('/user/<name>')
def sayHello(name):
    if name == 'baidu':
        return redirect('http://www.baidu.com')
    elif name == 'NO':
        return abort(404)
        
    return '<h1> Hello,%s </h1>' % name


if __name__ == "__main__":
    app.run()

'''
export FLASK_APP=start.py
flask run

Running on http://127.0.0.1:5000/
'''