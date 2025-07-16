class House:
    def __init__(self, location, numRooms):
        self.location = location
        self.numRooms = numRooms
        self.locked = True
        
    def addRoom(self,newRooms):
        self.numRooms + newRooms
        
    def howManyRooms(self):
        return self.numRooms
    
    def __str__(self):
        pass
    

class Pet:
    def __init__(self, name, hasLegs, age):
        self.name = name
        self.hasLegs = hasLegs
        self.age = age
        
    def intro(self):
        print(self.name, 'is', self.age, "years old!")
        
cat = Pet("Dog", True, 7)
dog1 = Pet("Sage", True, 5)

cat.intro()

def main():
    villa = House("Hamptons", 4)
    print(villa.howManyRooms())
    #print(villa)
    
main()