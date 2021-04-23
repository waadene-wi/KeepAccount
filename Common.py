import time

class Error:
    SUCCESS = 0
    ILLEGAL_ARGS = 1001
    ILLEGAL_URL = 1002
    DATABASE_ERROR = 1003
    METHOD_NOT_EXIST = 1004
    ERROR_TEST = 9999

    errmsg = {\
        SUCCESS : 'success' ,\
        ILLEGAL_ARGS : 'illegal args' ,\
        ILLEGAL_URL : 'illegal URL' ,\
        DATABASE_ERROR : 'database error' ,\
        ERROR_TEST : 'error test' ,\
        METHOD_NOT_EXIST : 'method not exist'
    }

def makeReturn(errno, data=None):
    ret = {'errno':errno, 'message':Error.errmsg[errno]}
    if data != None:
        ret['return'] = data
    return ret 

def timestampToDailyMonthlyAnnuallyTimestamp(timestamp):
    '''把時間戳轉換成對應的日、月、年的時間戳，單位：秒
    返回 {day, month, year}'''
    ts = time.localtime(timestamp)
    day_ts = time.strptime('%d-%d-%d'%(ts.tm_year, ts.tm_mon, ts.tm_mday), '%Y-%m-%d')
    day =int(time.mktime(day_ts))
    month_ts = time.strptime('%d-%d-1'%(ts.tm_year, ts.tm_mon), '%Y-%m-%d')
    month = int(time.mktime(month_ts))
    year_ts = time.strptime('%d-1-1'%(ts.tm_year), '%Y-%m-%d')
    year = int(time.mktime(year_ts))
    return {'day':day, 'month':month, 'year':year}

def timestampToString(timestamp):
    ts = time.localtime(timestamp)
    return time.strftime("%Y-%m-%d %H:%M", ts)

def timestampFromString(string):
    ts = time.strptime(string, "%Y-%m-%d %H:%M")
    return int(time.mktime(ts))

def fenIntToYuanStr(fen):
    '''把單位為（分）的整數轉換為單位為（元）的字符串'''
    isNegative = False
    if fen < 0:
        isNegative = True
        fen = 0 - fen
    yuan = fen // 100
    fen = fen % 100
    if fen == 0:
        retStr = str(yuan)
    else:
        retStr = str(yuan) + '.' + str(fen)
    if isNegative == True:
        retStr = '-' + retStr
    return retStr

def yuanStrToFenInt(yuan):
    '''把單位為（元）的字符串轉換成單位為（分）的整數'''
    fenStr = '0'
    yuanAndFen = yuan.split('.')
    yuanPart = yuanAndFen[0]
    if len(yuanAndFen) == 1:
        fenStr = yuanPart + '00'
    else: # len(yuanAndFen) == 2
        fenPart = yuanAndFen[1]
        if len(fenPart) == 1:
            fenStr = yuanPart + fenPart + '0'
        else: # len(fenPart) == 2
            fenStr = yuanPart + fenPart[0:1]
    return int(fenStr)
