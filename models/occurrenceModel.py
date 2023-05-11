from dataBase.read import readDB
from dataBase.write import writeDB
from time import time
from utils.id.uuid import getNewId

class OccurrenceModel():
  def __init__(self):
    None
  
  def createOccurrence(self,
    type: str,
    name: str,
    description: str,
    createdBy: str
  ): 
    ocurrenceData = {
      'id': getNewId(),
      'type': type,
      'name': name,
      'description': description,
      'createdAt': time(),
      'createdBy': createdBy,
    }
    writeDB('occurrence', ocurrenceData)
    return ocurrenceData

  def readOccurrencesDict(self):
    return readDB('occurrence')

  def readOccurrencesList(self):
    occurrences = self.readOccurrencesDict()
    result = list()
    for occurrence in occurrences:
        result.append(occurrence)
    return result
