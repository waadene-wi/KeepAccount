import sqlite3
from Common import *

DB_NAME = 'ka.db'

class DB:
    def __init__(self, logger):
        self.connection = None
        self.cursor = None
        self.logger = logger

    def call(self, method, args):
        # 判斷方法是否存在
        if hasattr(self, method) == False:
            self.logger.warning('method not exist: ' + method)
            return makeReturn(Error.METHOD_NOT_EXIST)
        # 連接數據庫
        try:
            self.connection = sqlite3.connect(DB_NAME)
            self.cursor = self.connection.cursor()
        except:
            self.logger.warning('db connect failed.')
            return makeReturn(Error.DATABASE_ERROR)
        # 執行
        ret = getattr(self, method)(args)
        if ret['errno'] != Error.SUCCESS:
            return ret
        # 關閉數據庫連接
        self.connection.close()
        return ret

    def executeTransaction(self, sqls):
        try:
            self.cursor.execute('BEGIN TRANSACTION')
            for sql in sqls:
                self.cursor.execute(sql)
            self.cursor.execute('COMMIT')
        except Exception as err:
            self.cursor.execute('ROLLBACK')
            self.logger.warning(err)
            self.logger.warning('transaction execute failed. sqls:' + str(sqls))
            return makeReturn(Error.DATABASE_ERROR)
        self.connection.commit()
        return makeReturn(Error.SUCCESS)

    def __selectData(self, attrs, tableName, condition, returnRaw):
        try:
            # 拼SQL语句
            if len(attrs) == 0:
                raise ValueError('attrs is empty!')
            sqlStr = 'SELECT '
            for attr in attrs:
                sqlStr += attr + ', '
            sqlStr = sqlStr[:-2] + ' FROM ' + tableName
            if condition != '':
                sqlStr += ' WHERE ' + condition
            self.logger.warning(sqlStr)
            # 执行SQL语句，并获取结果
            connection = sqlite3.connect(DB_NAME)
            cursor = connection.cursor()
            cursor.execute(sqlStr)
            dbData = cursor.fetchall()
        except:
            self.logger.warning('select failed. sql: ' + sqlStr)
            return makeReturn(Error.DATABASE_ERROR)
        cursor.close()
        connection.close()
        if returnRaw == True:
            return makeReturn(Error.SUCCESS, dbData)
        # 把属性名字加入数据库返回的数据中
        ret = []
        for row in dbData:
            rowMap = {}
            for i in range(0, len(attrs)):
                rowMap[attrs[i]] = row[i]
            ret.append(rowMap)
        return makeReturn(Error.SUCCESS, ret)

    def getAllAccountInfo(self, args):
        show_delete = args['show_delete']
        returnRaw = args['return_raw']
        attrs = ['acnt_id', 'crc_id', 'nameme', 'showable', 'deleteable']
        condition = '' # 默认获取所有记录
        if show_delete == False:
            condition = 'showable = 1'
        return self.__selectData(attrs, 'account', condition, returnRaw)

    def getAllAccountInfoGroupedByCurrency(self, args):
        show_delete = args['show_delete']
        returnRaw = args['return_raw']
        attrs = ['acnt_id', 'crc_id', 'nameme', 'showable', 'deleteable']
        condition = '' # 默认获取所有记录
        if show_delete == False:
            condition = 'showable = 1'
        # 獲取賬戶信息
        accountInfo = self.__selectData(attrs, 'account', condition, returnRaw)
        if accountInfo['errno'] != Error.SUCCESS:
            return accountInfo
        else :
            accountInfo = accountInfo['return']
        # 獲取幣種信息
        attrs = ['crc_id', 'nameme', 'unit', 'characterter', 'showable']
        currencyInfo = self.__selectData(attrs, 'currency', condition, returnRaw)
        if currencyInfo['errno'] != Error.SUCCESS:
            return currencyInfo
        else :
            currencyInfo = currencyInfo['return']
        # 把幣種和賬戶信息拼起來
        ret = {}
        for info in currencyInfo:
            crc_id = info['crc_id']
            info['account_list'] = []
            ret[crc_id] = info
        for info in accountInfo:
            crc_id = info['crc_id']
            ret[crc_id]['account_list'].append(info)
        ret = list(ret.values())
        return makeReturn(Error.SUCCESS, ret)

    def getIncomeCategory(self, args):
        show_delete = args['show_delete']
        returnRaw = args['return_raw']
        attrs = ['cat1_id', 'nameme', 'showable']
        condition = ''
        if show_delete == False:
            condition = 'showable = 1'
        return self.__selectData(attrs, 'income_cat1', condition, returnRaw)

    def getPaymentCategory1(self, args):
        show_delete = args['show_delete']
        returnRaw = args['return_raw']
        attrs = ['cat1_id', 'nameme', 'showable']
        condition = ''
        if show_delete == False:
            condition = 'showable = 1'
        return self.__selectData(attrs, 'payment_cat1', condition, returnRaw)

    def getPaymentCategory2(self, args):
        show_delete = args['show_delete']
        returnRaw = args['return_raw']
        attrs = ['cat2_id', 'cat1_id', 'nameme', 'showable']
        condition = ''
        if show_delete == False:
            condition = 'showable = 1'
        return self.__selectData(attrs, 'payment_cat2', condition, returnRaw)
        
    def getTransferCategory(self, args):
        show_delete = args['show_delete']
        returnRaw = args['return_raw']
        attrs = ['cat1_id', 'nameme', 'showable']
        condition = ''
        if show_delete == False:
            condition = 'showable = 1'
        return self.__selectData(attrs, 'transfer_cat1', condition, returnRaw)

    def addIncomeRecord(self, args):
        acnt_id = args['account_id']
        timeme = args['current_time']
        amount = args['amount']
        cat1_id = args['cat1_id']
        description = args['description']
        ret = timestampToDailyMonthlyAnnuallyTimestamp(timeme)
        dayTime = ret['day']
        monthTime = ret['month']
        yearTime = ret['year']
        sqls = []
        sqls.append('INSERT INTO income_record(rcd_id, acnt_id, timeme, amount, cat1_id, describebe, showable) VALUES (NULL, %s, %s, %s, %s, \'%s\', 1)'%(acnt_id, timeme, amount, cat1_id, description))
        sqls.append('UPDATE account_balance SET balance = balance + %s WHERE acnt_id = acnt_id'%(amount))
        sqls.append('INSERT OR IGNORE INTO daily_stat_record(timeme, income, payment) VALUES(%s, 0, 0)'%(dayTime))
        sqls.append('UPDATE daily_stat_record SET income = income + %s WHERE timeme = %s'%(amount, dayTime))
        sqls.append('INSERT OR IGNORE INTO monthly_stat_record(timeme, income, payment) VALUES(%s, 0, 0)'%(monthTime))
        sqls.append('UPDATE monthly_stat_record SET income = income + %s WHERE timeme = %s'%(amount, monthTime))
        sqls.append('INSERT OR IGNORE INTO annually_stat_record(timeme, income, payment) VALUES(%s, 0, 0)'%(yearTime))
        sqls.append('UPDATE annually_stat_record SET income = income + %s WHERE timeme = %s'%(amount, yearTime))
        return self.executeTransaction(sqls)

    def addPaymentRecord(self, args):
        acnt_id = args['account_id']
        timeme = args['current_time']
        amount = args['amount']
        cat1_id = args['cat1_id']
        cat2_id = args['cat2_id']
        description = args['description']
        ret = timestampToDailyMonthlyAnnuallyTimestamp(timeme)
        dayTime = ret['day']
        monthTime = ret['month']
        yearTime = ret['year']
        sqls = []
        sqls.append('INSERT INTO payment_record (rcd_id, acnt_id, timeme, amount, cat1_id, cat2_id, describebe, showable) VALUES (NULL, %s, %s, %s, %s, %s, \'%s\', 1)'%(acnt_id, timeme, amount, cat1_id, cat2_id, description))
        sqls.append('UPDATE account_balance SET balance = balance - %s WHERE acnt_id = acnt_id'%(amount))
        sqls.append('INSERT OR IGNORE INTO daily_stat_record(timeme, income, payment) VALUES(%s, 0, 0)'%(dayTime))
        sqls.append('UPDATE daily_stat_record SET payment = payment + %s WHERE timeme = %s'%(amount, dayTime))
        sqls.append('INSERT OR IGNORE INTO monthly_stat_record(timeme, income, payment) VALUES(%s, 0, 0)'%(monthTime))
        sqls.append('UPDATE monthly_stat_record SET payment = payment + %s WHERE timeme = %s'%(amount, monthTime))
        sqls.append('INSERT OR IGNORE INTO annually_stat_record(timeme, income, payment) VALUES(%s, 0, 0)'%(yearTime))
        sqls.append('UPDATE annually_stat_record SET payment = payment + %s WHERE timeme = %s'%(amount, yearTime))
        return self.executeTransaction(sqls)

    def addTransferRecord(self, args):
        timeme = args['current_time']
        amount = args['amount']
        cat1_id = args['cat1_id']
        src_acnt_id = args['src_account_id']
        dst_acnt_id = args['dst_account_id']
        description = args['description']
        sqls = []
        sqls.append('INSERT INTO transfer_record (rcd_id, timeme, amount, cat1_id, src_acnt_id, dst_acnt_id, describebe, showable) VALUES (NULL, %s, %s, %s, %s, %s, \'%s\', 1)'%(timeme, amount, cat1_id, src_acnt_id, dst_acnt_id, description))
        sqls.append('UPDATE account_balance SET balance = balance + %d WHERE acnt_id = %d'%(amount, dst_acnt_id))
        sqls.append('UPDATE account_balance SET balance = balance - %d WHERE acnt_id = %d'%(amount, src_acnt_id))
        return self.executeTransaction(sqls)

    def getIncomeRecord(self, args):
        pass

    def getPaymentRecord(self, args):
        pass

    def getTransferRecord(self, args):
        pass

    def getAllCurrency(self, args):
        attrs = ['crc_id', 'nameme', 'unit', 'characterter', 'showable']
        show_delete = args['show_delete']
        returnRaw = args['return_raw']
        condition = ''
        if show_delete == False:
            condition = 'showable = 1'
        return self.__selectData(attrs, 'currency', condition, returnRaw)
