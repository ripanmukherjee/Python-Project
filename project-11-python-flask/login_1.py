from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return 'hello world'
    return render_template('login_1.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
