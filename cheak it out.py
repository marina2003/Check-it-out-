# WJEC Controlled Asessment Computer Science
# Cheack It Out 2017
# Python 3.3.2/3.5.2

# Welcome message to the user
print("Welcome to loyalty card: Please follow the instructions provided")

# User Inputs
#full_name = input("Please enter your full name: ")
#postcode = input("Please enter your postcode: ")  
cardNumber = input("Please enter your loyalty card 8 digit number: ")
#CardExpiry = input("Please enter your cards expiry date: ")

# Testing Inputs
# print('Cusomer Deatils', full_name, postcode, cardNumber)

# Card Validation
while len(cardNumber) != 8:
    cardNumber = input('That was not a 8 digit number. Please enter your 8 cards digit number: ')
    break

# Digit Functions
check_Digit = int(cardNumber) // 10
print(check_Digit)

