def stringInput(texts: list[str]) -> str:
  inputText = str()
  for text in texts:
    inputText = inputText + '\n' + text
  inputText = inputText + '\n===> '
  inputValue = str(input(inputText))
  return inputValue