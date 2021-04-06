import sqlite3

DB_NAME = 'keepaccount.db'

class DB:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(DB_NAME)
        self.cursor = self.connection.cursor()
        

global db
db = DB()