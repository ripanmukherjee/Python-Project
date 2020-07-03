#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'

from routes import *


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)
