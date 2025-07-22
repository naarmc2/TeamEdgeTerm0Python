class BankAccount:
    def __init__(self, bankName, usersPinsAndBalances):
        self.bankName = bankName
        self.usersDictionary = usersPinsAndBalances
        
    def getBankName(self):
        return self.bankName
    
    def getUserPin(self,user):
        return self.usersDictionary[user][0]
    def getUserBalance(self,user):
        if user in self.usersDictionary:
            return self.usersDictionary[user][0]
        else:
            return None
        
    def updateBalance(self, user, amount):
        if user in self.usersDictionary:
            self.usersDictionary[user] = (self.usersDictionary[user][0], (self.usersDictionary[user][1] + amount))
        else:
            return False

        
class ATM:
    def __init__(self ,user, pin, userbankAccountObject):
        self.user = user
        self.exit = False
        self.pin = pin
        self.userbankAccount = userbankAccountObject
        
    def checkBalance(self, enteredPin):
        if enteredPin == self.pin:
            current_balance = self.bank_account.getUserBalance(self.user)
            if current_balance is not None:
                return f"Your current balance is: ${current_balance}"
            else:
                return "Error: Could not retrieve balance."
        else:
            return "Wrong pin. Try again."
        
    def depositMoney(self, money):
        self.balance += money
        print(f"You deposited ${money}. You now have ${self.balance}")
        
    def withdraw(self, money):
        other.balance -= money
        print(f"You withdraw ${money}. You now have ${self.balance}")
        
    def exitScreen(self, response):
        if response == "exit":
            self.exit = True

def main():
    users =["Tim", "Jac", "Natty"]
    pins = []
    usersPinsAndBalances = {}
    
    for i in range(len(users)):
        pins.append(input(f"Commit to a four number sequence {users[i]}: "))
        
    balances=[100, 1600, 532]
    for i in range(len(users)):
        usersPinsAndBalances[users[i]] = (pins[i], balances[i] )
       
    print(usersPinsAndBalances['Tim'][1])
    Tim = BankAccount("TD", usersPinsAndBalances)

    print(f"Welcome to {Tim.getBankName()} Bank. Please enter your name so that we may check if you have an account.")
    user = input("Name: ")
    
    if user in users:
        WalgreensATM = ATM(user, usersPinsAndBalances[user], Tim )
        print(f"You exist in our system. Welcome {user}!")
        print("What would you like to do today? ")
            
    WalgreensATM.depositMoney(Tim,4000)
    print(WalgreensATM.checkBalance(Tim))
    
main()


# class House:
#     def __init__(self, location, numRooms):
#         self.location = location
#         self.numRooms = numRooms
#         self.locked = True
        
#     def addRoom(self,newRooms):
#         self.numRooms + newRooms
        
#     def howManyRooms(self):
#         return self.numRooms
    
#     def __str__(self):
#         pass
    

# class Pet:
#     def __init__(self, name, hasLegs, age):
#         self.name = name
#         self.hasLegs = hasLegs
#         self.age = age
        
#     def intro(self):
#         print(self.name, 'is', self.age, "years old!")
        
# cat = Pet("Dog", True, 7)
# dog1 = Pet("Sage", True, 5)

# cat.intro()

# def main():
#     villa = House("Hamptons", 4)
#     print(villa.howManyRooms())
#     #print(villa)
    
# main()