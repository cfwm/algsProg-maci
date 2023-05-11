from validators.email import checkIsValidEmail

def stringInput(texts: list[str]) -> str:
  inputText = str()
  for text in texts:
    inputText = inputText + '\n' + text
  inputText = inputText + '\n===> '
  inputValue = str(input(inputText))
  return inputValue

def inputValidEmail() -> bool | str:
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


def inputNewUserName() -> bool | str:
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