# Journey Challenge:
# Create your own survival story by being creative in your story telling and create ways of surviving your simulation!
# Input at least 10 key-value pairs in your new dictionary and have more than 2 tool to help you survive!
# Make sure the conditions match with the bad and good decision making behind the template!

# BONUS: Create a functions within the program to make it more efficient and clean!


# dictionary for the tools
options = {
  "put in shopping bag": "A",
  "keys": "B",
  "wallet":"C",
  "pay the fee": "D",
  "buy": "E",
  "the sense to decline": "F",
  "hand":"G",
  "run": "H",
  "read your mothers note": "I"
}

print("Welcome to the journey simulator to choose options to win and escape! \n")
print("------------------------------------------------------------------------")
print("It's Saturday. Your mother tasked you with getting the ingredients for dinner.") 
print("As you are not the brightest crayon in the box, she wrote you very specific instructions on what to buy at the market.") 
print("Please safely navigate the journey to the market, obtain the correct items and make your mother proud.")
print("You about to exit the house. What do you grab on the way out?" )

values = options.values()
continuePrompts = False
# Get all key-value pairs
items = options.items()

# Print each key-value pair
for key, value in items:
  print(f"{value}: {key}")

print("Choose your option")
userChoices = input("Insert the letters you want to choose with no spaces but with a comma between each letter: ")
userList = list(userChoices.split(','))

# create a variable that holds on to the correct amount of tools needed to win the game
correctItems = 2

# each condition where if the right items aren't chosen, you describe the reason why you need it
if "B" not in userList:
  print("How are you going to get back into your house? \n")
if "C" not in userList:
  print("How are you going to pay? \n")

# condition where you will the right choices were there BUT there are other options that were chosen
if ("C" in userList and "B" in userList):
    if len(userList) == correctItems:
        continuePrompts = True
        print("You have chosen the right items to leave with! \n")
    else:
        print("You have chosen the right items to leave with BUT too many items! \n")
  # nested condition where you will win the game if you have the right tools 
else:
  print("You have chosen the wrong items to leave with, try again! \n")

  
print("A ball rolls towards you and the neighborhood children invite you to play. What do you do? \n")
for key, value in items:
  print(f"{value}: {key}")
userChoices = input("Insert the letters you want to choose with no spaces but with a comma between each letter: ")
userList = list(userChoices.split(','))
correctItems = 1

if continuePrompts == True:
    if "F" not in userList:
        print("Be serious. Don't you have somewhere to be? \n")
        continuePrompts == False
  #how does this work??? 
    if "F" in userList and len(userList) == correctItems:
        print("Good job! Onwards to the market. \n")
    # nested condition where you will win the game if you have the right tools 
    else:
        print("There is only one answer, try again! \n")
        continuePrompts == False

print("You have made it to the market. Do you remember what you are here for? If not, pull out the instructions note from your mother \n")

yesOrNo = input("Reply yes or no ")

if yesOrNo == "yes":
    print("Okay.... go buy those exact items then...")
else:
    print("Good choice. Your note reads that you need to purchase chicken, yams and packets of soup mix")
