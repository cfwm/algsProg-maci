def printOccurrencesList(title, noItemsText, occurrences, fields, users):
  def printOccurrenceField(occurrence, fields):
    occurrenceTypeTranslateMapper = {
      'sustainablePractice': 'prática sustentável',
      'complaint': 'denúncia',
    }
    fieldTypeTranslateMapper = {
      'id': 'Id',
      'type': 'Tipo',
      'name': 'Nome',
      'description': 'Descrição',
    }
    for i in range(len(fields)):
      if fields[i] == 'type':
        print(fieldTypeTranslateMapper[fields[i]] + ': ' + occurrenceTypeTranslateMapper[occurrence[fields[i]]])  
      else:
        print(fieldTypeTranslateMapper[fields[i]] + ': ' + occurrence[fields[i]])

  print('\n### ' + title + ' ###\n')
  if len(occurrences) > 0:
    for i in range(len(occurrences)):
      print(i + 1, ':')
      printOccurrenceField(occurrences[i], fields)
      if users:
        userName = users[occurrences[i]['createdBy']]['name']
        print('Autore: ', userName)
  else:
    print(noItemsText)
  print('\n#########\n')
