from views.loginView import LoginView
from views.homeView import HomeView

class Route(LoginView, HomeView):
  def __init__(self):
    super(LoginView, HomeView).__init__()
    print('\n2 ROUTE INIT')
    None

  # def getNextAction(self, route: str) -> bool:
  def next(self, route: str, user: object) -> bool:
    print('\nROUTE next,')
    print('route',route)
    print('user',user)
    mapper = {
      "login": self.login(),
      "home": self.home(user),
      # "listOccurrences": self.listOccurrences(),
      # "listUserOccurrences": self.listUserOccurrences(),
      # "listSustainablePracticeOccurrences": self.listSustainablePracticeOccurrences(),
      # "listUserSustainablePracticeOccurrences": self.listUserSustainablePracticeOccurrences(),
      # "listcomplaintOccurrences": self.listcomplaintOccurrences(),
      # "listUsercomplaintOccurrences": self.listUsercomplaintOccurrences(),
      # "createSustainablePracticeOccurrence": self.createSustainablePracticeOccurrence(),
      # "createComplaintOccurrence": self.createComplaintOccurrence(),
    }

    # print('mapper[route]', not route in mapper)
    # if not route in mapper:
    #   return False
    return mapper[route]

  # def getNextAction(route: str, command: str) ->: