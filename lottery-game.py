## Lottery Game

import random

nums_user = []
matches = int()
test_list = [1, 2, 3, 4, 5, 6]

## Recursive function, if a user inputs an invalid value they can try again
def fill_list(list):
    while True:
        try:
            n = int(input('Number: '))
        except ValueError:
            print('The value entered is not an integer, please try again')
            continue
        break        

    if (n < 1 or n > 36):
        print('The number entered is not between 1 and 36, please enter another number')
        fill_list(list)
    elif (n in list):
        print('The number had already been entered, please enter another')
        fill_list(list)
    else:
        nums_user.append(n)        

## The sample function is used to make sure there are no duplicate winner numbers
nums_random = random.sample(range(1, 36), 6)

print('Enter 6 numbers between 1 and 36')
for i in range(6):
    fill_list(nums_user)

## The nums_random list can be replaced with test_list for testing purposes
for i in range(len(nums_random)):
    if (nums_user[i] in nums_random):
        matches += 1

print('Numbers entered:', nums_user)
print('Winning numbers:', nums_random)
print('Matches:', matches)

if (matches == 6):
    print('You have won $5000000')
elif (matches == 5):
    print('You have won $1000000')
elif (matches == 4):
    print('You have won $500')
elif (matches == 3):
    print('You have won $100')
else:
    print('Sorry, no prize won')