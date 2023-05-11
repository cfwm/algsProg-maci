from models.occurrenceModel import OccurrenceModel

class OccurrenceController(OccurrenceModel):
  def __init__(self):
    None

  def addOccurrence(self, 
    type: str,
    name: str,
    description: str,
    userId: str,
  ):
    return self.createOccurrence(type, name, description, userId)

  def getOccurrences(self):
    occurrences = self.readOccurrencesList()
    return occurrences
  
  def getOccurrencesByUser(self, userId):
    occurrences = self.readOccurrencesDict()
    result = list()
    for occurrence in occurrences:
      if occurrence['createdBy'] == userId:
        result.append(occurrence)
    return result

  def getOccurrencesByType(self, type):
    occurrences = self.readOccurrencesDict()
    result = list()
    for occurrence in occurrences:
      if occurrence['type'] == type:
        result.append(occurrence)
    return result
  
  def getOccurrencesByUserAndType(self, userId, type):
    occurrences = self.readOccurrencesDict()
    result = list()
    for occurrence in occurrences:
      if occurrence['type'] == type and occurrence['createdBy'] == userId:
        result.append(occurrence)
    return result

