import math 

#radius to area & area to radius
def circleArea(r):
    area = 2 * math.pi * r

    return area

area = circleArea(10)
print(int(circleArea(10)))

def circleRadius(area):
    r = area/(2*math.pi)
    return r

print(circleRadius(area))

#fahrenheit to celsius & celsius to fahrenheit
f = 32

c = (f -32)* (5/9)
print(c)

c = 59
f = (c/(5/9)) + 32
print(f)

#kg to pounds, pounds to kg
kg = 100 
pounds = kg *  2.2046

print(pounds)
print(pounds/ 2.2046)