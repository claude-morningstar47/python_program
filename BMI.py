# Simple BMI calculator using python

def body_mass_index(weight, height):
    return round((weight / height**2), 2)


print("Welcome to the BMI calculator.")

h = float(input("Enter your height in meter: "))
w = float(input("Enter your weight in kg: "))


bmi = body_mass_index(w, h)
print("Yours Body Max Index is: ", bmi)

if bmi <= 18.5:
    print("you are underweight.")
elif 18.5 < bmi <= 24.9:
    print("you weight is normal.")
elif 25 < bmi <= 29.29:
    print("you are overweight.")
else:
    print("You are obese.")
