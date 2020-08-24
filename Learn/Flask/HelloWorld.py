from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def index():
    return 'Hello World'

if __name__ == '__main__':
    # app.debug = True #调试模式
    # 默认值：host="localhost", port=5000, debug=False
    app.run()