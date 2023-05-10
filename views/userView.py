from views.components.inputs import stringInput

from utils.hash.md5 import getHash
from controllers.userController import UserController

class UserView():
  def __init__(self):
    print('Bem vindo ao Mapa Ambiental Colaborativo e Interativo!')
    self.currentAction = 'login'

  # def listUserData(self)
    
  
  # def createComplaintOccurrence(self) -> bool:
