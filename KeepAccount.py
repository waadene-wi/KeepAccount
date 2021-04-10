import flask
import json
from Account import *
from Category import *
from Record import *
from Statistic import *
from Budget import *

app = flask.Flask(__name__)
app.debug = True

def executeService(typeOfClass, method_name):
    instance = typeOfClass()
    if hasattr(instance, method_name) == False:
        return json.dumps(makeReturn(Error.ILLEGAL_URL))
    args = flask.request.args.to_dict()
    ret = getattr(instance, method_name)(args)
    return json.dumps(ret)


@app.route('/')
def default_index():
    return flask.send_file('web/add_record.html')
    
@app.route('/test')
def test():
    return 'Hello, World!'

@app.route('/static/<file_name>')
def default_page(file_name):
    return flask.send_file('web/' + file_name)

@app.route('/account/<method_name>')
def account_service(method_name):
    return executeService(Account, method_name)

@app.route('/category/<method_name>')
def category_service(method_name):
    return executeService(Category, method_name)

@app.route('/record/<method_name>')
def record_service(method_name):
    return executeService(Record, method_name)

@app.route('/statistic/<method_name>')
def statistic_service(method_name):
    return executeService(Statistic, method_name)

@app.route('/budget/<method_name>')
def budget_service(method_name):
    return executeService(Budget, method_name)

if __name__ == '__main__':
    app.run()