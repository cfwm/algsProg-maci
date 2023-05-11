from controllers.occurrenceController import OccurrenceController
from views.components.outputs import listOutput
from views.components.inputs import stringInput

class OccurrenceView(OccurrenceController):
  def __init__(self):
    None

  def listOccurrences(self):
    occurrences = self.getOccurrences()
    print('Lista de ocorrências:')
    if len(occurrences) > 0:
      for i in range(len(occurrences)):
        print(i + 1, ': ', occurrences[i])
    else:
      print('Nenhuma ocorrência cadastrada.')
    return {
      'isRunning': True,
      'route': 'home',
    }
  
  def listOccurrencesByUser(self, user):
    occurrences = self.getOccurrencesByUser(user['id'])
    titleText = 'Lista de ocorrências cadastradas por ' + user['name'] + ':'
    noItemsText = 'Nenhuma ocorrência cadastrada.'
    listOutput(titleText, noItemsText, occurrences)
    return {
      'isRunning': True,
      'route': 'home',
    }

  def listOccurrencesByType(self, type):
    occurrences = self.getOccurrencesByType(type)
    titleText = 'Lista de práticas sustentáveis'
    noItemsText = 'Nenhuma prática sustentável cadastrada.'
    if type == '2':
      titleText = 'Lista de denúncias'
      noItemsText = 'Nenhuma denúncia cadastrada.'
    listOutput(titleText, noItemsText, occurrences)
    return {
      'isRunning': True,
      'route': 'home',
    }

  def listOccurrencesByUserAndType(self, user, type):
    occurrences = self.getOccurrencesByUserAndType(user['id'], type)
    titleText = 'Lista de práticas sustentáveis cadastradas por ' + user['name'] + ':'
    noItemsText = 'Nenhuma prática sustentável cadastrada por ' + user['name'] + ':'
    if type == '2':
      titleText = 'Lista de denúncias cadastradas por ' + user['name'] + ':'
      noItemsText = 'Nenhuma denúncia cadastrada por ' + user['name'] + ':'
    listOutput(titleText, noItemsText, occurrences)
    return {
      'isRunning': True,
      'route': 'home',
    }

  def newOccurrence(self, user, type: str):
    occurrenceMapper = {
      'sustainablePractice': 'prática sustentável',
      'complaint': 'denúncia',
    }
    print('Cadastro de ' + occurrenceMapper[type])
    name = self.__inputOccurence('name')
    description = self.__inputOccurence('description')
    occurrence = self.addOccurrence(type, name, description, user['id'])
    print('Ocorrência ' + occurrence['name'] + ' cadastrada.')
    return {
      'isRunning': True,
      'route': 'home',
    }
  
  def __inputOccurence(self, field) -> str:
    titleMapper = {
      "name": "o nome",
      "description": "a descrição",
    }
    text = 'Informe ' + titleMapper[field] + ':'
    response = stringInput([text])
    return response
