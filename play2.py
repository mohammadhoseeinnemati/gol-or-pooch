
print("rock ...")
print("paper ...")
print("scissors ...")


a = int(input("plz enter your 1 or 2:"))

player1 = 0
player2 = 0

score = {

    "rock":1,
    "paper":1,
    "scissors":1
    
}


import random

for player_1 in range(3):
    if player_1 == range(3):
        break

if a == "1":
    randomNumber = random.randint(0,2)
    computerMove = "rock"
    if randomNumber == 0:
        computerMove = "rock"
    elif randomNumber == 1:
        computerMove = "paper"
    elif randomNumber == 2:
        computerMove = "scissors"

        player_1 = input("player1 , make your move : ")
        print(f"player2 , make your move : {computerMove}")
        player_2 = computerMove   

        if player_1 == "rock" and player_2 == "scissors":
            print ("player 1 wins !...")
            player1 = score["rock"]*player1+1
            print(player1)
        elif player_1 == "rock" and player_2 == "paper":
            print("player 2 wins !...")
            player2 = score["paper"]*player2+1
            print(player2)
        elif player_1 == "paper" and player_2 == "rock":
            print("player 1 wins !...")
            player1 = score["paper"]*player1+1
            print(player1)
        elif player_1 == "paper" and player_2 == "scissors":
            print("player 2 wins !...")
            player2 = score["scissors"]*player2+1
            print(player2)
        elif player_1 == "scissors" and player_2 == "paper":
            print("player1 wins !...")
            player1 = score["scissors"]*player1+1
            print(player1)
        elif player_1 == "scissors" and player_2 == "rock":
            player2 = score["rock"]*player2+1
            print("player2 wins !...")
            print(player2)
        elif player_1 == player_2:
             print ("thats a tie !...")
        else:
            print("something went wrong !..")



elif a == "2":
    player_1 = input("plz enter your name:")
    player_2 = input("plz enter your name:")


    player_1 = input("player1 , make your move : ")
    player_2 = input("player1 , make your move : ")

    if player_1 == "rock" and player_2 == "scissors":
            print ("player 1 wins !...")
            player1 = score["rock"]*player1+1
            print(player1)
    elif player_1 == "rock" and player_2 == "paper":
            print("player 2 wins !...")
            player2 = score["paper"]*player2+1
            print(player2)
    elif player_1 == "paper" and player_2 == "rock":
            print("player 1 wins !...")
            player1 = score["paper"]*player1+1
            print(player1)
    elif player_1 == "paper" and player_2 == "scissors":
            print("player 2 wins !...")
            player2 = score["scissors"]*player2+1
            print(player2)
    elif player_1 == "scissors" and player_2 == "paper":
            print("player1 wins !...")
            player1 = score["scissors"]*player1+1
            print(player1)
    elif player_1 == "scissors" and player_2 == "rock":
            player2 = score["rock"]*player2+1
            print("player2 wins !...")
            print(player2)
    elif player_1 == player_2:
             print ("thats a tie !...")
    else:
            print("something went wrong !..")
