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

  def readOccurrences(self):
    return readDB('occurrence')

  def readOccurrencesByUser(self, userId):
    occurrences = self.readOccurrences()
    result = list()
    for occurrence in occurrences:
      if occurrence['createdBy'] == userId:
        result.append(occurrence)
    return result

  def readOccurrencesByType(self, type):
    occurrences = self.readOccurrences()
    result = list()
    for occurrence in occurrences:
      if occurrence['type'] == type:
        result.append(occurrence)
    return result

  def readOccurrencesList(self):
    occurrences = self.readOccurrences()
    result = list()
    for occurrence in occurrences:
        result.append(occurrence)
    return result
  
  def readOccurrencesByUserAndType(self, userId, type):
    occurrences = self.readOccurrences()
    result = list()
    for occurrence in occurrences:
      if occurrence['type'] == type and occurrence['createdBy'] == userId:
        result.append(occurrence)
    return result