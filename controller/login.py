from validators.email import checkIsValidEmail
from db.user import readUserById
from utils.hash.md5 import getHash
from model.user import User

def doLogin():
  validEmail = checkIsValidEmail()
  if not validEmail:
    return 'exit'

  hash = getHash(validEmail)
  user = readUserById(hash)
  if user == None:
    registerNewUser = int(input('Usuário não cadastrado.\nDigite 1 para criar um novo usuário e 2 para sair: '))
    while registerNewUser != 1 and registerNewUser != 2:
      registerNewUser = int(input('Comando inválido.\nDigite 1 para criar um novo usuário e 2 para sair: '))
    if registerNewUser == 2:
      return 'exit'
    else:
      email = validEmail
      name = str(input('Digite seu nome: '))
      user = User()
      user.create(name, email)
      return user.read()
  else:
    return user