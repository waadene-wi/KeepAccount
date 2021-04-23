import Account
import Category
import Record
import Statistic
import Budget
import Currency
import Common
import json
import logging
import sqlite3
import os

path = os.path.abspath(__file__)
dirname, useless = os.path.split(path)
ROOT_DIR = dirname + '/'
DB_FILE_NAME = ROOT_DIR + 'ka.db'
BACKUP_FILE_NAME = ROOT_DIR + 'commit.backup'

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logger = logging.getLogger('ReloadAllData')

service_list = {}
service_list['account'] = Account.Account(logger)
service_list['category'] = Category.Category(logger)
service_list['record'] = Record.Record(logger)
service_list['statistic'] = Statistic.Statistic(logger)
service_list['budget'] = Budget.Budget(logger)
service_list['currency'] = Currency.Currency(logger)

# 删除数据库文件
os.remove(DB_FILE_NAME)

# 读取创建数据库SQL文件内容
f = open(ROOT_DIR + 'sql/create.sql')
create_sql_content = f.read()
f.close()
f = open(ROOT_DIR + 'sql/add_basic_data.sql')
add_basic_data_sql_content = f.read()
f.close()

# 重新创建数据库
connect = sqlite3.connect(DB_FILE_NAME)
connect.executescript(create_sql_content)
connect.executescript(add_basic_data_sql_content)
connect.commit()
connect.close()

# 读取backup文件恢复数据
f = open(BACKUP_FILE_NAME)
while True:
    line = f.readline()
    if line == '':
        break
    index = 0
    first_BS = line.find(' ', 0)
    service_name = line[0:first_BS]
    second_BS = line.find(' ', first_BS + 1)
    interfance_name = line[first_BS + 1 : second_BS]
    args = json.loads(line[second_BS + 1:-1])
    ret = getattr(service_list[service_name], interfance_name)(args)
    if ret['errno'] != Common.Error.SUCCESS:
        raise ValueError('execute failed! line: ' + line)
f.close()

