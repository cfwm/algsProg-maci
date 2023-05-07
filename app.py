from controller.login import doLogin


isRunning = True

while isRunning:
  print('Bem vindo ao Mapa Ambiental Colaborativo e Interativo!')
  user = doLogin()
  
  if user == 'exit':
    print('exiting app')
    isRunning = False
  else:
    print('user', user)
    print('Olá', user['name'])
    
    print('Tchau')
    isRunning = False
