
# -------------------------------------------- 
# Day 1 Challenges: 
# -------------------------------------------- 

# Example
message = "Hello World!"
print(message)

# -------------------------------------------- 
# Challenge 1:
# Imagine it's the first day of class. (Wait, it is the first day isn't it..Deja vu?) 
# Everyone's participating in an icebreaker and has to introduce themselves. 
# It goes something like:
# -------------------------------------------- 

print("------------------- Challenge 1 -------------------")

name = "Nathania"
grade = 12
funFact = "I like painting"

print(f"Hi! My name is {name}")
print(f"I'm in the {grade}th grade.")
print(f"A fun fact about me is that {funFact}")


# **** Challenge 1: Problem 1 ****
# Initalize the variables with your response for the three statements above! 
# Hint: Also think about where you would initialize those variables


# **** Upchallenge! ****
# Can you also print out the data type of the variables? 
name = ("Nathania", "string")
grade = (12, "int")
funFact = ("I like painting")

print(f"Hi! My name is {name}")
print(f"I'm in the {grade}th grade.")
print(f"A fun fact about me is that {funFact}")

# **** Challenge 1: Problem 2 ****
# Create a string for the different lines of the Happy Birthday Song
# Print out the song using the strings you declared.
line1 = "Happy Birthday to You"
line2 = "Happy Birthday to You"
line3 = "Happy Birthday dear ____"
line4 = "Happy Birthday to You"

print(line1 + '\n' + line2 + '\n' + line3 + '\n' + line4)

# **** Challenge 1: Problem 3 ****
# Print out a string that has brackets in it.
score = 120
print(f"{score}")


# -------------------------------------------- 
# Challenge 2: 
# Below is a set of problems to help you solidify your understanding of math operators
# Write your solution code under each commented problem. 
# -------------------------------------------- 

print("------------------- Challenge 2 -------------------")

# Here are some variables to get you started
num1 = 5
num2 = 10

# **** Challenge 2: Problem 1 ****
# Store the sum of num1 and num2 in a variable.
# Print the sum.
sum1 = num1 + num2
print(sum1)

# **** Challenge 2: Problem 2 ****
# Store the difference between sum (above) and 7 in a variable.
# Print the difference.
diff = sum1 - 7
print(diff)

# **** Challenge 2: Problem 3 ****
# Store the product of the difference and 3 in a variable.
# Print the product.
mult = diff * 3
print(mult)

# **** Challenge 2: Problem 4 ****
# Store the power of the product squared in a variable.
# Print the power.
power = mult**2
print(power)
# **** Challenge 2: Problem 5 ****
# Store the quotient of the power divided by 4 in a variable.
# Print the quotient.
quotient = power/4
print(quotient)

# **** Challenge 2: Problem 6 ****
# Store the remainder of the quotient divided by 2 in a variable.
# Print the remainder.
remainder = quotient%2
print(remainder)

# **** Upchallenge! ****
# Given a variable that stores a number, print the values that come right before and right after.
# For example, given the number 4, the program should print 3 and 5. 
# Your code should work if the value of the variable is changed.
num = 9
numBefore = num -1
numAfter = num + 1
print(num)
print(numBefore)
print(numAfter)
# -------------------------------------------- 
