

# functions go here...
def yes_no(question):
  valid = False
  while not valid:
    response = input(question).lower()
    
    if display_instructions == "yes" or display_instructions == "y":
     response = "yes"
     return response
  
    elif display_instructions == "no" or display_instructions == "n":
     response = "no"
     return response

    else:
      print("Please answer yes / no")

def instructions():
  print("**** how to Play ****")
  print()
  print("The rules of the game go here")
  print()
  return ""

  # main routine goes here...
  played_before = yes_no("have you played the " 
  "game before")
  print("you chose {}".format(display_instructions)):
  print()
  having_fun = yes_no("are you having fun? ")
  print("you said {} to having fun".format(having_fun))

  display_instructions = ""
  while display_instructions.lower() != "xxx":
  # ask the user if they have played before
    display_instructions = input("have you played this game" "before?").lower()

  # If they say yes, output 'program continues'
  # If they say no, output 'display instructions'
  # If the answer is invalid, print an error.