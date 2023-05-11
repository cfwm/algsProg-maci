from views.loginView import LoginView
from views.homeView import HomeView
from views.occurrenceView import OccurrenceView

class Route(LoginView, HomeView, OccurrenceView):
  def __init__(self):
    super().__init__()
    # None

  def next(self, route: str, user: object) -> bool:
    print('++++ ROUTE next ++++\n')
    response = None
    match route:
      case 'login':
        response = self.login()
      case 'home':
        response = self.home(user)
      case 'listOccurrences':
        response = self.listOccurrences()
      case 'listOccurrencesByUser':
        response = self.listOccurrencesByUser(user)
      case 'listSustainablePracticeOccurrences':
        response = self.listOccurrencesByType('sustainablePractice')
      case 'listUserSustainablePracticeOccurrences':
        response = self.listOccurrencesByUserAndType(user, 'sustainablePractice')
      case 'listcomplaintOccurrences':
        response = self.listOccurrencesByType('complaint')
      case 'listUsercomplaintOccurrences':
        response = self.listOccurrencesByUserAndType(user, 'complaint')
      case 'createSustainablePracticeOccurrence':
        response = self.newOccurrence(user, 'sustainablePractice')
      case 'createComplaintOccurrence':
        response = self.newOccurrence(user, 'complaint')
    return response