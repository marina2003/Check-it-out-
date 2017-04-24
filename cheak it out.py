# WJEC Controlled Asessment Computer Science
# Cheack It Out 2017
# Python 3.3.2/3.5.2

# Python Import
import time

# Welcome message 
print("Welcome to Illuminate Jewelers Loyalty Card System")  
while True:
    user = input("Would You Like To Check If Your Loyalty Card Is Valid? (yes/no): ")
    if user == 'yes':
        break
        print("Please Wait While We Process Your Request...")
    else:
        print("Exiting Program")
        exit(0)
time.sleep( 0 )
# User Inputs
#fullName = input("Please Enter Your Full Name: ")
#time.sleep( 1 )
#postCode = input("Please Enter Your Postcode?")
#time.sleep( 1 )
#print("Just Some More Details Before We Can Process Your Request...")
#time.sleep( 1 )
cardNumber = input("Please Enter Your Loyalty Card Eight Digit Card Number: ")

# CardExpiry Date Validation

# Card Validation
while len(cardNumber) != 8:
  cardNumber = input('Invalid Not An Eight Digit Number. Please Enter Your Cards Eight digit number: ')
  break
print("Please Wait While We Process Your Information...")

# Digit Conversation
number_list = list(map(int, cardNumber))

# Store Eight Digit
check_Digit = number_list[7] #grab the 8th item
print(check_Digit)
#check_Digit = list(map(int, cardNumber))[7]

# Digit Function Removes Eight Digit
del(number_list[7])

# Digit conversation list to string
string_number = ''.join(map(str, number_list))

# Digit Reverse Functions
reversed_number = int(string_number[::-1] )
print(reversed_number)

# Digit Call Function
Digits = reversed_number
# Digit Extraction Functions
Digit1 = int(str(Digits)[0])
Digit3 = int(str(Digits)[2])
Digit5 = int(str(Digits)[4])
Digit7 = int(str(Digits)[6])
# Loop over all digits
for digit in str(Digits):
# Convert current digit to an integer
  digit = int(digit)
# Odd Digit Multiply Functions
  if digit % 2 == 1:
    digit = digit * 2
# Digit Function If Greated Than 9 Then -9
  if digit > 9:
    digit = digit - 9
    
# Customers - Loyalty Card Details Message
print("Thank You, Below You Will Find Your Customers Details: ")
time.sleep( 2 )
print("Your FullName Is: ", fullName)
time.sleep( 1 )
print("Your Postcode Is: ", postcode)
time.sleep( 1 )
print("Your CardNumber Is: ", cardNumber)
time.sleep( 1 )
print("Your Card Expiry Date Is: ", cardExpiry)
time.sleep( 1 )
print("Thank You For Using Our Loyalty Cards! GoodBye")

