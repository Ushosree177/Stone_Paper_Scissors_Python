import random
options = ("rock","paper","scissor")
player = None
computer = random.choice(options)
player = input("Enter a choice(rock,paper,scissor): ")
print(f"Player: {player}")
print(f"Computer: {computer}")
if (player == computer):
    print("It's a tie.")
elif (player == "rock" and computer == "scissor"):
    print("Player is the winner.")
elif (player == "scissor" and computer == "paper"):
    print("Player is the winner.")
elif (player == "paper" and computer == "rock"):
    print("Player is the winner.")
else:
    print("Computer is the winner.")
