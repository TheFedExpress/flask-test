# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 10:41:35 2018

@author: peter_goodridge
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'The app worked'
    
if __name__ ==  '__main__':
    app.run(host = '0.0.0.0')