def getFieldNames(kind):
  match kind:
    case 'user':
      return ['id', 'email', 'name', 'occurrences', 'createdAt']
    case 'occurrence':
      return ['id', 'type', 'name', 'description', 'region', 'city', 'street', 'number', 'neighborhood', 'country',   'createdAt', 'createdBy']
# return ['type', 'name', 'description', 'region', 'city', 'street', 'number', 'neighborhood', 'country',   'initialDate', 'endDate', 'createdAt', 'createdBy']
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