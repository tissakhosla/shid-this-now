'''handle sql actions'''
import sqlite3
from datetime import datetime

class Crud:
    '''sql crud'''
    def __init__(self, db):
        self.db = db
        self.createSheds()
        self.createLogsTable()

    def crud(self, cmd=None, tup=None):
        con = sqlite3.connect(self.db)
        try:
            if cmd:
                cur = con.cursor()
                if tup:
                    cur.execute(cmd, tup)
                else:
                    cur.execute(cmd)
            con.commit()
        finally:
            con.close()

    def createSheds(self):
        self.crud()

    def createLogsTable(self):
        '''create the initial table'''
        self.crud('''CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            start TIMESTEMP,
            end TIMESTAMP)''')
    
    def createLogEntry(self, vals):
        self.crud('INSERT INTO logs (name, start, end) VALUES (?, ?, ?)', vals)