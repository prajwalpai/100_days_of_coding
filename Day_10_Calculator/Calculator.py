import os
import ascii_art

def do_op(num1,num2,operation):
    if operation == "+":
        return(num1+num2)
    if operation == "-":
        return(num1-num2)
    if operation == "*":
        return(num1*num2)
    if operation == "/":
        return(num1/num2)

more_calulations=True
new_calculation='n'
result=0
while more_calulations:
    os.system('clear')
    print(ascii_art.calc)
    if new_calculation=='n':
        first_num  = int(input("What's the first number? : "))
    else:
        print(f"Using result as first num: {result}")
        first_num = result
    second_num = int(input("What's the next number?  : "))
    print("\n+\n-\n*\n/\n")
    op=input("Pick and operation : ")
    result = do_op(first_num,second_num,op)
    print(f"\n OUTPUT : {first_num} {op} {second_num} = {result}\n\n")
    new_calculation = input(f"Type 'Y' to continue calculating with {result}, or type 'N' to start a new calculation , 'E' to End. ").lower()
    if new_calculation == 'e':
        more_calulations = False
