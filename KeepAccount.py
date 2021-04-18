import flask
import json
from Account import *
from Category import *
from Record import *
from Statistic import *
from Budget import *
from Currency import *
from Common import *

app = flask.Flask(__name__)
app.debug = True

def executeService(typeOfClass, method_name):
    instance = typeOfClass(app.logger)
    if hasattr(instance, method_name) == False:
        return json.dumps(makeReturn(Error.ILLEGAL_URL))
    args = flask.request.args.to_dict()
    ret = getattr(instance, method_name)(args)
    return json.dumps(ret)


@app.route('/')
def default_index():
    return flask.send_file('web/add_record.html')

@app.route('/favicon.ico')
def favicon():
    return flask.send_file('web/favicon.ico')

@app.route('/test')
def test():
    return 'Hello, World!'

@app.route('/<page_name>')
def get_page(page_name):
    # 文件不存在时需要做处理
    return flask.send_file('web/' + page_name + '.html')

@app.route('/res/<file_name>')
def get_resource(file_name):
    return flask.send_file('web/' + file_name)

@app.route('/service/account/<method_name>')
def account_service(method_name):
    return executeService(Account, method_name)

@app.route('/service/category/<method_name>')
def category_service(method_name):
    return executeService(Category, method_name)

@app.route('/service/record/<method_name>')
def record_service(method_name):
    return executeService(Record, method_name)

@app.route('/service/statistic/<method_name>')
def statistic_service(method_name):
    return executeService(Statistic, method_name)

@app.route('/service/budget/<method_name>')
def budget_service(method_name):
    return executeService(Budget, method_name)

@app.route('/service/currency/<method_name>')
def currency_service(method_name):
    return executeService(Currency, method_name)

if __name__ == '__main__':
    app.run()