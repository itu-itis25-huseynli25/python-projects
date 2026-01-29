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









