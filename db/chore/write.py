import csv
import os.path
from db.chore.utils import getTable, getFieldNames 

def isTableExistent(table):
  r = os.path.isfile(table)
  return r

def writeDB(kind, payload):
  table = getTable(kind)
  fieldnames = getFieldNames(kind)

  if not isTableExistent(table):
    createTable(table)

  with open(table, 'a') as file:
    writer = csv.DictWriter(file, fieldnames = fieldnames)
    writer.writerow(payload)

def createTable(kind):
  table = getTable(kind)
  fieldnames = getFieldNames(kind)
  with open(table, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames = fieldnames)
    writer.writeheader()