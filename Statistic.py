from Common import *
from DB import *
from DictParamChecker import *

class Statistic:
    def __init__(self, logger):
        self.db = DB.DB(logger)
        self.logger = logger
    
    def test(self, args):
        return makeReturn(Error.SUCCESS, {'hello':'world', 'from':'statistic'})

    def __specialInputArgsTransfer(self, args):
        '''成功返回轉換後的args，否則返回-1'''
        args['begin_time'] = timestampFromString(args['begin_time'])
        args['end_time'] = timestampFromString(args['end_time'])
        return args

    def getIncomePercentage(self, args):
        checker = DictParamChecker()
        checker.addParam('begin_time', 'int', True)
        checker.addParam('end_time', 'int', True)
        args = checker.check()
        if type(args) == str:
            self.logger