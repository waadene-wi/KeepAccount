import sqlite3
from Common import *

DB_NAME = 'ka.db'

class DB:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(DB_NAME)
        self.cursor = self.connection.cursor()

    def __selectData(self, attrs, tableName, condition):
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
            return makeReturn(Error.DATABASE_ERROR)
        cursor.close()
        connection.close()
        # 把属性名字加入数据库返回的数据中
        ret = []
        for row in dbData:
            rowMap = {}
            for i in range(0, len(attrs)):
                rowMap[attrs[i]] = row[i]
            ret.append(rowMap)
        return makeReturn(Error.SUCCESS, ret)

    def getAllAccountInfo(self, show_delete):
        attrs = ['acnt_id', 'crc_id', 'nameme', 'showable', 'deleteable']
        condition = '' # 默认获取所有记录
        if show_delete == False:
            condition = 'showable = 1'
        return self.__selectData(attrs, 'account', condition)

    def getIncomeCategory(self, show_delete):
        attrs = ['cat1_id', 'nameme', 'showable']
        condition = ''
        if show_delete == False:
            condition = 'showable = 1'
        return self.__selectData(attrs, 'income_cat1', condition)

    def getPaymentCategory1(self, show_delete):
        attrs = ['cat1_id', 'nameme', 'showable']
        condition = ''
        if show_delete == False:
            condition = 'showable = 1'
        return self.__selectData(attrs, 'payment_cat1', condition)

    def getPaymentCategory2(self, show_delete):
        attrs = ['cat1_id', 'cat1_id', 'nameme', 'showable']
        condition = ''
        if show_delete == False:
            condition = 'showable = 1'
        return self.__selectData(attrs, 'payment_cat2', condition)
        
    def getTransferCategory(self, show_delete):
        attrs = ['cat1_id', 'nameme', 'showable']
        condition = ''
        if show_delete == False:
            condition = 'showable = 1'
        return self.__selectData(attrs, 'transfer_cat1', condition)