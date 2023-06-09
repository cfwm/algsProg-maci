from views.components.inputs import stringInput

class HomeView():
  def __init__(self):
    None

  def home(self, user) -> bool:
    response = {
      'isRunning': False,
      'route': 'login',
      'user': None,
    }
    name = 'Nameless'
    if user and 'name' in user:
      response['user'] = user
      name = user['name']

    command = self.__inputValidCommand(name)
    if command != '0':
      response['isRunning'] = True
      response['route'] = self.__homeMapper(command)
    return response
    
  def __inputValidCommand(self, name) -> str:
    command = stringInput([
      'Olá, ' + name,
      'Digite:',
      '  1 para listar todas as ocorrências;',
      '  2 para listar todas as ocorrências cadastradas por você;',
      '  3 para listar práticas sustentáveis;',
      '  4 para listar práticas sustentáveis cadastradas por você;',
      '  5 para listar denúncias;',
      '  6 para listar denúncias cadastradas por você;',
      '  7 para criar uma prática sustentável;',
      '  8 para criar uma denúncia;',
      '  0 para sair do programa.',
    ])
    validCommands = { '0', '1', '2', '3', '4', '5', '6', '7', '8' }
    isValidCommand = command in validCommands
    while not isValidCommand:
      command = stringInput([
        'Comando inválido.',
        'Digite:',
        '  1 para listar todas as ocorrências;',
        '  2 para listar todas as ocorrências cadastradas por você;',
        '  3 para listar práticas sustentáveis;',
        '  4 para listar práticas sustentáveis cadastradas por você;',
        '  5 para listar denúncias;',
        '  6 para listar denúncias cadastradas por você;',
        '  7 para criar uma prática sustentável;',
        '  8 para criar uma denúncia;',
        '  0 para sair do programa.',
      ])
      isValidCommand = command in validCommands
      print('__inputValidCommand command',command)
    return command

  def __homeMapper(self, command: str) -> str:
    return {
      '1': 'listOccurrences',
      '2': 'listOccurrencesByUser',
      '3': 'listSustainablePracticeOccurrences',
      '4': 'listUserSustainablePracticeOccurrences',
      '5': 'listcomplaintOccurrences',
      '6': 'listUsercomplaintOccurrences',
      '7': 'createSustainablePracticeOccurrence',
      '8': 'createComplaintOccurrence',
    }[command]
