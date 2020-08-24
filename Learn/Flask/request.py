from flask import Flask,url_for,render_template,request

app = Flask(__name__)

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            return "Admin Login Successful"
        else:
            return "Login Failure"
    
    title = request.args.get('title', 'Default')
    return render_template('login.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)