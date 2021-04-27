import requests
import json
import time
import DatabaseController
import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/api/v1/user/add', methods=['POST'])
def add_user_route():
    req = request.data.decode("utf-8")
    req = json.loads(req)
    if DatabaseController.Users().insert_user(req['fullname'], req['birth'], req['cpf'], req['height']):
        return 'Sucess', 200
    else:
        return 'Error: cannot insert user in database.', 400

@app.route('/api/v1/user/update/<int:id>', methods=['PUT'])
def update_user_route(id):
    req = request.data.decode("utf-8")
    req = json.loads(req)
    if DatabaseController.Users().update_user(id, req['fullname'], req['birth'], req['cpf'], req['height']):
        return 'Sucess', 200
    else:
        return 'Error: cannot update user in database.', 400

@app.route('/api/v1/user/delete/<int:id>', methods=['DELETE'])
def delete_user_route(id):
    if DatabaseController.Users().delete_user(id):
        return 'Sucess', 200
    else:
        return 'Error: cannot delete user in database.', 400

@app.route('/api/v1/users', methods=['GET'])
def get_users_route():
    users = DatabaseController.Users().get_users()
    if users:
        return pd.DataFrame(users, columns=['id', 'name', 'birth', 'cpf', 'height']).to_json(orient="records")
    else:
        return str(users), 400

@app.route('/')
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)