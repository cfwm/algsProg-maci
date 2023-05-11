from views.components.inputs import inputValidEmail, inputNewUserName
from utils.hash.md5 import getHash
from controllers.userController import UserController


class LoginView(UserController):
  def __init__(self):
    None

  def login(self) -> bool:
    response = {
      'isRunning': False,
      'route': 'login',
      'user': None,
    }
    email = inputValidEmail()
    if not email:
      return response
    
    id = getHash(email)
    validUser = self.checkIsValidUser(id)

    if not validUser:
      newUserName = inputNewUserName()
      if newUserName:
        newUser = self.addUser(id, newUserName, email)
        if newUser:
          response = {
            'isRunning': True,
            'route': 'home',
            'user': newUser,
          }
    else:
      response = {
        'isRunning': True,
        'route': 'home',
        'user': validUser,
      }
    return response
