height = float(input("Enter your Height in Metres : "))
weight = int(input("Enter your Weight in KG : "))

BMI=(weight)/(height **2)
print(f"Height = {height} and Weight = {weight} \nBMI = {BMI}")

if BMI < 18.5:
    print("You are Underweight")
elif BMI < 25:
    print("Congratulations! Normal weight")
elif BMI < 30:
    print("You are a bit overweight")
elif BMI < 35:
    print("You are obese ; Watch what you are eating")
else:
    print("You need help! You are clinically obese")