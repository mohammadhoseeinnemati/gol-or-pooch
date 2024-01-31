a = int(input("plz enter your 1 or 2 :"))

if a == 1:
    print("rock ...")
    print("paper ...")
    print("scissors ...")

    import random 

        
    randomNumber = random.randint(0,2)
    computerMove = "rock"

    if randomNumber == 0:
        computerMove = "rock"
    elif randomNumber == 1:
        computerMove = "paper"
    elif randomNumber == 2:
        computerMove = "scissors"

    player1 = input("player1 , make your move : ")
    print(f"player2 , make your move : {computerMove}")
    player2 = computerMove


    if a == 1:
        for  player1 in range(3):
            if player1 == range(3):
                break


    if player1 == "rock" and player2 == "scissors":
         print ("player 1 wins !...")
    elif player1 == "rock" and player2 == "paper":
        print("player 2 wins !...")
    elif player1 == "paper" and player2 == "rock":
        print("player 1 wins !...")
    elif player1 == "paper" and player2 == "scissors":
        print("player 2 wins !...")
    elif player1 == "scissors" and player2 == "paper":
        print("player1 wins !...")
    elif player1 == "scissors" and player2 == "rock":
        print("player2 wins !...")
    elif player1 == player2:
        print ("thats a tie !...")
    else:
        print("something went wrong !...")
   
if a == 2:
    player_1 = input("player1 , make your move :")
    player_2 = input("player2 , make your move :")

    if player_1 == "rock" and player_2 == "scissors":
         print ("player 1 wins !...")
    elif player_1 == "rock" and player_2 == "paper":
        print("player 2 wins !...")
    elif player_1 == "paper" and player_2 == "rock":
        print("player 1 wins !...")
    elif player_1 == "paper" and player_2 == "scissors":
        print("player 2 wins !...")
    elif player_1 == "scissors" and player_2 == "paper":
        print("player1 wins !...")
    elif player_1 == "scissors" and player_2 == "rock":
        print("player2 wins !...")
    elif player_1 == player_2:
        print ("thats a tie !...")
    else:
        print("something went wrong !...")
