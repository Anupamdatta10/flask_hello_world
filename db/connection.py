
import mysql.connector

class connection():
    def __init__(self):
        self.con=mysql.connector.connect(host='127.0.0.1',user='root',password='',database='test')
        self.db=self.con.cursor(dictionary=True)