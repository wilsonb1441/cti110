# CTI-110 
# P3HW1 - Age Classifier 
# Brandon Wilson
# 23 June 2018

def main():
    userAge = int( input("Please enter your age: "))

    if userAge <= 1: 
        print("\nInfant")
    elif userAge < 13:
        print("\nChild")
    elif userAge < 20:
        print("\nTeenager")
    elif userAge >= 20:
        print("\nAdult")


main()

