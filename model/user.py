from utils.hash.md5 import getHash
from db.user import createUser, readUserById
from db.chore.read import readDB

class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.id = getHash(email)
    self.occurrences = list()
  
  def create(self):
    createUser({
      'id': self.id,
      'name': self.name,
      'email': self.email,
      'occurrences': self.occurrences
    })

  def read(self):
    return readUserById(self.id)