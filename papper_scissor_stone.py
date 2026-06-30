#猜拳遊戲
# import random
#
# player = None
# computer = None
# options = ["rock", "paper", "scissors"]
# running = True
#
# while running:
#     player = input("pls enter your choice:(rock, paper, scissors) ")
#     while player not in options:
#         input("pls enter your choice:(rock, paper, scissors) ")
#     computer = random.choice(options)
#     print(f"玩家:{player}，電腦:{computer}")
#     if player == computer:
#         print("平手")
#     elif player == "rock" and computer == "scissors":
#         print("玩家獲勝")
#     elif player == "paper" and computer == "rock":
#         print("玩家獲勝")
#     elif player == "scissors" and computer == "paper":
#         print("玩家獲勝")
#     else:
#         print("電腦獲勝")
#     play_again = input("do you want to play again?(y/n)").lower()
#     if play_again == "y":
#         running = True
#     else:
#         running = False
# print("Thank you for playing")

#改寫

import random

def rules(player, computer):
    if player == computer:
        return "平手"
    elif player == "rock" and computer == "scissors":
        return "玩家獲勝"
    elif player == "paper" and computer == "rock":
        return "玩家獲勝"
    elif player == "scissors" and computer == "paper":
        return "玩家獲勝"
    else:
        return "電腦獲勝"

options = ["rock", "paper", "scissors"]
running = True

while running:
    player = input("Please enter your choice: ").lower()

    while player not in options:
        player = input("Please enter your choice: ").lower()

    computer = random.choice(options)

    print(f"玩家: {player}，電腦: {computer}")

    result = rules(player, computer)
    print(result,"test error")

    play_again = input("Do you want to play again? (y/n): ").lower()

    if play_again != "y":
        running = False

print("Thank you for playing")
