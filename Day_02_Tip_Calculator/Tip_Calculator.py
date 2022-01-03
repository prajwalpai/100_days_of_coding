print('Welcome to the tip calculator.')
bill=int(input('\nEnter the total bill : '))
ppl=int(input('How many people to split the bill: '))
percnt=int(input('What percentage tip would you like to give : '))

tip= ((bill/ppl)*(percnt/100))
print('Each person should pay : '+str(tip))

