from Common import *

class Account:
    def __init__(self):
        pass

    def handle(self):
        ret = {'data':'test from Account'}
        return makeReturn(Error.SUCCESS, ret)