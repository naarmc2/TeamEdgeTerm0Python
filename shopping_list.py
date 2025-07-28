#********************************************************************
 #                                                                 
 #  Team Edge List Mini-project: THE SHOPPING LIST HELPER
 # 
 #  This project prompts users using input() to prompt users
 #  to add (or remove) items from a shopping list. It starts empty
 #  and each time the program is run it asks you to either add or 
 #  remove an item from the list. It also updates the user of its
 #  contents. The shopping list also checks to see if an item 
 #  is already present in the list and prevents you from adding it
 #  again, giving feedback along the way. 
 # 
 # ***************************************************************/

active = True

print("Welcome to Shopping List!")

welcome_message = "Hi! I'm your shopping assistant. Let me take your order. \n You can type 'add milk' to add milk to your shopping list. \n or you can type 'remove milk' to remove it. \n"

print(welcome_message)


#-->Todo: declare a shopping_list list
shoppingList = []

def prompt_user():


    reply = input("What do you want to add or remove?  >>  ")

    return reply


def check_answer(ans):
    splitAns = ans.split(" ",  1)
    return splitAns

def add_item(item):
#this function can take in a string and store it in an array
    shoppingList.append(item)


def remove_item(item):
    if item in shopping_list:
        shoppingList.remove(item)
    else:
        print("That was never in the list. ")


check_answer("remove milk")

while active:
    ans = check_answer(prompt_user())
    doneWriting = input("Are you done writing your list? (T/F) ") 
    if doneWriting == "T":
        active = False
    else:
        check_answer(prompt_user()) #this makes the program continously prompt and check response while the boolean 'active' returns True

    action = ans[0]
    item = ans[1]

    if action == "remove":
        remove_item(item)
        print(shoppingList)

    elif action == "add":
        add_item(item)
        print(shoppingList)

        
        
