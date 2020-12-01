in_temp = input('Type the temprature you want to convert.\n  (eg. 34C, 76F)\n Temprature: ')
# program input

temp = int(in_temp[:-1])
# numeric temperature

sym = in_temp[-1]
# 'sym' : symbol of temperature 

def C_F(sym, temp):
    """This function will change Farenhite to Celius or visa-versa"""

    if sym.upper() == 'F':
        F = int(temp)

        C = int(F - ((32/9) * 5))
        print(str(F) + sym.title() + 'F in Celcius: ' + str(C) + 'C')

    else:
        C = int(temp)

        F = int(((9*C)/5) + 32)
        print(str(C) + 'C in Farenhite: ' + str(F) + 'F')

C_F(sym, temp)
