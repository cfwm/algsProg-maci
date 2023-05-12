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
      'createdAt': 'Data de cadastro'
    }
    for i in range(len(fields)):
      if fields[i] == 'type':
        print(fieldTypeTranslateMapper[fields[i]] + ': ' + occurrenceTypeTranslateMapper[occurrence[fields[i]]])  
      elif fields[i] == 'createdAt':
        day = occurrence[fields[i]][0:10].split('-')[2]
        month = occurrence[fields[i]][0:10].split('-')[1]
        year = occurrence[fields[i]][0:10].split('-')[0]
        print(fieldTypeTranslateMapper[fields[i]] + ': ' + day + '/' + month + '/' + year)
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
