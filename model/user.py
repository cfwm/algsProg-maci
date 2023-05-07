from utils.hash.md5 import getHash
from db.user import createUser, readUserById

class User:
  def __init__(self):
    None
  
  def create(self, name, email):
    self.id = getHash(email)
    self.name = name
    self.email = email
    self.occurrences = list()
    createUser({
      'id': self.id,
      'name': self.name,
      'email': self.email,
      'occurrences': self.occurrences
    })

  def read(self):
    return readUserById(self.id)