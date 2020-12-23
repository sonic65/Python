#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from flask import *
app= Flask(__name__)
from ibot_token import ibot


@app.route('/')
def hello_world():
    return "Hello Flask"

@app.route('/ibot')
def post_invoke():
    s = ibot.ibot_request()
    return s 

if __name__ == "__main__":
    app.run(debug=True)

'''
Running on http://127.0.0.1:5000/
'''