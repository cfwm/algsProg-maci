from dataBase.read import readDB
from dataBase.write import writeDB
from datetime import datetime

class UserModel():
  def __init__(self):
    None

  def readUsersDict(self):
    return readDB('user')

  def readUserById(self, id):
    users = self.readUsersDict()
    response = None
    if id in users:
      response = users[id]
    return response
  
  def createUser(self, id: str, name: str, email: str):
    userData = {
      'id': id,
      'name': name,
      'email': email,
      'createdAt': datetime.now(),
    }
    writeDB('user', userData)
    return userData