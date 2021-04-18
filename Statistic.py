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

    def __getCat1Percentage(self, db_func_name, args):
        checker = DictParamChecker()
        checker.addParam('begin_time', 'string', True)
        checker.addParam('end_time', 'string', True)
        checker.addParam('currency_id', 'int', True)
        args = checker.check(args)
        if type(args) == str:
            self.logger.warning(args)
            return makeReturn(Error.ILLEGAL_ARGS)
        args = self.__specialInputArgsTransfer(args)
        ret = self.db.call(db_func_name, args)
        if ret['errno'] != Error.SUCCESS:
            return ret
        ret = ret['return']
        totalAmount = 0
        for row in ret:
            totalAmount += row['amount']
        for i in range(0, len(ret)):
            ret[i]['rate'] = ret[i]['amount'] / totalAmount * 100
        return makeReturn(Error.SUCCESS, ret)

    def getIncomeCat1Percentage(self, args):
        return self.__getCat1Percentage('getIncomeCat1Percentage', args)

    def getPaymentCat1Percentage(self, args):
        return self.__getCat1Percentage('getPaymentCat1Percentage', args)
        