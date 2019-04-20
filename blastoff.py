# additional while loop exercises

################
## Blastoff 1 ##
################

'''
num = 11
while num > 0:
    num -= 1
    print(num)
'''

################
## Blastoff 2 ##
################

'''
num = 11
while num > 0:
    num -= 1
    print(num)
    if num == 0:
        print('You have reached zero!')
'''

################
## Blastoff 3 ##
################

'''
num = int(input('Please enter an integer: '))

while num > 0:
    num -= 1
    print(num)
    if num == 0:
        print('You have reached zero!')

'''

################
## Blastoff 4 ##
################

num = int(input('Please enter an integer that is less than 20: '))

should_run = True

while should_run:
    if num > 20:
        should_run = False
    elif num < 20 and num > 0:
        num -= 1
        print(num)
    elif num == 0:
        print('Zero')
        should_run = False

