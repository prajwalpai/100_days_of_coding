year = int(input("Enter the year you want to check : "))

if year % 4 != 0 :
    print("This is not a Leap year")
elif year % 100 != 0:
    print("This is a Leap year")
elif year % 400 != 0:
    print("This is not a Leap year")
else:
    print("Yes!! A leap year")

