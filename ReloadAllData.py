import json
import Account
import Category
import Record
import Statistic
import Budget
import Currency
import Common
import logging

BACKUP_FILE_NAME = 'commit.backup'
logger = None ################
service_list = {}
service_list['account'] = Account.Account(logger)
service_list['category'] = Category.Category(logger)
service_list['record'] = Record.Record(logger)
service_list['statistic'] = Statistic.Statistic(logger)
service_list['budget'] = Budget.Budget(logger)
service_list['currency'] = Currency.Currency(logger)

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