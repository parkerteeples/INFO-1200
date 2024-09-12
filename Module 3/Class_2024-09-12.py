# var_string = 'Parker'
# var_number = 125

# # Boolean Values and Expressions
# var_1 = True

# if var_1:
#     print(var_string)

# if var_string == 'Parker' and var_number == 13:
#     print('Correct Values')

# # if statements
    
# number = int(input('Please Enter a Number From 1 to 10: '))

# # If the nmber is 1-10
# if number >= 1 and number <= 10:
#     pass
# #if number is less than 10
# elif number < 1:
#     print('Your number is too low')
# #if number is greater than 10
# elif number > 11:
#     print('Number is too high')
# else:
#     print('use case was not handled')

# # String upper and lower methods

# name = input('Enter your name: ')

# # if name == 'Twix' or name == 'twix' or name == 'TWIX':
# #     print('Thats the name of my cat')

# if name.lower() == 'Twix':
#     print('Thats the name of my cat!')

# While Loops
# number = 0

# while number < 10 or number > 50:
#     number = int(input('Enter Number between 10-50:'))
#     if number < 10 or number > 50:
#         print('Your Number is NOT valid')
# print('Your number is valid')

# number = 0
# while True:
#     number = int(input('Enter Number between 10-50:'))
#     if number < 10 or number > 50:
#         print('Your Number is NOT valid')
#         continue

#     print('Your number is valid')
#     break

# For loop
for i in range(10):
    print(i,end=', ')
    if i == 5:
        print('caught a 5')
        continue
    if i == 5:
        break
print()


# for i in range(1,10):
#     print(i,end=', ')
# print()
# for i in range(2,10,2):
#     print(i,end=', ')
# print()