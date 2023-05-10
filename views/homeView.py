from views.components.inputs import stringInput

class HomeView():
  def __init__(self):
    None

  def home(self, user: object) -> bool:
    print('HOME user', user)
    name = ''
    if 'name' in user:
      name = user['name']

    command = self.__inputValidCommand(name)
    print('exec command', command)
    if command == '0':
      print('TCHAU')
      return {
        'success': False
      }
    else:
      print('Vamos lá...')
      # __homeMapper(currentAction, command)
      # return {
      #   'success': True
      # }
      return {
        'success': False
      }
    
  def __inputValidCommand(self, name) -> str:
    print('__inputValidCommand name',name)
    command = stringInput([
      'Olá, ' + name,
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
        '  6 para listar denúncias;',
        '  7 para listar denúncias cadastradas por você;',
        '  5 para criar uma prática sustentável;',
        '  8 para criar uma denúncia;',
        '  0 para sair do programa.',
      ])
      isValidCommand = command in validCommands
      print('__inputValidCommand command',command)
    return command

  def __homeMapper(self, command: str) -> None:
      return {
        '1': 'listOccurrences',
        '2': 'listUserOccurrences',
        '3': 'listSustainablePracticeOccurrences',
        '4': 'listUserSustainablePracticeOccurrences',
        '5': 'listcomplaintOccurrences',
        '6': 'listUsercomplaintOccurrences',
        '7': 'createSustainablePracticeOccurrence',
        '8': 'createComplaintOccurrence',
      }[command]
      # actions = {
      #   '1': 'listOccurrences',
      #   '2': 'listUserOccurrences',
      #   '3': 'listSustainablePracticeOccurrences',
      #   '4': 'listUserSustainablePracticeOccurrences',
      #   '5': 'listcomplaintOccurrences',
      #   '6': 'listUsercomplaintOccurrences',
      #   '7': 'createSustainablePracticeOccurrence',
      #   '8': 'createComplaintOccurrence',
      # }
      # currentAction = actions[command]