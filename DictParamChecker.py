class DictParamChecker:
    def __init__(self):
        self.paramInfo = {}

    def addParam(self, name, valueType, required, default=None):
        if type(name) != str:
            raise ValueError('name is not string!')
        if type(valueType) != str:
            raise ValueError('valueType is not type!')
        if type(required) != bool:
            raise ValueError('required is not bool!')
        self.paramInfo[name] = {'type':valueType, 'required':required, 'default':default}

    def check(self, params):
        ''' 返回params，否則返回錯誤信息字符串'''
        if type(params) != dict:
            return 'type of params is not dict'
        for name in self.paramInfo:
            # 檢查參數是否是必填參數
            if self.paramInfo[name]['required'] == True:
                if name not in params:
                    return 'param %s is missing'%(name)
            else:
                if name not in params:
                    params[name] = self.paramInfo[name]['default']
            # 檢查參數類型
            valueType = self.paramInfo[name]['type']
            try:
                if valueType == 'str':
                    if type(params[name]) != str:
                        raise TypeError()
                elif valueType == 'int':
                    int(params[name])
                elif valueType == 'float':
                    float(params[name])
            except:
                return 'type of %s is not correct'%(name)
        return params
            