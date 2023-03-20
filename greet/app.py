from flask import Flask
app = Flask(__name__)


@app.route('/welcome')
def welcome_page():
    return '''
    <h1>Welcome</h1>
    <a href='/welcome' label='welcome'>welcome</a>
    <a href='/welcome/home' label='home'>home</a>
    <a href='/welcome/back' label='back'>back</a>
    '''

@app.route('/welcome/home')
def welcomehome_page():
    return '''
    <h1>Welcome Home</h1>
    <a href='/welcome' label='welcome'>welcome</a>
    <a href='/welcome/home' label='home'>home</a>
    <a href='/welcome/back' label='back'>back</a>
    '''

@app.route('/welcome/back')
def welcomeback_page():
    return '''
    <h1>Welcome Back</h1>
    <a href='/welcome' label='welcome'>welcome</a>
    <a href='/welcome/home' label='home'>home</a>
    <a href='/welcome/back' label='back'>back</a>
    '''