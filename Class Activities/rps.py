import random

def rockPaperScissors():
    player1Points = 0
    player2Points = 0 
    done = False

    while done == False: 
        player1Choice = input('Player 1 choose rock, paper, or scissors: ').lower().strip()
        while player1Choice not in ["rock", "paper", "scissors"]:
            player1Choice = input('Invalid. Player 1 choose rock, paper, or scissors: ')

        player2Choice = input('Player 2 Choose rock, paper, or scissors: ').lower().strip()

        while player2Choice not in ["rock", "paper", "scissors"]:
            player2Choice = input('Invalid. Player 2 choose rock, paper, or scissors: ')

        if player1Choice == player2Choice:
            print("Tie")
        elif (player1Choice == "rock" and player2Choice == "scissors") or (player1Choice == "scissors" and player2Choice == "paper") or (player1Choice == "paper" and player2Choice == "rock")  :
            player1Points += 1
            print(f"Player 1 wins with {player1Points}")
        else:
            player2Points +=1
            print(f"Player 2 wins with {player2Points}")
            
        done = input("Are you done playing? (True/False) ").upper()
        if done == "TRUE":
            done = True
        else:
            done = False

    if done == True:
        print(f"Player 1 has {player1Points} points")
        print(f"Player 2 has {player2Points} points")

#rockPaperScissors()


def rockPaperScissorsAI():
    player1Points = 0
    player2AIPoints = 0 

    done = False
    while done == False: 
        player1Choice = input('Player 1 choose rock, paper, or scissors: ').lower().strip()
        while player1Choice not in ["rock", "paper", "scissors"]:
            player1Choice = input('Invalid. Player 1 choose rock, paper, or scissors: ')

        player2AI = random.randint(1,3)
        if player2AI == 1:
            player2AIChoice = "rock"
        elif player2AI == 2:
            player2AIChoice = "paper"
        else:
            player2AIChoice = "scissors"

        if player1Choice == player2AIChoice:
            print("Tie")
        elif (player1Choice == "rock" and player2AIChoice == "scissors") or (player1Choice == "scissors" and player2AIChoice == "paper") or (player1Choice == "paper" and player2AIChoice == "rock")  :
            player1Points += 1
            print(f"Player 1 wins with {player1Points}")
        else:
            player2AIPoints +=1
            print(f"Player 2 AI wins with {player2AIPoints}")
                
        done = input("Are you done playing? (True/False) ").upper()
        if done == "TRUE":
            done = True
        else:
            done = False

    if done == True:
        print(f"Player 1 has {player1Points} points")
        print(f"Player 2 AI has {player2AIPoints} points")

rockPaperScissorsAI()