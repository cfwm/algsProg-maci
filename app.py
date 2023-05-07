from controller.login import doLogin


isRunning = True

while isRunning:
  print('Bem vindo ao Mapa Ambiental Colaborativo e Interativo!')
  user = doLogin()
  
  if user == 'exit':
    print('EXIT')
    isRunning = False
  else:
    print('user', user)
    print('Tchau')
    isRunning = False
