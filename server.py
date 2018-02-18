#!/usr/bin/python3


from flask import Flask
from logging import Logger
from flask import Request

from common import config
from common import logic


app = Flask(__name__)
@app.route('/',method=['GET'])
def top():
    return 'Hellow, World'

@app.route('/omikuzi',method=['POST'])
def draw():
    return 'Hellow, World'

if __name__ == '__main__':
    app.run()

