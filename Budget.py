from Common import *
from DB import *

class Budget:
    def __init__(self, logger):
        self.db = DB(logger)
        self.logger = logger