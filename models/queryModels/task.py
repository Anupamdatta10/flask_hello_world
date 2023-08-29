from db.connection import connection
db=connection()

class user_model():
    def __init__(self):
        pass
        #  self.con=mysql.connector.connect(host='127.0.0.1',user='root',password='',database='test')
        #  self.db=self.con.cursor(dictionary=True)
    def getAllUsers(self):
        db.db.execute("SELECT * FROM task")
        result=db.db.fetchall()
        return {"data":result}

    def createUser(self):
        pass
        # db.db.execute('INSERT INTO task (description,status,user_id,date) VALUES \
        #     (% s, % s, 1, % s )',
        #                    (data['task'],data['status'],data['date'], ))