import os
import sqlite3
APP_PATH=os.getcwd()
DB_PATH = APP_PATH + "\DiabetesDbase.db"

class Conect():
    def __init__(self):
        self.con = sqlite3.connect(DB_PATH)
        self.cursor = self.con.cursor()
        print("test", DB_PATH)
        
    def insertData(self,savedTime, txtGlucemia, txtTensionSistolica, txtTensionDiastolica):
        print ('debug insert', self.con, self.cursor)
        self.cursor.execute("""INSERT INTO CONTROL VALUES(?,?,?,?,?)""",(None,savedTime, txtGlucemia, txtTensionSistolica, txtTensionDiastolica) )
        self.con.commit()
        self.con.close()
        