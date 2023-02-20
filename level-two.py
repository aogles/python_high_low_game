import random

guess = 0
player = int(input("Pick a number 1-10? "))

while guess < 3:
    guess += 1
    computer = random.randint(1, 10)

    if computer == player:
        print("Computer wins! :)")
        break
    elif computer < player:
        print("Computers guess is too low.")
    else:
        print("Computers guess is too high.")
    if guess == 3:
        print("Computer ran out of guesses. Computer loses. :(")
        print("the number was", player)
