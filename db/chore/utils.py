def getFieldNames(kind):
  match kind:
    case 'user':
      return ['email', 'name', 'id', 'occurrences']
    case 'occurrence':
      return ['type', 'name', 'description', 'initialDate', 'endDate', 'createdAt', 'createdBy']
    # case 'denouncement':
    #   return ['name', ]
    # case 'joint-effort':
    #   return []
    # case 'good-practice':
    #   return []

def getTable(kind):
  match kind:
    case 'user':
      return 'users.csv'
    case 'occurrence':
      return 'occurrences.csv'