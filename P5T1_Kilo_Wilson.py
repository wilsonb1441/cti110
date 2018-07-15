#CTI-110
#Kiloconverter
#Brandon Wilson
#8 July 2018




def askUserForKilometers():
    userKilometers = float (input("Please enter the distance in kilometers: "))
    return userKilometers

def convertKilometersToMiles(userKilometers):
    miles = userKilometers * 0.6214
    return miles

def main():
    userKilometersTyped = askUserForKilometers()
    convertedMiles = convertKilometersToMiles( userKilometersTyped )
    
    print ("\n", userKilometersTyped, "kilometers converted to miles is", format (convertedMiles, ".2f" ), "miles")
            
main()
