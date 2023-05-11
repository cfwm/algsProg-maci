from dataBase.read import readDB
from dataBase.write import writeDB
from time import time
from utils.id.uuid import getNewId

class OccurrenceModel():
  def __init__(self):
    None

  def getOccurrenceDict(self):
    return readDB('occurrence')
  
  def createOccurrence(self,
    type: str,
    name: str,
    description: str,
    region: str,
    city: str,
    street: str,
    number: str,
    neighborhood: str,
    country: str, 
    initialDate: str,
    endDate: str,
    createdBy: str
  ): 
    ocurrenceData = {
      'id': getNewId(),
      'type': type,
      'name': name,
      'description': description,
      'region': region,
      'city': city,
      'street': street,
      'number': number,
      'neighborhood': neighborhood,
      'country': country ,
      'initialDate': initialDate,
      'endDate': endDate,
      'createdAt': time(),
      'createdBy': createdBy,
    }
    writeDB('occurrence', ocurrenceData)
    return ocurrenceData

  def readOccurrencesDict(self):
    return readDB('occurrence')

  def readOccurrenceById(self, id):
    occurrences = self.readOccurrencesDict()
    if id in occurrences:
      return occurrences[id]
    else:
      return None

  def readOccurrencesByUser(self, user):
    occurrences = self.readOccurrencesDict()
    result = list()
    for occurrence in occurrences:
      if occurrence['createdBy'] == user:
        result.append(occurrence)
    return result

  def readOccurrencesByType(self, type):
    occurrences = self.readOccurrencesDict()
    result = list()
    for occurrence in occurrences:
      if occurrence['type'] == type:
        result.append(occurrence)
    return result

  def readOccurrencesList(self):
    occurrences = self.readOccurrencesDict()
    result = list()
    for occurrence in occurrences:
        result.append(occurrence)
    return result