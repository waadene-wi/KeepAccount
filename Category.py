from Common import *
from DB import *

class Category:
    def __init__(self, logger):
        self.db = DB(logger)
        self.logger = logger

    def __handleSpecialArgs(self, args):
        if 'show_delete' in args and args['show_delete'] == '1':
            args['show_delete'] = True
        else:
            args['show_delete'] = False
        if 'return_raw' in args and args['return_raw'] == '1':
            args['return_raw'] = True
        else:
            args['return_raw'] = False
        return args

    def getIncome(self, args):
        args = self.__handleSpecialArgs(args)
        return self.db.call('getIncomeCategory', args)

    def getPaymentCat1(self, args):
        args = self.__handleSpecialArgs(args)
        return self.db.call('getPaymentCategory1', args)

    def getPaymentCat2(self, args):
        args = self.__handleSpecialArgs(args)
        return self.db.call('getPaymentCategory2', args)

    def getPayment(self, args):
        args = self.__handleSpecialArgs(args)
        ret1 = self.db.call('getPaymentCategory1', args)
        if ret1['errno'] != Error.SUCCESS:
            return ret1
        ret2 = self.db.call('getPaymentCategory2', args)
        if ret2['errno'] != Error.SUCCESS:
            return ret2
        ret = {}
        for cat1_item in ret1['return']:
            cat1_id = cat1_item['cat1_id']
            cat1_item['cat2_list'] = []
            ret[cat1_id] = cat1_item
        for cat2_item in ret2['return']:
            cat1_id = cat2_item['cat1_id']
            ret[cat1_id]['cat2_list'].append(cat2_item)
        return makeReturn(Error.SUCCESS, list(ret.values()))

    def getTransfer(self, args):
        args = self.__handleSpecialArgs(args)
        return self.db.call('getTransferCategory', args)
        


