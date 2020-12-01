n = 10
g = 47

print('\nYou have a total of 10 chances.\n Type "rules" to know about rules.')

while True:
    if n == 0:
        print('\n      ------GAME-OVER------')
        break

    n -= 1

    x = input('\n  Type the number you guessed: ')

    if x.lower() == 'q':
        break

    if x == 'rules':
        n += 1
        print(
            '\n1. There is a random 1 or 2 digit number is selected by the game.' +
            '\n2. You have guess the number without knowing it.\n' +
            '3. System will tell you that weather your number is greater or less than the selected number.\n' +
            '4. For this you have 10 chances\n' +
            '5. Good Luck!'
        )

    elif int(x) == g and n == 9:
        print('Bingo!! Correct guess in the first go!')

        break

    elif int(x) > g:
        print(' The number you guessed is greater.')
        print('   Chances remaining: ' + str(n))
    
    elif int(x) < g:
        print(' The number you gessed is smaller.')
        print('   Chances remaining: ' + str(n))
