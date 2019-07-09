"""
In this excercise we compute adult BMI from this page: https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html
You will have prepared command for reading input. 
Your task is to just implement the actual computation

Example: Weight = 68 kg, Height = 165 cm (1.65 m)
Calculation: 68 ÷ (1.65)^2 = 24.98

"""

mass_kg = int(input("What is your mass in kilograms?" ))
heights_m = float(input("What is your height?" ))


bmi = mass_kg / (heights_m /100)**2

print("Your BMI is: " + str(bmi))

# convert your weigth to stones:
# https://en.wikibooks.org/wiki/Python_Programming/Basic_Math

mass_stones = (mass_kg * 2.2)/14

print("Your weigth in stones is: " + str(mass_stones)) 