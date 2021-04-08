
class Error:
    SUCCESS = 0
    ILLEGAL_ARGS = 1001
    ILLEGAL_URL = 1002
    DATABASE_ERROR = 1003
    ERROR_TEST = 9999

    errmsg = {\
        SUCCESS : 'success' ,\
        ILLEGAL_ARGS : 'illegal args' ,\
        ILLEGAL_URL : 'illegal URL' ,\
        DATABASE_ERROR : 'database error' ,\
        ERROR_TEST : 'error test'\
    }

def makeReturn(errno, data=None):
    ret = {'errno':errno, 'message':Error.errmsg[errno]}
    if data != None:
        ret['return'] = data
    return ret 
