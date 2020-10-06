#This is the 'Guess the vegetable' minigame combined with the 'Guess the animal'
#sample script, which has been slightly modified, to make them into one program.
print("Welcome to guess the vegetable or animal!")
print("Please pick from ostrich, lion or whale, OR")
print("Please pick from broccoli, peas, carrot or sweetcorn!")
print("I will attempt to guess your choice.")
print("Please enter y or n for your answers (i.e. yes or no),")
print("otherwise this program will not work properly.")
print("Is your choice an animal?")
answer = input().lower()
if answer == "n":
  print("Is it green?")
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
elif answer == "y":
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