from view.components.inputs import stringInput
from validators.email import checkIsValidEmail
from utils.hash.md5 import getHash
from controller.userController import UserController

class UserView():
  def __init__(self):
    print('Bem vindo ao Mapa Ambiental Colaborativo e Interativo!')
    self.currentAction = 'login'

  def getNextAction(self) -> bool:
    actionsMapper = {
      "login": self.login(),
      "mainMenu": self.mainMenu(),
      # "listOccurrences": self.listOccurrences(),
      # "listUserOccurrences": self.listUserOccurrences(),
      # "listSustainablePracticeOccurrences": self.listSustainablePracticeOccurrences(),
      # "listUserSustainablePracticeOccurrences": self.listUserSustainablePracticeOccurrences(),
      # "listcomplaintOccurrences": self.listcomplaintOccurrences(),
      # "listUsercomplaintOccurrences": self.listUsercomplaintOccurrences(),
      # "createSustainablePracticeOccurrence": self.createSustainablePracticeOccurrence(),
      "createcomplaintOccurrence": self.createcomplaintOccurrence(),
    }
    print('self.currentAction',self.currentAction)
    return actionsMapper[self.currentAction]

  def getValidEmail(self) -> bool | str:
    email = stringInput([
      'Digite seu e-mail para continuar.',
    ])
    isValidEmail = checkIsValidEmail(email)
    while not isValidEmail:
      email = stringInput([
        'E-mail inválido.',
        'Digite um e-mail válido ou', 
        'digite 1 para sair do programa.',
      ])
      if email == '1':
        return False
      else:
        isValidEmail = checkIsValidEmail(email)
    return email
  
  def checkWantsRegisterNewUser(self) -> bool | str:
    wantRegisterNewUser = stringInput([
      'Usuário não cadastrado. Digite:',
      '  1 para criar um novo usuário;',
      '  0 para sair.',
    ])
    while wantRegisterNewUser != '1' and wantRegisterNewUser != '2':
      wantRegisterNewUser = stringInput([
        'Comando inválido. Digite:',
        ' 1 para criar um novo usuário',
        ' 0 para sair.',
      ])    
    if wantRegisterNewUser == '2':
      return False
    else:
      name = stringInput([
        'Digite seu nome.'
      ])
      return name

  def login(self) -> bool:
    email = self.getValidEmail()
    if not email:
      return False
    
    id = getHash(email)
    self.controller = UserController()
    validUser = self.controller.checkIsValidUser(id)
    if not validUser:
        newUserName = self.checkWantsRegisterNewUser()
        if not newUserName:
          return False
        else:
          newUser = self.controller.createUser(id, newUserName, email)
          if not newUser:
            return False
          else:
            self.id = newUser['id']
            self.name = newUser['name']
            self.email = newUser['email']
            self.occurrences = newUser['occurrences']
            self.createdAt = newUser['createdAt']
            self.currentAction = 'mainMenu'
            return True
    else:
      self.id = validUser['id']
      self.name = validUser['name']
      self.email = validUser['email']
      self.occurrences = validUser['occurrences']
      self.createdAt = validUser['createdAt']
      self.currentAction = 'mainMenu'
      return True

  def checkIsValidCommand(self, action: str, command: str) -> bool:
    validCommandsBy = {
      'mainMenu': ['0', '1', '2', '3', '4', '5', '6', '7', '8'],
    }
    return validCommandsBy[action].count(command) == 1

  def getMainMenuValidCommand(self) -> str:
    command = stringInput([
      'Olá, ' + self.name,
      'Digite:',
      '  1 para listar todas as ocorrências;',
      '  2 para listar todas as ocorrências cadastradas por você;',
      '  3 para listar práticas sustentáveis;',
      '  4 para listar práticas sustentáveis cadastradas por você;',
      '  5 para criar uma prática sustentável;',
      '  6 para listar denúncias;',
      '  7 para listar denúncias cadastradas por você;',
      '  8 para criar uma denúncia;',
      '  0 para sair do programa.',
    ])
    isValidCommand = self.checkIsValidCommand('mainMenu', command)
    while not isValidCommand:
      command = stringInput([
        'Comando inválido.',
        'Digite:',
        '  1 para listar todas as ocorrências;',
        '  2 para listar todas as ocorrências cadastradas por você;',
        '  3 para listar práticas sustentáveis;',
        '  4 para listar práticas sustentáveis cadastradas por você;',
        '  6 para listar denúncias;',
        '  7 para listar denúncias cadastradas por você;',
        '  5 para criar uma prática sustentável;',
        '  8 para criar uma denúncia;',
        '  0 para sair do programa.',
      ])
      isValidCommand = self.checkIsValidCommand('mainMenu', command)
    return command

  def setCurrentActionFromMainMenu(self, command: str) -> None:
    actions = {
      '1': 'listOccurrences',
      '2': 'listUserOccurrences',
      '3': 'listSustainablePracticeOccurrences',
      '4': 'listUserSustainablePracticeOccurrences',
      '5': 'listcomplaintOccurrences',
      '6': 'listUsercomplaintOccurrences',
      '7': 'createSustainablePracticeOccurrence',
      '8': 'createcomplaintOccurrence',
    }
    self.currentAction = actions[command]

  def mainMenu(self) -> bool:
    command = self.getMainMenuValidCommand()
    print('mainMenu command', command)
    if command == '0':
      print('TCHAU')
      return False
    else:
      print('Vamos lá...')
      # self.setCurrentActionFromMainMenu(command)
      # return True
      return False
    
  # def listOccurrences(self) -> bool:
  # def listUserOccurrences(self) -> bool:
  # def listSustainablePracticeOccurrences(self) -> bool:
  # def listUserSustainablePracticeOccurrences(self) -> bool:
  # def listcomplaintOccurrences(self) -> bool:
  # def listUsercomplaintOccurrences(self) -> bool:
  # def createSustainablePracticeOccurrence(self) -> bool:
  
  # def createcomplaintOccurrence(self) -> bool:
