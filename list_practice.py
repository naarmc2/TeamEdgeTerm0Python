list_a = [1,2]
list_b = [3,7,8,9]

list_a.append(list_b.pop())
x = list_a[2] * list_b[1]

print(x)

cars = ["Honda", "Toyota", "BMW", "Ferrari", "Nissan", "Buggati"]

print(cars)

cars.remove('Buggati')
cars.append('Rolls Royce')
print(cars)
cars[3] ='Subaru'
#print(cars.clear())

message = 'he1Lo w0rld'

message = message.title().replace('1', 'l').replace('0','o')
print(message)

greeting = 'Hello!'
greeting = greeting[0:len(greeting)-1]
print(greeting)