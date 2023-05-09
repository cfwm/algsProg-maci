from dataBase.read import readDB
from dataBase.write import writeDB
from time import time
from utils.id.uuid import getNewId

class UserModel():
  def __init__(self):
    None

  def getUsersDict(self):
    return readDB('user')
  
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

def readOccurrences():
  return readDB('occurrence')

def readOccurrenceById(id):
  occurrences = readOccurrences()
  if id in occurrences:
    return occurrences[id]
  else:
    return None

def readOccurrencesByUser(user):
  occurrences = readOccurrences()
  result = list()
  for occurrence in occurrences:
    if occurrence['createdBy'] == user:
      result.append(occurrence)
  return result

def readAllOccurrences(user):
  occurrences = readOccurrences()
  result = list()
  for occurrence in occurrences:
      result.append(occurrence)
  return result