#import objects from a flask model first
from flask import Flask, request, session, jsonify

app = Flask(__name__) #app uses flask

users = [
    {'name': 'Brian Nomwesigwa', 'email':'bnomwesigwa@gmail.com', 'password':'rest'}, 
    {'name': 'John Bay', 'email': 'bhoa@gmail.com', 'password': 'restful'}, 
    {'name': 'Alex Hunter', 'email': 'api@gmail.com', 'password': 'restless'}
]

@app.route('/', methods=['GET'])
def Test():
    return jsonify({'message':'it works properly'})

@app.route('/allusers', methods=['GET'])
def ReturnAll():
    return jsonify({'users': users})


@app.route('/allusers/<string:name>', methods=['GET'])
def ReturnOne(name):
    user = [user for user in users if user['name'] == name]
    return jsonify({'user':users[0]})

if __name__ == '__main__':
    app.run(debug=True) 
