from controllers.occurrenceController import OccurrenceController

class OccurrenceView(OccurrenceController):
  def __init__(self):
    None

  def listOccurrences(self):
    print('Lista de Ocorrências:')
    occurrences = self.getOccurrences()
    if len(occurrences) > 0:
      for i in range(len(occurrences)):
        print(i + 1, ': ', occurrences[i])
    else:
      print('Nenhuma ocorrência cadastrada.\n')
    return {
      'isRunning': True,
      'route': 'home',
    }
  # def updateUser(self)
    
  
  # def createComplaintOccurrence(self) -> bool:
