from routes.route import Route

class App(Route):
  def __init__(self):
    super().__init__()
    print('Bem vindo ao Mapa Ambiental Colaborativo e Interativo!')
    self.isRunning = True
    self.route = 'login'
    self.user = None

  def exec(self):
    print('\n1 APP exec')
    request = self.__requestHandler()
    print('## request ##\n',request)
    self.__responseHandler(request)
    return self.isRunning
  
  def __requestHandler(self):
    request = self.next(self.route, self.user)
    print('===> REQUEST <===\n',request)
    return request

  def __responseHandler(self, request):
    print('===> RESPONSE <===\n')
    print('RESPONSE request',request)
    if 'isRunning' in request:
      self.isRunning = request['isRunning']
    if 'route' in request:
      self.route = request['route']
    if 'user' in request:
      self.user = request['user']
    

