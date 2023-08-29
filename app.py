from flask import Flask , jsonify,request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
import MySQLdb.cursors
app = Flask(__name__)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'
 
 
mysql = MySQL(app)

@app.route('/',methods=['GET'])
def hello_world():
    # print("=====>>",request.headers['Authorization'])
    return 'Hello, World!'


@app.route('/getData',methods=['GET'])
def getData():
    print("request.args",request.args.get('status'))
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if(request.args.get('status')!=None):
       print ("SELECT * FROM task where status=%s", (request.args.get('status'),))
       cursor.execute("SELECT * FROM task where status=%s", (request.args.get('status'),))
    else:
        cursor.execute("SELECT * FROM task")
    dbdata = cursor.fetchall()
    result={"success":True,"message":"", "data":dbdata}
    return jsonify(result)

@app.route('/getDataById/<int:id>',methods=['GET'])
def getDataById(id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM task where id =  % s ",(id,))
    data = cursor.fetchone()
    if(data==None):
        result={"message":"no data found!", "data":data}
    else:
        result={"success":True,"message":"true", "data":data}
    return jsonify(result)


@app.route('/create',methods=['POST'])
def create():
    data=request.get_json(force=True) 
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('INSERT INTO task (description,status,user_id,date) VALUES \
            (% s, % s, 1, % s )',
                           (data['task'],data['status'],data['date'], ))
    mysql.connection.commit()
    result={"success":True,"message":"true", "data":data}
    return  result


@app.route('/update/<int:id>',methods=['PATCH'])
def update(id):
    data=request.get_json(force=True)
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute('update task set description=%s ,status=% s, date=%s where id = % s',
                           (data['task'],data['status'],data['date'], id,))
    mysql.connection.commit()
    result={"success":True,"message":"updated successfully", "data":data}
    return  result

if __name__ == '__main__':
    app.run(debug=True,port=8000)