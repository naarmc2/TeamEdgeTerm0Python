class BankAccount:
    def __init__(self, bankName, balance, users, pins):
        self.bankName = bankName
        self.users= users
        self.balance = balance
        self.pins = pins

class ATM:
    def __init__(self ,user, pin):
        self.user = user
        self.exit = False
        self.pin = pin
        
    def checkBalance(self, pin):
        if pin == self.pin:
            return (f"${self.balance}")
        else:
            print("Wrong pin. Try again: ")
    def depositMoney(other, money):
        other.balance += money
        print(f"You deposited ${money}. You now have ${other.balance}")
        
    def withdraw(other, money):
        other.balance -= money
        print(f"You withdraw ${money}. You now have ${other.balance}")
        
    def exitScreen(self, response):
        if response == "exit":
            self.exit = True

def main():
    users =["Tim", "Jac", "Natty"]
    pins = []
    usersPinAndBalances = {}
    for i in range(len(users)):
        pins.append(input(f"Commit to a four number sequence {users[i]}: "))
        
    print(pins)
    balances=[100, 1600, 532]
    for user in users:
        i = 0
        usersPinAndBalances[user] = (usersPinAndBalances[user], balances[i] )
        print((usersPinAndBalances[user], balances[i] ))
        i +=1
    print(usersPinAndBalances[user], balances[i] )
    
    TDBank = BankAccount("TDBank", users, usersPinAndBalances)
    
    WalgreensATM = ATM("Natty", usersPinAndBalances["Natty"] )
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