from view.userView import UserView

isRunning = True
user = UserView()

while isRunning:
  isRunning = user.getNextAction()