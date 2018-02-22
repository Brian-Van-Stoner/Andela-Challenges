#import objects from a flask model first
from flask import Flask, request, session, jsonify

app = Flask(__name__) #app uses flask

#Dic to be used
users = [
    {'name': 'Brian'}, {'name': 'John'}, {'name': 'Alex'}
]
#Test code Just to make sure it works fine
@app.route('/', methods=['GET'])
def test():
    return jsonify({'message':'it works properly'})

#Returning the whole dic
@app.route('/allusers', methods=['GET'])
def returnAll():
    return jsonify({'users' : users})


#returning only the value searched for
@app.route('/allusers/<string:name>', methods=['GET'])
def returnOne(name):
    userful = [user for user in users if user['name'] == name]
    return jsonify({'user' : userful[0]})

#adding values to the dic
@app.route('/allusers', methods=['POST'])
def addUser():
    username = {'name' : request.json['name']} #creates a new dic and return Json value sent by POST request
    
    users.append(username)
    return jsonify({'users' : users})
 
#Updating DB
@app.route('/allusers/<string:name>', methods=['PUT'])
def editOne(name):
    userful = [user for user in users if user['name'] == name]
    userful[0]['name'] = request.json['name'] #update name 
    return jsonify({'user' : userful[0]})

#Delete Request
@app.route('/allusers/<string:name>', methods=['DELETE'])
def deleteOne(name):
    userless = [user for user in users if user['name'] == name]
    users.remove(userless[0])
    return jsonify({'users': users[0]})

if __name__ == '__main__':
    app.run(debug=True) 
