#CTI-110
#Feet to inches
#Brandon Wilson
#8 July 2018

inches_per_foot = 12

def main():
    feet = int(input("Enter number of feet: "))
    print(feet, "feet equals", feet_to_inches(feet), "inches.")

def feet_to_inches(feet):
    return feet * inches_per_foot
    


main()
