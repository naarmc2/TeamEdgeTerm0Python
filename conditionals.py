
import random
# -------------------------------------------- 
# Day 2 Challenges
# -------------------------------------------- 

message = "Welcome to Day 2.\nToday we are learning about conditionals.\nLet's practice writing some conditionals of our own!"
print(message)
# -------------------------------------------- 

print("------------------- Challenge 1 -------------------")
# Can you drive?
   # Prompt the user to enter their age.
   # Write condi12tional statements that print out whether you can drive in your city. 



def canYouDrive(age):
   while not age.isdigit():
      age = input("Enter your age: ")
   age = int(age)
   if age < 16:
      print("You can't drive! Underage")
   elif 16 <= age <= 60:
      print("You can drive")
   else:
      print("You can't drive. Too old")

def main():
   age = (input("Enter your age: "))
   (canYouDrive(age))

#main()






# -------------------------------------------- 

print("------------------- Challenge 2 -------------------") 

# Who placed first?
   # Write conditional statements that checks which is the highest and prints the highest score. 
   # Hint: Create three variables and assign them random scores. 


score1 =  random.randint(1, 100)
score2 =  random.randint(1, 100)
score3 =  random.randint(1, 100)

def highestScore(score1, score2, score3):
   print( score1, score2, score3)
   if score1 > score2:
      if score1 > score3:
         return (f"Highest is score1: {score1}")
   elif score2 > score1:
      if score2 > score3:
         return (f"Highest is score2: {score2}")
   elif score3 > score1:
      if score3 > score2:
         return (f"Highest is score3: {score3}")
   else:
      return ("All or some values are the same" + str(max([score1, score2, score3])) )

print(highestScore(score1,score2,score3))

# -------------------------------------------- 

print("------------------- Challenge 3 -------------------")

# One of the most common parts of our daily routine is checking the weather. 
# Our outfit and accessories are dependent on the temperature and conditions outside. 
# ie. We're probably not going to wear shorts out when it's snowing...


# **** Challenge 3: Part 1 ****
# Write a conditional statement that checks the value of the weather variable 
# and prints out a weather report based on the current weather:
# Rainy: Bring an umbrella
# Sunny: Wear a hat and sunglasses
# Snowing: Wear gloves and a scarf 

# Here's a variable to get you started:
weather = "rainy"

if weather == "rainy":
   print("Bring an umbrella")
elif weather == "sunny":
   print("Wear a hat and sunglasses")
elif weather == "snowing":
   print("Wear gloves and a scarf")
else:
   print("Idk what to tell you man")



# Tip: Try changing the value of the weather variable to test your other conditions.

# **** Challenge 3: Part 2 ****
# Now that you've written conditions for specific weather forecasts, let's also add in temperature! 
# You can't dress accordingly if you only know that it's raining outside but not how cold it is!
# For example:
    # If it's raining and 60 degrees, you might want to bring your umbrella and wear a light jacket.
    # However, if it's raining and 30 degrees, you might want to break out a warmer jacket with your umbrella instead. 
    
   # Add to your conditional statements above and modify your weather reports to also take into account the temperature. 
   # Make sure to account for at least three different temperatures!
   # Hint: You will need another variable to keep track of the temperature.


temperature = random.randint(0, 125)

if 30 < temperature <= 60 and weather == "rainy":
   print("Bring umbrella & wear a light jacket")
elif temperature <= 30 and weather == "rainy":
   print("Bring umbrella & a warmer jacket")
else:
   print("Wear light clothing. it's hot")




# -------------------------------------------- 

print("------------------- Challenge 4 -------------------")

# Prompt the user to enter the day of the week (1-7 representing Monday - Sunday)
# Write a set of conditionals that will take a number from 1 to 7 
# and print out the corresponding day of the week. 
# Make sure to add a statement that accounts for any numbers out of range! 


dayOfWeek = input("What day is it? ")

number = input("Enter a number from 1-7, inclusive: ")
while number not in "1234567":
   number = input("Enter a number from 1-7, inclusive: ")

print(f"Today is {dayOfWeek} the {number}th")


# -------------------------------------------- 

print("------------------- Challenge 5 -------------------")

# A leap year is a calendar year that contains an additional day added 
# to keep the calendar year synchronized with the astronomical year or seasonal year.
# To calculate if a specific year is/was a leap year, you can follow the following steps:
     # 1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
     # 2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
     # 3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
     # 4. The year is a leap year (it has 366 days).
     # 5. The year is not a leap year (it has 365 days).

# Those are a lot of conditions...
# Your challenge is to translate the steps above into conditionals which will evaluate if the 
# year stored in a variable is/was a leap year.



year = int(input("Enter the year: "))

if year%4 == 0:
   if year%100 == 0:
      if year%400 == 0:
         print("It's a leap year")
else:
   print("year is not a leap year")


