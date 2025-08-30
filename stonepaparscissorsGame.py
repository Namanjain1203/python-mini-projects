import random
option = ("stone","paper","scissor")
computer = random.choice(option)
player = "NONE"
while player not in option:
    player = input("CHOOSE BETWEEN stone, paper AND scissor :")

print(f"COMPUTER : {computer}")
print(f"PLAYER : {player}")
if player == computer:
    print("TIE")
elif player == "stone" and computer == "paper":
    print("YOU LOSE!")
elif player == "stone" and computer == "scissor":
    print("YOU WIN!")
elif player == "paper" and computer == "stone":
    print("YOU WIN!")
elif player == "paper" and computer == "sciccors":
    print("YOU LOSE!")
elif player == "sciccors" and computer == "paper":
    print("YOU WIN!")
else:
    print("YOU LOSE!")