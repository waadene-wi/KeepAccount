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
        crc_id = args['currency_id']
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
        sqls.append('INSERT OR IGNORE INTO daily_stat_record(timeme, crc_id, income, payment) VALUES(%s, %s, 0, 0)'%(dayTime, crc_id))
        sqls.append('UPDATE daily_stat_record SET income = income + %s WHERE timeme = %s and crc_id = %s'%(amount, dayTime, crc_id))
        sqls.append('INSERT OR IGNORE INTO monthly_stat_record(timeme, crc_id, income, payment) VALUES(%s, %s, 0, 0)'%(monthTime, crc_id))
        sqls.append('UPDATE monthly_stat_record SET income = income + %s WHERE timeme = %s and crc_id = %s'%(amount, monthTime, crc_id))
        sqls.append('INSERT OR IGNORE INTO annually_stat_record(timeme, crc_id, income, payment) VALUES(%s, %s, 0, 0)'%(yearTime, crc_id))
        sqls.append('UPDATE annually_stat_record SET income = income + %s WHERE timeme = %s and crc_id = %s'%(amount, yearTime, crc_id))
        return self.executeTransaction(sqls)

    def addPaymentRecord(self, args):
        crc_id = args['currency_id']
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
        sqls.append('INSERT OR IGNORE INTO daily_stat_record(timeme, crc_id, income, payment) VALUES(%s, %s, 0, 0)'%(dayTime, crc_id))
        sqls.append('UPDATE daily_stat_record SET payment = payment + %s WHERE timeme = %s and crc_id = %s'%(amount, dayTime, crc_id))
        sqls.append('INSERT OR IGNORE INTO monthly_stat_record(timeme, crc_id, income, payment) VALUES(%s, %s, 0, 0)'%(monthTime, crc_id))
        sqls.append('UPDATE monthly_stat_record SET payment = payment + %s WHERE timeme = %s and crc_id = %s'%(amount, monthTime, crc_id))
        sqls.append('INSERT OR IGNORE INTO annually_stat_record(timeme, crc_id, income, payment) VALUES(%s, %s, 0, 0)'%(yearTime, crc_id))
        sqls.append('UPDATE annually_stat_record SET payment = payment + %s WHERE timeme = %s and crc_id = %s'%(amount, yearTime, crc_id))
        return self.executeTransaction(sqls)

    def addTransferRecord(self, args):
        timeme = args['current_time']
        amount = args['amount']
        cat1_id = args['cat1_id']
        crc_id = args['currency_id']
        src_acnt_id = args['src_account_id']
        dst_acnt_id = args['dst_account_id']
        description = args['description']
        sqls = []
        sqls.append('INSERT INTO transfer_record (rcd_id, timeme, amount, cat1_id, src_acnt_id, dst_acnt_id, describebe, showable) VALUES (NULL, %s, %s, %s, %s, %s, \'%s\', 1)'%(timeme, amount, cat1_id, src_acnt_id, dst_acnt_id, description))
        sqls.append('UPDATE account_balance SET balance = balance + %s WHERE acnt_id = %s'%(amount, dst_acnt_id))
        sqls.append('UPDATE account_balance SET balance = balance - %s WHERE acnt_id = %s'%(amount, src_acnt_id))
        return self.executeTransaction(sqls)

    def getIncomeRecord(self, args):
        begin_time = args['begin_time']
        end_time = args['end_time']
        condition = 'WHERE timeme >= %s and timeme <= %s '%(begin_time, end_time)
        if 'account_id' in args:
            condition += 'and acnt_id = %s'%(args['account_id'])
        if 'cat1_id' in args:
            condition += 'and cat1_id = %s'%(args['cat1_id'])
        sqlStr = 'SELECT rcd_id, account.nameme, timeme, income_cat1.nameme, amount, describebe FROM \
            (SELECT * FROM income_record %s ORDER BY timeme DESC) AS rslt \
            LEFT JOIN account ON account.acnt_id = rslt.acnt_id \
            LEFT JOIN income_cat1 ON income_cat1.cat1_id = rslt.cat1_id'%(condition)
        try:
            dbData = self.cursor.execute(sqlStr).fetchall()
        except:
            self.logger.warning('query failed. sql:' + sqlStr)
            return makeReturn(Error.DATABASE_ERROR)
        attrs = ['rcd_id', 'acnt_name', 'timeme', 'cat1_name', 'amount', 'describebe']
        ret = []
        for row in dbData:
            ret.append(dict(zip(attrs, row)))
        return makeReturn(Error.SUCCESS, ret)

    def getPaymentRecord(self, args):
        begin_time = args['begin_time']
        end_time = args['end_time']
        condition = 'WHERE timeme >= %s and timeme <= %s '%(begin_time, end_time)
        if 'account_id' in args:
            condition += 'and acnt_id = %s'%(args['account_id'])
        if 'cat1_id' in args:
            condition += 'and cat1_id = %s'%(args['cat1_id'])
        sqlStr = 'SELECT rcd_id, account.nameme, timeme, payment_cat1.nameme, payment_cat2.nameme, amount, describebe FROM \
            (SELECT * FROM payment_record %s ORDER BY timeme DESC) AS rslt \
            LEFT JOIN account ON account.acnt_id = rslt.acnt_id \
            LEFT JOIN payment_cat1 ON payment_cat1.cat1_id = rslt.cat1_id \
            LEFT JOIN payment_cat2 ON payment_cat2.cat2_id = rslt.cat2_id'%(condition)
        try:
            dbData = self.cursor.execute(sqlStr).fetchall()
        except:
            self.logger.warning('query failed. sql:' + sqlStr)
            return makeReturn(Error.DATABASE_ERROR)
        attrs = ['rcd_id', 'acnt_name', 'timeme', 'cat1_name', 'cat2_name', 'amount', 'describebe']
        ret = []
        for row in dbData:
            ret.append(dict(zip(attrs, row)))
        return makeReturn(Error.SUCCESS, ret)

    def getTransferRecord(self, args):
        begin_time = args['begin_time']
        end_time = args['end_time']
        condition = 'WHERE timeme >= %s and timeme <= %s '%(begin_time, end_time)
        if 'src_account_id' in args:
            condition += 'and src_acnt_id = %s'%(args['src_account_id'])
        if 'dst_account_id' in args:
            condition += 'and dst_acnt_id = %s'%(args['dst_account_id'])
        if 'cat1_id' in args:
            condition += 'and cat1_id = %s'%(args['cat1_id'])
        sqlStr = 'SELECT rcd_id, timeme, acnt_1.nameme, acnt_2.nameme, transfer_cat1.nameme, amount, describebe FROM \
            (SELECT * FROM transfer_record %s ORDER BY timeme DESC) AS rslt \
            LEFT JOIN account AS acnt_1 ON acnt_1.acnt_id = rslt.src_acnt_id \
            LEFT JOIN account AS acnt_2 ON acnt_2.acnt_id = rslt.dst_acnt_id \
            LEFT JOIN transfer_cat1 ON transfer_cat1.cat1_id = rslt.cat1_id'%(condition)
        try:
            dbData = self.cursor.execute(sqlStr).fetchall()
        except:
            self.logger.warning('query failed. sql:' + sqlStr)
            return makeReturn(Error.DATABASE_ERROR)
        attrs = ['rcd_id', 'timeme', 'src_acnt_name', 'dst_acnt_name', 'cat1_name', 'amount', 'describebe']
        ret = []
        for row in dbData:
            ret.append(dict(zip(attrs, row)))
        return makeReturn(Error.SUCCESS, ret)

    def getAllCurrency(self, args):
        attrs = ['crc_id', 'nameme', 'unit', 'characterter', 'showable']
        show_delete = args['show_delete']
        returnRaw = args['return_raw']
        condition = ''
        if show_delete == False:
            condition = 'showable = 1'
        return self.__selectData(attrs, 'currency', condition, returnRaw)

    def getIncomeCat1Percentage(self, args):
        begin_time = args['begin_time']
        end_time = args['end_time']
        crc_id = args['currency_id']
        sqlStr = 'SELECT income_cat1.nameme, SUM(amount) FROM income_record\
            LEFT JOIN account on income_record.acnt_id = account.acnt_id\
            LEFT JOIN income_cat1 on income_record.cat1_id = income_cat1.cat1_id\
            WHERE account.crc_id = %s and income_record.timeme BETWEEN %s AND %s GROUP BY income_record.cat1_id'%(crc_id, begin_time, end_time)
        try:
            dbData = self.cursor.execute(sqlStr).fetchall()
        except:
            self.logger.warning('query failed. sql:' + sqlStr)
            return makeReturn(Error.DATABASE_ERROR)
        attrs = ['cat1_name', 'amount']
        ret = []
        for row in dbData:
            ret.append(dict(zip(attrs, row)))
        return makeReturn(Error.SUCCESS, ret)

    def getPaymentCat1Percentage(self, args):
        begin_time = args['begin_time']
        end_time = args['end_time']
        crc_id = args['currency_id']
        sqlStr = 'SELECT payment_cat1.nameme, SUM(amount) FROM payment_record\
            LEFT JOIN account on payment_record.acnt_id = account.acnt_id\
            LEFT JOIN payment_cat1 on payment_record.cat1_id = payment_cat1.cat1_id\
            WHERE account.crc_id = %s and payment_record.timeme BETWEEN %s AND %s GROUP BY payment_record.cat1_id'%(crc_id, begin_time, end_time)
        try:
            dbData = self.cursor.execute(sqlStr).fetchall()
        except:
            self.logger.warning('query failed. sql:' + sqlStr)
            return makeReturn(Error.DATABASE_ERROR)
        attrs = ['cat1_name', 'amount']
        ret = []
        for row in dbData:
            ret.append(dict(zip(attrs, row)))
        return makeReturn(Error.SUCCESS, ret)
        
        
