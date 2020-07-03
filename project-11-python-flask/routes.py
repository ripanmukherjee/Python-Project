from app import app
from flask import render_template, redirect, url_for
import forms
from subprocess import check_output


@app.route('/')
@app.route('/index')
def index():
    check_output(["zenity", "--info", "--width=400", "--height=200", "--text=ALERT!!!\n\nLast Name cannot"])
    return render_template('/index.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print('submitted', form.title.data)
        #return redirect(url_for('index'))
    return render_template('/about.html', form=form)
