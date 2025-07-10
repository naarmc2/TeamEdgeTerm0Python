import random

guess =int(input("Enter a number from 1-10: "))
actualNumber = random.randint(1,10)
print(actualNumber)

def guessNumber(guess):
    while guess != actualNumber:
        guess =int(input("Enter a number from 1-10: "))
    print('Congrats!')

def main():
    guessNumber(guess)

main()