#This is the 'Guess the vegetable' minigame combined with the 'Guess the animal'
#sample script, which has been slightly modified, to make them into one program.
print("Welcome to guess the vegetable or animal!")
print("Please pick from ostrich, lion or whale, OR")
print("Please pick from broccoli, peas, carrot or sweetcorn!")
print("I will attempt to guess your choice.")
print("Please enter y or n for your answers (i.e. yes or no),")
print("otherwise this program will not work properly.")
print("Is your choice an animal?")
first = input().lower()
if first == "n":
  print("Is it green?")
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
elif first == "y":
  print("Does the animal live in the water?")
  answer = input().lower()
  if answer == "n":
    print("Does the animal have wings?")
    answer = input().lower()
    if answer == "y":
       print("It must be an ostrich!")
    elif answer == "n":
       print("It must be a lion!")
  elif answer == "y":
   print("It must be a whale!")