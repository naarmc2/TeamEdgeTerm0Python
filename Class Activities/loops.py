
###Example 1
#groceryList = ["Milk", "Bread","Eggs","Apples","Bananas"]
#for x in groceryList:
#    print(x)

#for i in range(0,10,2):
#    print(i)




###1)
#for i in range(100,201):
#    print(i)

###2)
for x in ['C','O','D','E',' ','N','E','X','T']:
   print(x)

lst = ['C','O','D','E',' ','N','E','X','T']
for x in range(len(lst)):
    print(lst[x])

#for x in range(-10, 11):
#    print(x)

#interval = 1
#for x in range(1,10):
#   print(x**2)

#for x in range(88, 42, -2):
#    print(x)

list = ['🍇', 3, 2, 1, '🍎', 3 ,2, 1, '🍌' , 3, 2, 1]

#for item in list:
#   print(item)

for i in range(101):
    if i%5 == 0 and i%3 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)