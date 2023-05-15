'''handle sql actions'''
import sqlite3
from datetime import datetime, timedelta

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

    def readLogs(self):
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
                        # xr.append(f"{v - row[2]}")
                        td = timedelta((row[2]/1000) - (v/1000))
                        d = td.total_seconds()
                        hh = d.seconds // 3600
                        mm = (d.seconds % 3600) // 60
                        ss = d.seconds % 60
                        xr.append("{:02d}:{:02d}:{:02d}".format(hh, mm, ss))
                logs.append(xr)
            con.commit()
        finally:
            con.close()
        return logs
