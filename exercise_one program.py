# Hello! This python program calculates multiplication or sum of two given numbers. 

# Asks the user to input two integer numbers:
user_inputted_number_one = int(input('Hello User! Please add a number here: '))
user_inputted_number_two = int(input('Please add the other number: '))

# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
user_inputted_number_product = user_inputted_number_one * user_inputted_number_two
if user_inputted_number_product <= 1000:
    print('The product of your two given numbers is', user_inputted_number_product)
else:
    print('The sum of your two given numbers is', (user_inputted_number_one + user_inputted_number_two))
