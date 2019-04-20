
# 1 to 10

'''
num = 0

while num < 10:
    num = num + 1
    print(num)
'''

# n to m

'''

start_num = int(input("Enter the starting number..."))
end_num = int(input("Enter the ending number..."))


num = start_num - 1

while num < end_num:
    num = num + 1
    print(num)

'''

# Odd numbers

'''
num = 1

while num < 10:
    if num % 2 == 1:
        print(num)
        num = num + 2
    else:
        continue
'''

# Coins

'''
coins = 0

print("You have %s coins" % (coins,))

should_run = True

while should_run:
    user_input = str(input("Do you want another? "))
    if user_input == "yes":
        coins = coins + 1
        print("You have %s coins." % (coins,))
    elif user_input == "no":
        should_run = False
        print("Bye")
'''

# Print a Square

print(*****)
