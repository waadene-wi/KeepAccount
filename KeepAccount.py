import flask
import json
import copy
from Account import *
from Category import *
from Record import *
from Statistic import *
from Budget import *
from Currency import *
from Common import *
from URLBackup import *

app = flask.Flask(__name__)
app.debug = True
url_backup = URLBackup()

def executeService(typeOfClass, service_name, method_name):
    instance = typeOfClass(app.logger)
    if hasattr(instance, method_name) == False:
        return json.dumps(makeReturn(Error.ILLEGAL_URL))
    args = flask.request.args.to_dict()
    ori_args = copy.deepcopy(args)
    ret = getattr(instance, method_name)(args)
    url_backup.backup(service_name, method_name, ori_args)
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
    return executeService(Account, 'account', method_name)

@app.route('/service/category/<method_name>')
def category_service(method_name):
    return executeService(Category, 'category', method_name)

@app.route('/service/record/<method_name>')
def record_service(method_name):
    return executeService(Record, 'record', method_name)

@app.route('/service/statistic/<method_name>')
def statistic_service(method_name):
    return executeService(Statistic, 'statistic', method_name)

@app.route('/service/budget/<method_name>')
def budget_service(method_name):
    return executeService(Budget, 'budget', method_name)

@app.route('/service/currency/<method_name>')
def currency_service(method_name):
    return executeService(Currency, 'currency', method_name)

if __name__ == '__main__':
    app.run()