#!/usr/bin/env python3
from flask import Flask, render_template
from subprocess import check_output

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'


@app.route('/')
def base():
    return render_template('/base.html')


@app.route('/add')
def add():
    return render_template('/add.html')


@app.route('/search')
def search():
    return render_template('/search.html')


@app.route('/modify')
def modify():
    return render_template('/modify.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)
