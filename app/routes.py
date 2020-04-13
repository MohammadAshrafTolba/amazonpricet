from app.init_app import app
from flask import render_template, request

@app.route('/')
@app.route('/index')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    uEmail = request.form['uEmail']
    pURL = request.form['pURL']
    print(uEmail, pURL)
    return uEmail, pURL