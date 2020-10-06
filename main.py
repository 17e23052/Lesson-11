#This is a 'Guess the vegetable' minigame.
print("Welcome to guess the vegetable!")
print("Please pick from broccoli, peas, carrot or sweetcorn!")
print("I will attempt to guess your choice.")
print("Please enter y or n for your answers (i.e. yes or no),")
print("otherwise this program will not work properly.")
print("Is the vegetable green?")
green = input().lower()
if green == "y":
  print("Does it look like a tree?")
  tree = input().lower()
  if tree == "y":
    print("It must be broccoli!")
  elif tree == "n":
    print("It must be peas!")
elif green == "n":
  print("Is it orange?")
  orange = input().lower()
  if orange == "y":
    print("It must be a carrot!")
  elif orange == "n":
    print("It must be sweetcorn!")