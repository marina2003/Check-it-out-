# WJEC Controlled Asessment Computer Science
# Cheack It Out 2017
# Python 3.3.2/3.5.2

# Python Import
import time

# Welcome Message
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
cardExpiry = input("Please enter your cards expiry date: ")
#time.sleep ( 1 )
cardNumber = input("Please enter your loyalty card eight digit number: ")

# CardExpiry Date Validation
print (time.strftime("%d/%m/%Y"))# Gets Current date
currentDate = (time.strftime("%d/%m/%Y"))

yearExpiry = cardExpiry[6:10]
monthExpiry = cardExpiry[3:5]
dayExpiry = cardExpiry[0:2]

NewcardExpiry = yearExpiry + "/" + monthExpiry + "/" + dayExpiry

# Card Validation
while len(cardNumber) != 8:
  cardNumber = input('Invalid not an eight digit number. Please enter your cards eight digit number: ')
  break
print("Please wait while we process your information...")

# Digit Conversation
numberList = list(map(int, cardNumber))

# Store Eight Digit
checkDigit = numberList[7] #grab the 8th item
print(checkDigit)
checkDigit = list(map(int, cardNumber))[7]

# Digit Function Removes Eight Digit
del(numberList[7])

# Digit conversation list to string
stringNumber = ''.join(map(str, numberList))

# Digit Reverse Functions
reversedNumber = int(stringNumber[::-1] )
print(reversedNumber)

# Digit Call Function
digits = reversedNumber
# Digit Extraction Functions
digit1 = int(str(digits)[0])
digit3 = int(str(digits)[2])
digit5 = int(str(digits)[4])
digit7 = int(str(digits)[6])
# Loop over all digits
for digit in str(digits):
# Convert current digit to an integer
  digit = int(digit)
# Odd Digit Multiply Functions
  if digit % 2 == 1:
    digit = digit * 2
    print(digit)
# Digit Function If Greater Than 9 Then -9
  if digit > 9:
    digit = digit - 9
    print(digit)

total_digits = Digit1 + Digit3 + Digit5 + Digit7 + Digit
print(total_digits)

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
