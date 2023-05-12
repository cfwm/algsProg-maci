from controllers.occurrenceController import OccurrenceController
from controllers.userController import UserController
from views.components.outputs import printOccurrencesList
from views.components.inputs import inputOccurence

class OccurrenceView(OccurrenceController, UserController):
  def __init__(self):
    None

  def listOccurrences(self):
    occurrences = self.getOccurrences()
    users = self.getUsersDict()
    printOccurrencesList(
      'Lista de ocorrências',
      'Nenhuma ocorrência cadastrada.',
      occurrences,
      ['id', 'type', 'name', 'description', 'createdAt'],
      users
    )
    return {
      'isRunning': True,
      'route': 'home',
    }
  
  def listOccurrencesByUser(self, user):
    occurrences = self.getOccurrencesByUser(user['id'])
    printOccurrencesList(
      'Lista de ocorrências cadastradas por ' + user['name'],
      'Nenhuma ocorrência cadastrada.',
      occurrences,
      ['id', 'type', 'name', 'description', 'createdAt'],
      None
    )
    return {
      'isRunning': True,
      'route': 'home',
    }

  def listOccurrencesByType(self, type):
    occurrences = self.getOccurrencesByType(type)
    users = self.getUsersDict()
    titleText = 'Lista de práticas sustentáveis'
    noItemsText = 'Nenhuma prática sustentável cadastrada.'
    if type == 'complaint':
      titleText = 'Lista de denúncias'
      noItemsText = 'Nenhuma denúncia cadastrada.'
    printOccurrencesList(
      titleText,
      noItemsText,
      occurrences,
      ['id', 'name', 'description', 'createdAt'],
      users
    )
    return {
      'isRunning': True,
      'route': 'home',
    }

  def listOccurrencesByUserAndType(self, user, type):
    occurrences = self.getOccurrencesByUserAndType(user['id'], type)
    titleText = 'Lista de práticas sustentáveis cadastradas por ' + user['name'] + ':'
    noItemsText = 'Nenhuma prática sustentável cadastrada.'
    if type == 'complaint':
      titleText = 'Lista de denúncias cadastradas por ' + user['name'] + ':'
      noItemsText = 'Nenhuma denúncia cadastrada'
    printOccurrencesList(
      titleText,
      noItemsText,
      occurrences,
      ['id', 'name', 'description', 'createdAt'],
      None
    )
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
    name = inputOccurence('name')
    description = inputOccurence('description')
    occurrence = self.addOccurrence(type, name, description, user['id'])
    print('Ocorrência ' + occurrence['name'] + ' cadastrada.')
    return {
      'isRunning': True,
      'route': 'home',
    }

