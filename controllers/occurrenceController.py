from models.occurrenceModel import OccurrenceModel

class OccurrenceController(OccurrenceModel):
  def __init__(self):
    None

  def getOccurrences(self):
    occurrences = self.readOccurrencesList()
    return occurrences
  
  def addOccurrence(self, 
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
    userId: str,
  ):
    return self.createOccurrence(
      type,
      name,
      description,
      region,
      city,
      street,
      number,
      neighborhood,
      country, 
      initialDate,
      endDate,
      userId,
    )


  
