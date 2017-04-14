# WJEC Controlled Asessment Computer Science
# Cheack It Out 2017
# Python 3.3.2/3.5.2

# Python Import
import time

# Welcome message 
print("Welcome to Illuminate Jewelers") 
while True:
    user = input("Would You Like To Check If Your Loyalty Card Is Valid? (yes/no): ")
    if user == 'yes':
        break
        print("Please Wait While We Process Your Request...")
    else:
        print("Exiting Program")
        exit(0)
time.sleep( 5 )
# User Inputs
fullName = input("Please Enter Your Full Name: ")
time.sleep( 1 )
postCode = input("Please Enter Your Postcode?")
time.sleep( 1 )
print("Just Some More Details We Need To Process Your Request...")
time.sleep( 1 )
cardNumber = input("Please Enter Your Loyalty Card Eight Digit Card Number: ")
cardExpiry = input("Please Enter Your Cards Expiry Date: ")

# Date Validation

# Card Validation
while len(cardNumber) != 8:
  cardNumber = input('Invalid Not An Eight Digit Number. Please Enter Your Cards Eight digit number: ')
  break
print("Please Wait While We Process Your Information...")

# Digit Functions
check_Digit = int(cardNumber) // 10
check_Digit = int(str(check_Digit)[::-1])
print(check_Digit)

# Customers - Loyalty Card Details Message
print("Thank You, Below You Will Find Your Customers Details: ")
time.sleep( 2 )
print("Your FullName Is: ", fullName)
time.sleep( 1 )
print("Your Postcode Is: ", postCode)
time.sleep( 1 )
print("Your CardNumber Is: ", cardNumber)
time.sleep( 1 )
print("Your Card Expiry Date Is: ", cardExpiry)
time.sleep( 1 )
print("Thank You For Using Our Loyalty Cards! GoodBye")
