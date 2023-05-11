from views.components.inputs import stringInput
from validators.email import checkIsValidEmail
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
    email = self.__inputValidEmail()
    if not email:
      return response
    
    id = getHash(email)
    validUser = self.checkIsValidUser(id)

    if not validUser:
      newUserName = self.__inputNewUserName()
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
    
  def __inputValidEmail(self) -> bool | str:
    email = stringInput([
      'Digite seu e-mail para continuar.',
    ])
    isValidEmail = checkIsValidEmail(email)
    while not isValidEmail:
      email = stringInput([
        'E-mail inválido.',
        'Digite um e-mail válido ou', 
        'digite 0 para sair do programa.',
      ])
      if email == '0':
        return False
      else:
        isValidEmail = checkIsValidEmail(email)
    return email

  def __inputNewUserName(self) -> bool | str:
    commandWantRegisterNewUser = stringInput([
      'Usuário não cadastrado. Digite:',
      '  1 para criar um novo usuário;',
      '  0 para sair.',
    ])
    validCommands = { '0', '1' }
    while not commandWantRegisterNewUser in validCommands:
      commandWantRegisterNewUser = stringInput([
        'Comando inválido. Digite:',
        ' 1 para criar um novo usuário',
        ' 0 para sair.',
      ])    
    
    response = None
    if commandWantRegisterNewUser == '0':
      response = False
    elif commandWantRegisterNewUser == '1':
      name = stringInput([
        'Digite seu nome.'
      ])
      response = name

    return response