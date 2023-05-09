from dataBase.read import readDB
from dataBase.write import writeDB
from time import time

class UserModel():
  def __init__(self):
    None

  def getUsersDict(self):
    return readDB('user')

  def getById(self, id):
    users = self.getUsersDict()
    if id in users:
      return users[id]
    else:
      None
  
  def createUser(self, id: str, name: str, email: str):
    userData = {
      'id': id,
      'name': name,
      'email': email,
      'occurrences': list(),
      'createdAt': time()
    }
    writeDB('user', userData)
    return userData


  # def getUser(id):
  #   users = readDB('user')
  #   if id in users:
  #     return users[id]
  #   else:
  #     return None