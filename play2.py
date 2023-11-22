
print("rock")
print("paper")
print("scissor")

player1 = int(input("player1 plz enter yuor moove:"))

import random
rnd = (random .randint(0,2))
print(rnd)

if player1 == "0" and rnd == "1":
    print("you lost")
elif player1 == "0" and rnd == "2":
    print("you win")
elif player1 == "0" and rnd =="0":
    print("equal")
elif player1 == "1" and rnd == "0":
    print("you win")
elif player1 == "1" and rnd == "2":
    print("you lost")
elif player1 == "1" and rnd =="1":
    print("equal")
elif player1 == "2" and rnd == "0":
    print("you lost")
elif player1 == "2" and rnd == "1":
    print("you win")
elif player1 == "2" and rnd =="2":
    print("equal")