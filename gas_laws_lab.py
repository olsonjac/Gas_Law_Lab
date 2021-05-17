# AirBag Lab Solver
###All variables are found in the header of this program
# Temperature in Kelvin = room temp in Celsius + 273
t = 293
# Rydberg's constant 
q = 0.0821
# Initial Volume of the ziploc bag in Liters
v = 0.95
# Molarity of HCl in moles/Liter
z = 6
# Molar Mass of NaHCO3 in Grams
a = 84.077
# Standard temperature and Pressure conversion from moles to Liters(22.4L/1 mole)
r = 22.4

#starting prompt that explains the purpose of the program
print('This program will help you determine how much HCl and NaHCO3 to put in your ziploc bag')

def my_function():
    x = float(input('Enter the amount of HCl in Liters that you intend to use '))
    y = float(input('Enter the amount of NaHCO3 in grams that you intend to use '))

#functions that calculate and prints the moles of CO2 generated
    Moles_CO2_HCl = float(x * z)
    Moles_CO2_NaHCO3 = float(y / a)
    print(Moles_CO2_HCl, 'moles of CO2 will be created with the entered amount of HCl')
    print(Moles_CO2_NaHCO3, 'moles of CO2 will be created with the entered amount of NaHCO3')

#Calculates the excess reactant left of whichever one was in excess.    
    Excess_NaHCO3 = (Moles_CO2_NaHCO3 - Moles_CO2_HCl)
    Excess_HCl = (Moles_CO2_HCl - Moles_CO2_NaHCO3)
    if (Moles_CO2_HCl > Moles_CO2_NaHCO3):
        print('There will be', Excess_HCl, 'moles of HCl unreacted.')
    else:
        print('There will be', Excess_NaHCO3, 'moles of NaHCO3 unreacted.')

#statement that determines how much CO2 is actually produced by taking into the account which reactant is the limiting reagaent  
    Actual_CO2_Volume1 = (Moles_CO2_HCl * r)
    Actual_CO2_Volume2 = (Moles_CO2_NaHCO3 * r)
    if (Moles_CO2_HCl > Moles_CO2_NaHCO3):
        print('The real volume of CO2 created when you account for limiting reagent(NaHCO3) is', Actual_CO2_Volume2, 'liters')
    else:
        print('The real volume of CO2 created when you account for limiting reagent(HCl) is', Actual_CO2_Volume1, 'liters')

#Determines the actual pressure in the bag using the ideal gas law(PV=nRT) in atm and prints to the console.
    actual_bag_pressure_1 = ((Moles_CO2_NaHCO3 * q * t) / (v))
    actual_bag_pressure_2 = ((Moles_CO2_HCl * q * t) / (v))
    if (Moles_CO2_HCl > Moles_CO2_NaHCO3):
        print('The pressure within the ziploc bag will be ',actual_bag_pressure_1, 'atm')
    else:
        print('The pressure within the ziploc bag will be',actual_bag_pressure_2, 'atm')
   
my_function()