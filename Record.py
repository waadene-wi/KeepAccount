from Common import *
import DB
import time
from DictParamChecker import *

class Record:
    def __init__(self, logger):
        self.db = DB.DB(logger)
        self.logger = logger
    
    def test(self, args):
        return makeReturn(Error.SUCCESS, {'hello':'world', 'from':'record'})

    def __specialInputArgsTransfer(self, args):
        '''成功返回轉換後的args，否則返回-1'''
        if 'current_time' in args:
            args['current_time'] = timestampFromString(args['current_time'])
        if 'begin_time' in args:
            args['begin_time'] = timestampFromString(args['begin_time'])
        if 'end_time' in args:
            args['end_time'] = timestampFromString(args['end_time'])
        if 'amount' in args:
            args['amount'] = yuanStrToFenInt(args['amount'])
        return args

    def __specialValueTransfer(self, rows):
        '''转换从数据库返回的数据中的某些值
        没有返回值'''
        for i in range(0, len(rows)):
            if 'amount' in rows[i]:
                rows[i]['amount'] = fenIntToYuanStr(rows[i]['amount'])
            if 'timeme' in rows[i]:
                rows[i]['timeme'] = timestampToString(rows[i]['timeme'])
        return rows

    def addIncome(self, args):
        checker = DictParamChecker()
        checker.addParam('currency_id', 'int', True)
        checker.addParam('account_id', 'int', True)
        checker.addParam('current_time', 'str', True)
        checker.addParam('amount', 'float', True)
        checker.addParam('cat1_id', 'int', True)
        checker.addParam('description', 'str', False, '')
        args = checker.check(args)
        if type(args) == str:
            return makeReturn(Error.ILLEGAL_ARGS)
        args = self.__specialInputArgsTransfer(args)
        if args == -1:
            return makeReturn(Error.ILLEGAL_ARGS)
        return self.db.call('addIncomeRecord', args)

    def addPayment(self, args):
        checker = DictParamChecker()
        checker.addParam('currency_id', 'int', True)
        checker.addParam('account_id', 'int', True)
        checker.addParam('current_time', 'str', True)
        checker.addParam('amount', 'float', True)
        checker.addParam('cat1_id', 'int', True)
        checker.addParam('cat2_id', 'int', True)
        checker.addParam('description', 'str', False, '')
        args = checker.check(args)
        if type(args) == str:
            return makeReturn(Error.ILLEGAL_ARGS)
        args = self.__specialInputArgsTransfer(args)
        if args == -1:
            return makeReturn(Error.ILLEGAL_ARGS)
        return self.db.call('addPaymentRecord', args)

    def addTransfer(self, args):
        checker = DictParamChecker()
        checker.addParam('currency_id', 'int', True)
        checker.addParam('current_time', 'str', True)
        checker.addParam('amount', 'float', True)
        checker.addParam('cat1_id', 'int', True)
        checker.addParam('src_account_id', 'int', True)
        checker.addParam('dst_account_id', 'int', True)
        checker.addParam('description', 'str', False, '')
        args = checker.check(args)
        if type(args) == str:
            self.logger.warning(args)
            return makeReturn(Error.ILLEGAL_ARGS)
        args = self.__specialInputArgsTransfer(args)
        if args == -1:
            return makeReturn(Error.ILLEGAL_ARGS)
        return self.db.call('addTransferRecord', args)

    def getIncome(self, args):
        checker = DictParamChecker()
        checker.addParam('begin_time', 'str', True)
        checker.addParam('end_time', 'str', True)
        args = checker.check(args)
        if type(args) == str:
            self.logger.warning(args)
            return makeReturn(Error.ILLEGAL_ARGS)
        args = self.__specialInputArgsTransfer(args)
        if args == -1:
            return makeReturn(Error.ILLEGAL_ARGS)
        dbData = self.db.call('getIncomeRecord', args)
        if dbData['errno'] != Error.SUCCESS:
            return dbData
        dbData = self.__specialValueTransfer(dbData['return'])
        return makeReturn(Error.SUCCESS, dbData)

    def getPayment(self, args):
        checker = DictParamChecker()
        checker.addParam('begin_time', 'str', True)
        checker.addParam('end_time', 'str', True)
        args = checker.check(args)
        if type(args) == str:
            self.logger.warning(args)
            return makeReturn(Error.ILLEGAL_ARGS)
        args = self.__specialInputArgsTransfer(args)
        if args == -1:
            return makeReturn(Error.ILLEGAL_ARGS)
        dbData = self.db.call('getPaymentRecord', args)
        if dbData['errno'] != Error.SUCCESS:
            return dbData
        dbData = self.__specialValueTransfer(dbData['return'])
        return makeReturn(Error.SUCCESS, dbData)

    def getTransfer(self, args):
        checker = DictParamChecker()
        checker.addParam('begin_time', 'str', True)
        checker.addParam('end_time', 'str', True)
        args = checker.check(args)
        if type(args) == str:
            self.logger.warning(args)
            return makeReturn(Error.ILLEGAL_ARGS)
        args = self.__specialInputArgsTransfer(args)
        if args == -1:
            return makeReturn(Error.ILLEGAL_ARGS)
        dbData = self.db.call('getTransferRecord', args)
        if dbData['errno'] != Error.SUCCESS:
            return dbData
        dbData = self.__specialValueTransfer(dbData['return'])
        return makeReturn(Error.SUCCESS, dbData)
