import json

class URLBackup:
    def __init__(self):
        self.fileName = 'commit.backup'
        self.writfulInterface = { \
            'record_addIncome','record_addPayment','record_addTransfer' \
        }

    def backup(self, service_name, interface_name, args):
        key = service_name + '_' + interface_name
        if key not in self.writfulInterface:
            return
        line = service_name + ' '  + interface_name + ' ' + json.dumps(args) + '\n'
        f = open(self.fileName, 'a')
        f.write(line)
        f.close()