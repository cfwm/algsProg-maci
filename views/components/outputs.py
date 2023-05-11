def listOutput(titleText: str, noItemsText: str, items: list[str]) -> None:
  print('\n\n\n+++++++++>')
  print(titleText)
  if len(items) > 0:
    for i in range(0, len(items)):
      print(items[i])
  else:
    print(noItemsText)
  print('<+++++++++\n\n\n')