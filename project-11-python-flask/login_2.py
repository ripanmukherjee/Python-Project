from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from subprocess import check_output

app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login_2.html')
    else:
        return "Hello Boss!"


@app.route('/login_2', methods=['POST'])
def do_admin_login_2():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        session['logged_in'] = False
        flash('wrong password!')
        check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nLast Name cannot "
                                                                          "be blank or less than 2 characters. \n"
                                                                          "Please try again!!!!"])

    return home()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
