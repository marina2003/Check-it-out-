# WJEC Controlled Asessment Computer Science
# Cheack It Out 2017
# Python 3.3.2/3.5.2

# Python Import
import time

# Welcome message 
print("Welcome to Illuminate Jewelers")
while True:
    user = input("Would you like to cheack if your loyalty card is valid? (yes/no): ")
    if user == 'yes':
        break
        print("Please wait while we process your request...")
    else:
        print("Exiting Program")
        exit(0)
time.sleep( 5 )
# User Inputs
fullName = input("Please Enter Your Name: ")
postCode = input("Please Enter Your Postcode?")  
cardNumber = input("Please enter your loyalty card 8 digit number: ")
cardExpiry = input("Please enter your cards expiry date: ")

# Date Validation

# Card Validation
while len(cardNumber) != 8:
  cardNumber = input('That was not a 8 digit number. Please enter your 8 cards digit number: ')
  break
print("Please wait while we process your information...")

# Digit Functions
check_Digit = int(cardNumber) // 10
check_Digit = int(str(check_Digit)[::-1])
print(check_Digit)

# Customers - Loyalty Card Details Message
print("Thank you, below you will find your customers details: ")
time.sleep( 2 )
print("Your FullName Is: ", fullName)
print("Your Postcode Is: ", postCode)
print("Your CardNumber Is: ", cardNumber)
print("Your Card Expiry Date Is: ", cardExpiry)
print("Thank-You for using our loyalty cards!")

