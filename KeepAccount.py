from flask import *
from Account import *

app = Flask(__name__)

@app.route('/test')
def test():
    return 'Hello, World!'

@app.route('/')
def default_page():
    return send_file('web/home.html')

@app.route('/account/')
def account():
    acnt = Account()
    ret = acnt.handle()
    return ret