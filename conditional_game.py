import random
# -------------------------------------------- 

	# You've just learned about variables, conditionals.
	# Just from knowing those two topics, you can do so much!
	
	# Let's try to make a simple program that responds to the user.
	# We're going to recreate the Magic 8 Ball!!!
			
			# Never heard of it? That's ok!

					# You got this!

  # -------------------------------------------- 

	# How a Magic 8 Ball Works:

	# The user asks a question and vigoriously shakes the ball. 
	# Then the ball will respond with one of twenty responses, chosen at random. 

	# That's pretty simple right?

 # -------------------------------------------- 

	# Part 1: 
	# Print instructions on the screen and 
	# prompt the user to ask a question
  # --------------------------------------------


print("Welcome to 8 Ball. Ask a question and vigoriously shake the ball \n Then the ball will respond with one of twenty responses, chosen at random. ")

question = input("What is your question? ")

def manual(ballNumber):
	if ballNumber == 0:
		print("It is certain.")
	if ballNumber == 1:
		print("It is decidedly so")
	elif ballNumber == 2:
		print("Without a doubt")
	elif ballNumber == 3:
		print("Yes - definitely.")
	elif ballNumber == 4:
		print("You may rely on it.")
	elif ballNumber == 5:
		print(" As I see it, yes.")
	elif ballNumber == 6:
		print("Most likely.")
	elif ballNumber == 7:
		print("Outlook good.")
	elif ballNumber == 8:
		print("Yes")
	elif ballNumber == 9:
		print("Signs point to yes.")
	elif ballNumber == 10:
		print(" Reply hazy, try again.")
	elif ballNumber == 11:
		print(" Ask again later.")
	elif ballNumber == 12:
		print(" Better not tell you now.")
	elif ballNumber == 13:
		print(" Cannot predict now.")
	elif ballNumber == 14:
		print(" Concentrate and ask again.")
	elif ballNumber == 15:
		print(" Don't count on it.")
	elif ballNumber == 16:
		print("My reply is no.")
	elif ballNumber == 17:
		print("My sources say no")
	elif ballNumber == 18:
		print(" Outlook not so good.")
	else:
		print("Very doubtful.")

def lst_8_ball(ballNumber):
	lstOfResponses = [" It is certain.","It is decidedly so.","Without a doubt.","Yes - definitely."]
	print(lstOfResponses[ballNumber])

def main():
	ballNumber = random.randint(0,3)
	lst_8_ball(ballNumber)

main()

# -------------------------------------------- 

	# Part 2: Next, we need to randomly select a response from 20 options.

	# Randomly select a number from 0 - 19 
	# Use that to select from the following responses:
		# 0 - It is certain.
		# 1 - It is decidedly so.
		# 2 - Without a doubt.
		# 3 - Yes - definitely.
		# 4 - You may rely on it.
		# 5 - As I see it, yes.
		# 6 - Most likely.
		# 7 - Outlook good.
		# 8 - Yes.
		# 9 - Signs point to yes.
		# 10 - Reply hazy, try again.
		# 11 - Ask again later.
		# 12 - Better not tell you now.
		# 13 - Cannot predict now.
		# 14 - Concentrate and ask again.
		# 15 - Don't count on it.
		# 16 - My reply is no.
		# 17 - My sources say no.
		# 18 - Outlook not so good.
		# 19 - Very doubtful.

	# Look up random.rand_int to see how you can use it to select a random number.

  # -------------------------------------------- 

# -------------------------------------------- 

	# Part 3: Customize it!

	# Select your own theme and use case and modify your code!
	
# -------------------------------------------- 
#paper fortune teller

















