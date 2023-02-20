import random

guess = 0
player = int(input("Pick a number 1-10? "))
computer = 0
low = 1
high = 10

while computer != player:
    guess += 1
    computer = (low + high) // 2
    if computer > player:
        print("Computer guessed", computer, ".That's too high!",
              "this is guess number", guess,)
        high = computer - 1
        continue
    elif computer < player:
        print("Computer guessed", computer, ". That's too low!",
              "this is guess number", guess,)
        low = computer + 1
        continue

if computer == player:
    print("Computers guessed", computer, "Computer wins! :)",
          "this is guess number", guess)
