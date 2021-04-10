from Common import *
from DB import *

class Category:
    def __init__(self):
        self.db = DB()

    def getIncome(self, args):
        show_delete = False
        if 'show_delete' in args and show_delete == 1:
            show_delete = True
        return self.db.getIncomeCategory(show_delete)

    def getPaymentCat1(self, args):
        show_delete = False
        if 'show_delete' in args and show_delete == 1:
            show_delete = True
        return self.db.getPaymentCategory1(show_delete)

    def getPaymentCat2(self, args):
        show_delete = False
        if 'show_delete' in args and show_delete == 1:
            show_delete = True
        return self.db.getPaymentCategory2(show_delete)

    def getPayment(self, args):
        show_delete = False
        if 'show_delete' in args and show_delete == 1:
            show_delete = True
        ret1 = self.db.getPaymentCategory1(show_delete)
        if ret1['errno'] != Error.SUCCESS:
            return ret1
        ret2 = self.db.getPaymentCategory2(show_delete)
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
        return list(ret.values())

    def getTransfer(self, args):
        show_delete = False
        if 'show_delete' in args and show_delete == 1:
            show_delete = True
        return self.db.getTransferCategory(show_delete)
        


