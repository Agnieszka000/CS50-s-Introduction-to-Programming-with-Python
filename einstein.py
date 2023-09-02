# Implement a program that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. 
# Assume that the user will input an integer.
# E = mc2

mass = input('Write mass in kilograms: ')
energy = int(mass) * (300000000 * 300000000)
print (f'The equivalent number of Joules is: {energy:,} Joules.')