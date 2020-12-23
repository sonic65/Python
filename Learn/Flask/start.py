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
    # app.debug = True #调试模式
    # 默认值：host="localhost", port=5000, debug=False

'''

export FLASK_APP=start.py
flask run

'''