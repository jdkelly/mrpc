from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/linka')
def linka():
    return '<h1>Link A</h1>'


@app.route('/linkb')
def linkb():
    return '<h1>Link B</h1>'


@app.route('/login')
def login():
    return '<h1>Login</h1>'


@app.route('/logout')
def logout():
    return '<h1>Logout</h1>'
