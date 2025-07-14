import random

def generateRandomNumber(maximumValue):
    actualNumber = random.randint(1, maximumValue)
    return actualNumber

def guessNumber(maximumValue):
    actualNumber = generateRandomNumber(maximumValue)
    print(f"The actual number is {actualNumber}")
    #count = 0
    guess =int(input(f"Enter a number from 1-{maximumValue}: "))
   
    while guess != actualNumber:
        #count +=1
        if 1 <= guess <= maximumValue:
            print("Your guess is wrong but within range")
        else:
            print('Your guess is out of range')
        guess =int(input(f"Enter a number from 1-{maximumValue}: "))
    print('Congrats!')

def main():
    maximumValue = 10
    guessNumber(maximumValue)

main()


