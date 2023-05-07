import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def isValid(email):
  if re.fullmatch(regex, email):
    return True
  else:
    return False
  
def checkIsValidEmail():
  email = str(input('Digite seu e-mail para continuar: '))
  isValidEmail = isValid(email)
  while not isValidEmail:
    email = str(input('E-mail inválido.\nDigite um e-mail válido ou "s" para sair do programa: '))
    if email == 's':
      return False
    isValidEmail = isValid(email)
  return email