from app import App

app = App()
isRunning = True
route = 'login'
user = None

while isRunning:
  response = app.exec(route, user)
  isRunning = response['success']
  route = response['nextRoute']
  user = response['user']
  print('response', response)
  print('isRunning', isRunning)
  print('route', route)