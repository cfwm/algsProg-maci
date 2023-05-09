import csv
from dataBase.write import createTable, isTableExistent
from dataBase.utils import getTable

def readDB(kind):
  table = getTable(kind)
  if not isTableExistent(table):
    createTable(kind)

  with open(table, 'r') as file:
    csv_file = csv.DictReader(file)
    result = dict()
    for row in csv_file:
      id = dict(row)['id']
      result[id] = dict(row)
    return result