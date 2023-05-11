from models.userModel import UserModel

class UserController(UserModel):
  def __init__(self):
    None

  def getUsersDict(self):
    return self.readUsersDict()
  
  def addUser(self, id: str, name: str, email: str):
    return self.createUser(id, name, email)
  
  def checkIsValidUser(self, id: str) -> dict | None:
    users = self.readUsersDict()
    if id in users:
      return users[id]
    else:
      None