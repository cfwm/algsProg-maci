from views.components.inputs import stringInput
from validators.email import checkIsValidEmail
from utils.hash.md5 import getHash
from controllers.userController import UserController


class LoginView(UserController):
  def __init__(self):
    None

  def login(self) -> bool:
    print('**login')
    response = {
      'user': None,
      'success': False,
      'nextRoute': 'login'
    }
    email = self.__inputValidEmail()
    if not email:
      return response
    
    id = getHash(email)
    validUser = self.checkIsValidUser(id)
    print('**validUser',validUser)

    if not validUser:
      newUserName = self.__inputNewUserName()
      print('### newUserName', newUserName)
      if newUserName:
        print('newUserName:')
        newUser = self.addUser(id, newUserName, email)
        if newUser:
          print('if newUser', newUser)
          response = {
            'user': newUser,
            'success': True,
            'nextRoute': 'home'
          }
    else:
      print('else not validUser')
      response = {
        'user': validUser,
        'success': True,
        'nextRoute': 'home'
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
    print('**** __inputNewUserName')
    wantRegisterNewUser = stringInput([
      'Usuário não cadastrado. Digite:',
      '  1 para criar um novo usuário;',
      '  0 para sair.',
    ])
    print('wantRegisterNewUser', wantRegisterNewUser)
    validCommands = { '0', '1' }
    while not wantRegisterNewUser in validCommands:
    # while wantRegisterNewUser != '1' or wantRegisterNewUser != '0':
      # print('wantRegisterNewUser',wantRegisterNewUser)
      # print('validCommands',validCommands)
      # print("not wantRegisterNewUser in validCommands",not wantRegisterNewUser in validCommands)
      # print('\n')
      wantRegisterNewUser = stringInput([
        'Comando inválido. Digite:',
        ' 1 para criar um novo usuário',
        ' 0 para sair.',
      ])    
      print('while wantRegisterNewUser', wantRegisterNewUser)
    
    print('AFTER wantRegisterNewUser', wantRegisterNewUser)
    if wantRegisterNewUser == '0':
      return False
    else:
      name = stringInput([
        'Digite seu nome.'
      ])
      return name