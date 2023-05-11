import csv
from dataBase.write import createTable, isTableExistent
from dataBase.utils import getTable

def readDB(kind):
  table = getTable(kind)
  if not isTableExistent(table):
    createTable(kind)

  with open(table, 'r') as file:
    csv_file = csv.DictReader(file)
    result = formatDBResult(kind, csv_file)
    return result
  
def formatDBResult(kind, csvFile):
  if kind == 'user':
    return formatBDDict(csvFile)
  elif kind == 'occurrence':
    return formatBDList(csvFile)
  
def formatBDDict(csvFile):
  result = dict()
  for row in csvFile:
    id = dict(row)['id']
    result[id] = dict(row)
  return result

def formatBDList(csvFile):
  result = list()
  for row in csvFile:
    result.append(dict(row))
  return result