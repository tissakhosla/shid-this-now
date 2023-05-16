'''handle sql actions'''
import sqlite3
from datetime import datetime
from xform import timelength

class Crud:
    '''sql crud'''
    def __init__(self, db):
        self.db = db
        self.createSheds()
        self.createLogsTable()

    def crud(self, cmd=None, tup=None):
        '''general crud wrapper'''
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
            start TIMESTAMP,
            end TIMESTAMP)''')

    def createLogEntry(self, vals):
        self.crud('INSERT INTO logs (name, start, end) VALUES (?, ?, ?)', vals)

    def readLogs(self):
        '''read all logs'''
        logs = []
        con = con = sqlite3.connect(self.db)
        try:
            cur = con.cursor()
            for row in cur.execute('SELECT * FROM logs'):
                xr = []
                for i, v in enumerate(row):
                    if not i:
                        continue
                    if i == 1:
                        xr.append(v)
                    if i == 2:
                        xr.append(datetime.fromtimestamp(v/1000).strftime("%Y-%m-%d %H:%M:%S"))
                    if i == 3:
                        xr.append(f'{timelength(v - row[2])}')
                logs.append(xr)
            con.commit()
        finally:
            con.close()
        return logs
