from models.occurrenceModel import OccurrenceModel

class OccurrenceController(OccurrenceModel):
  def __init__(self):
    None
  
  def addUser(self, id: str, name: str, email: str):
    return self.createUser(id, name, email)
  
  def checkIsValidUser(self, id: str) -> dict | None:
    users = self.getUsersDict()
    if id in users:
      return users[id]
    else:
      None