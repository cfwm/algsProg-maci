from db.chore.write import writeDB
from db.chore.read import readDB

def createUser(payload):
  writeDB('user', payload)

def readUserById(id):
  users = readDB('user')
  if id in users:
    return users[id]
  else:
    return None