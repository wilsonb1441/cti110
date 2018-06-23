#CTI-110
#Software Sales
#Brandon Wilson
#23 June 2018

def main():
    numberOfPackages = int( input( "How many packages would you like to purchase?: "))
    packagePrice = 99
    if numberOfPackages < 10:
        discount = 0
    elif numberOfPackages < 20:
        discount = 0.10
    elif numberOfPackages < 50:
        discount = 0.20
    elif numberOfPackages < 100:
        discount = 0.30
    else:
        discount = 0.40
    subTotal = numberOfPackages * packagePrice
    discountAmount = discount * subTotal
    total = subTotal - discountAmount

    print("\nTotal Before Discount: $" +format( subTotal, ",.2f") + "\nDiscount Amount: $" +format( discountAmount, ",.2f") +"\nTotal Amount: $" + format( total, ",.2f"))
        




main()
print("")
print("Thank You For Your Purchase")

