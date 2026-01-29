import random

random_nmbr = random.randint(1, 100)

while True:
    try:
        guess_number = int(input("Guess the number between 1 and 100: "))

        if guess_number < random_nmbr:
            print("too low!")
        elif guess_number > random_nmbr:
            print("too high!")
        else:
            print("Congrats!")
            break
    except ValueError:
        print("Invalid!")