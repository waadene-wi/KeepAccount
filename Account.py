from Common import *
from DB import *

class Account:
    def __init__(self):
        self.db = DB()

    def getAll(self, args):
        show_delete = False
        if 'show_delete' in args and args['show_delete'] == 1:
            show_delete = True
        return self.db.getAllAccountInfo(show_delete)
    