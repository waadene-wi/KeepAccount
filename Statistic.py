from Common import *
import DB
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

    def getIncomeCat1Percentage(self, args):
        checker = DictParamChecker()
        checker.addParam('begin_time', 'int', True)
        checker.addParam('end_time', 'int', True)
        checker.addParam('interval', 'string', True)
        args = checker.check(args)
        if type(args) == str:
            self.logger.warning(args)
            return makeReturn(Error.ILLEGAL_ARGS)
        args = self.__specialInputArgsTransfer(args)
        ret = self.db.call('getIncomeCat1Percentage', args)
        if ret['errno'] != Error.SUCCESS:
            return ret
        