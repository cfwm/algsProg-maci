from model.userModel import UserModel

class UserController:
  def __init__(self):
    self.userModel = UserModel()


  def checkIsValidUser(self, id: str) -> dict | None:
    users = self.userModel.getUsersDict()
    if id in users:
      return users[id]
    else:
      None
  
  def createUser(self, id: str, name: str, email: str):
    return self.userModel.createUser(id, name, email)