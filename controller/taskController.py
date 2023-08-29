from models.queryModels.task import user_model
from flask import Flask , jsonify,request
obj=user_model()
def taskController():
    # Task.query('select * from tasks')
    return obj.getAllUsers()

def store():
    print(request.get_json(force=True) )
    return 'create data'
    # return obj.createUser()