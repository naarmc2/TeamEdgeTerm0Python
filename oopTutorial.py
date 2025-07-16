class BankAccount:
    def __init__(self, bankName, users, pins):
        self.bankName = bankName
        self.users= users
        self.pins = pins


class ATM:
    def __init__(self ,user, balance, pin):
        self.user
        self.exit = False
        self.pin = pin
        self.balance = balance
        
    def checkBalance(self, pin):
        if pin  == self.pin:
            return (f"${self.balance}")
        else:
            print("Wrong pin. Try again: ")
    def depositMoney(self, money):
        self.balance += money
        print(f"You deposited ${money}. You now have ${self.balance}")
        
    def withdraw(self, money):
        self.balance -= money
        print(f"You withdraw ${money}. You now have ${self.balance}")
        
    def exitScreen(self, response):
        if response == "exit":
            self.exit = True

def main():
    users =["Tim", "Jac", "Natty"]
    usersPin = {}
    for user in users:
        usersPin[user] = input("Commit to a four number sequence: ")
        
    print(usersPin)
    
    TDBank = BankAccount("TDBank", users, usersPin)
    
    #WalgreensATM = ATM("Natty" ,1000, )
    #WalgreensATM.depositMoney(4000)
    #print(User1.checkBalance(user1Pin))
    
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