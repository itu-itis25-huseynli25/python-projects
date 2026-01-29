'''
import random

while True:
    option = input("Wanna roll the dice?(y/n): ").lower()
    if option == 'y':
        col1 = random.randint(1, 9)
        col2 = random.randint(1, 9)
        print(f'({col1}, {col2})')
    elif option == 'n':
        print('Thanks for playing!')
        break
    else: print ('Invalid option!')
'''
'''
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
'''










