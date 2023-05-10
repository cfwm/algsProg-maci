from routes.route import Route

class App(Route):
  def __init__(self):
    print('Bem vindo ao Mapa Ambiental Colaborativo e Interativo!')

  def exec(self, route: str, user: object):
    print('\n1 APP exec')
    request = self.__requestHandler(route, user)
    print('request',request)
    # return self.__responseHandler({route, request})
    response = self.__responseHandler(request, user)
    print('response', response)

    return response
  
  def __requestHandler(self, route: str, user: object):
    return self.next(route, user)

  def __responseHandler(self, request, user):
    updatedUser = user
    if 'updatedUser' in request:
      updatedUser = request['updatedUser']
    return {
      'success': request['success'],
      'nextRoute': request['nextRoute'],
      'user': updatedUser
    }
    

