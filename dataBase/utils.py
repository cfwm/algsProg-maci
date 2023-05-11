def getFieldNames(kind):
  match kind:
    case 'user':
      return ['id', 'email', 'name', 'createdAt']
    case 'occurrence':
      return ['id', 'type', 'name', 'description', 'createdAt', 'createdBy']

# case occurrence.type = 'complaint' | sustainablePractice

def getTable(kind):
  match kind:
    case 'user':
      return 'users.csv'
    case 'occurrence':
      return 'occurrences.csv'