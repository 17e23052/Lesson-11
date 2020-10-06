#This is a 'Guess the vegetable' minigame.
print("Welcome to guess the vegetable!")
print("Please pick from broccoli, peas, carrot or sweetcorn!")
print("I will attempt to guess your choice.")
print("Please enter y or n for your answers (i.e. yes or no),")
print("otherwise this program will not work properly.")
print("Is the vegetable green?")
answer = input().lower()
if answer == "y":
  print("Does it look like a tree?")
  answer = input().lower()
  if answer == "y":
    print("It must be broccoli!")
  elif answer == "n":
    print("It must be peas!")
elif answer == "n":
  print("Is it orange?")
  answer = input().lower()
  if answer == "y":
    print("It must be a carrot!")
  elif answer == "n":
    print("It must be sweetcorn!")