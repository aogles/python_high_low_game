import random


def play():
    guess = 0
    computer = random.randint(1, 10)

    while guess < 3:
        guess += 1
        player = int(input("Pick a number 1-10? "))

        if player == computer:
            print("You win! :)")
            break
        elif player < computer:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        if guess == 3:
            print("You ran out of guesses. You lose. :(")
            print("The number was", computer)


if__name__ == '__main__':
play()
