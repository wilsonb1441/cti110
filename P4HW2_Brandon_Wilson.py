#CTI-110
#Running Total
#Brandon Wilson
#30 June 2018

total = 0 
userNumber = float (input("Please enter first number: "))

while userNumber > -1:
    total = total + userNumber
    userNumber = float( input("Enter the next number: "))
print("Total", total)
