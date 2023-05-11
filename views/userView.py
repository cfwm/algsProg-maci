from controllers.userController import UserController

class UserView(UserController):
  def __init__(self):
    None

  def getUser(self, id: str):
    print('getUser uid', id)
  # def updateUser(self)
