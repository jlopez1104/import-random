import random

#random intergers
#.lower = lowercase
#.upper = uppercase
#.capitalize = capitalize first letter
q = input('do you want to enter in a random number? (y/n): ').lower()
if q == 'y':
    x= random.randint(1,20) #creates random interger
    print(x)
else:
    print('goodbye')
    a = False

#other random selections

#random.random () - return a floating pt. number between 0 and 1

y = random.random()
print(y)
#want to make between 0 and 100? multiply by 100
y=y*100
print(y)

colour = random.choice(['red','yellow','blue'])
print(colour)