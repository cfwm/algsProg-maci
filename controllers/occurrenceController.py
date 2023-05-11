from models.occurrenceModel import OccurrenceModel

class OccurrenceController(OccurrenceModel):
  def __init__(self):
    None

  def getOccurrences(self):
    occurrences = self.readOccurrencesList()
    return occurrences
  
  def addOccurrence(self, 
    type: str,
    name: str,
    description: str,
    userId: str,
  ):
    return self.createOccurrence(type, name, description, userId)


  
