print('-------------------------------------------------------------------Welcome To Unit Converter---------------------------------------------------------------------------------')


#select unit
print('\n Select cm for Centimeter \n Select m for Meter \n Select km for Kilometer \n')

#select unit conversion from unit1 to unit2
unit1 = input('Convert distance from ')
unit2 = input('Convert distance to ')

#Input of temperature
num1 = input('Enter Distance to convert ')

#conversion formulas for Centimeter
if unit1 == "cm" and unit2 == "cm":
    ans = (num1)
    print(num1,'cm =',ans,'cm')
elif unit1 == "cm" and unit2 == "m":
    ans = float(num1)/100
    print(num1,'cm =',ans,'m')
elif unit1 == "cm" and unit2 == "km":
    ans = float(num1)/100000
    print(num1,'cm =',ans,'km')

#conversion formulas for Meter
elif unit1 == "m" and unit2 == "m":
    ans = float(num1)
    print(num1,'m =',ans,'m')
elif unit1 == "m" and unit2 == "cm":
    ans = float(num1)*100
    print(num1,'m =',ans,'cm')
elif unit1 == "m" and unit2 == "km":
    ans = float(num1)/1000
    print(num1,'m =',ans,'km')

#conversion formulas for Kilometers
elif unit1 == "km" and unit2 == "km":
    ans = float(num1)
    print(num1,'km =',ans,'km')
elif unit1 == "km" and unit2 == "cm":
    ans = float(num1)*100000
    print(num1,'km =',ans,'cm')
elif unit1 == "km" and unit2 == "m":
    ans = float(num1)*1000
    print(num1,'km =',ans,'m')
