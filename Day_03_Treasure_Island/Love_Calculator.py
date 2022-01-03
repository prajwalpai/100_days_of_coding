your = input("Enter your name : ")
their = input("Enter their name : ")

combined_name = your.lower() + their.lower()

true_sum = 0
for letter in "true":
    true_sum = true_sum + combined_name.count(letter)

love_sum = 0
for letter in "love":
    love_sum = love_sum + combined_name.count(letter)

Total_sum = (true_sum*10)+love_sum

#print(f"Love caclulator score between {your} and {their} is : {Total_sum} ")

if Total_sum < 9 or Total_sum > 90:
    print(f"Your score is {Total_sum}, you go together like coke and mentos")
elif 40 < Total_sum < 50:
    print(f"Your score is {Total_sum}, you are alright togehter")
else:
    print (f"Your score is {Total_sum}")