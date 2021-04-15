from Common import *
from DB import *

class Account:
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

    def getAll(self, args):
        args = self.__handleSpecialArgs(args)
        return self.db.call('getAllAccountInfo', args)

    def getAllGroupedByCurrency(self, args):
        args = self.__handleSpecialArgs(args)
        return self.db.call('getAllAccountInfoGroupedByCurrency', args)

    