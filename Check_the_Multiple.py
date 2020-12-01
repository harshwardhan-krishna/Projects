x = int(input('What is your number: '))

if x % 7 == 0:
    if x % 5 == 0:
        print(' Yes! This is number is a multiple of both 7 and 5.')
else:
    print('  This is not a correct value.')
