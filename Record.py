from Common import *
from DB import *

class Record:
    def __init__(self):
        self.db = DB()
    
    def test(self, args):
        return makeReturn(Error.SUCCESS, {'hello':'world', 'from':'record'})

    def addIncome(self, args):
        pass
