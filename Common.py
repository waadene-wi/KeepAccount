import json

class Error:
    SUCCESS = 0
    ILLEGLA_ARGS = 1
    errmsg = {\
        SUCCESS : 'Success' \
    }

def makeReturn(errno, data=None):
    ret = {'errno':errno, 'message':Error.errmsg[errno]}
    if data != None:
        ret['return'] = data
    return json.dumps(ret)  