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

    def __specialArgsTransfer(self, args):
        '''成功返回轉換後的args，否則返回-1'''
        if 'current_time' in args:
            args['current_time'] = timestampFromString(args['current_time'])
        if 'amount' in args:
            args['amount'] = args['amount'] + '00'
        return args

    def addIncome(self, args):
        checker = DictParamChecker()
        checker.addParam('account_id', 'int', True)
        checker.addParam('current_time', 'str', True)
        checker.addParam('amount', 'float', True)
        checker.addParam('cat1_id', 'int', True)
        checker.addParam('description', 'str', False, '')
        args = checker.check(args)
        if type(args) == str:
            return makeReturn(Error.ILLEGAL_ARGS)
        args = self.__specialArgsTransfer(args)
        if args == -1:
            return makeReturn(Error.ILLEGAL_ARGS)
        return self.db.call('addIncomeRecord', args)

    def addPayment(self, args):
        checker = DictParamChecker()
        checker.addParam('account_id', 'int', True)
        checker.addParam('current_time', 'str', True)
        checker.addParam('amount', 'float', True)
        checker.addParam('cat1_id', 'int', True)
        checker.addParam('cat2_id', 'int', True)
        checker.addParam('description', 'str', False, '')
        args = checker.check(args)
        if type(args) == str:
            return makeReturn(Error.ILLEGAL_ARGS)
        args = self.__specialArgsTransfer(args)
        if args == -1:
            return makeReturn(Error.ILLEGAL_ARGS)
        return self.db.call('addPaymentRecord', args)

    def addTransfer(self, args):
        checker = DictParamChecker()
        checker.addParam('current_time', 'str', True)
        checker.addParam('amount', 'float', True)
        checker.addParam('cat1_id', 'int', True)
        checker.addParam('src_account_id', 'int', True)
        checker.addParam('dst_account_id', 'int', True)
        checker.addParam('description', 'str', False, '')
        args = checker.check(args)
        if type(args) == str:
            return makeReturn(Error.ILLEGAL_ARGS)
        args = self.__specialArgsTransfer(args)
        if args == -1:
            return makeReturn(Error.ILLEGAL_ARGS)
        return self.db.call('addTransferRecord', args)

    def getIncome(self, args):
        checker = DictParamChecker()
        checker.addParam('begin_time', 'str', True)
        checker.addParam('end_time', 'str', True)

    def getPayment(self, args):
        pass

    def getTransfer(self, args):
        pass
