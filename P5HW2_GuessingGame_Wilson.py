#CTI-110
#Guessing Game
#Brandon Wilson
#8 July 2018

import random

def generateRandomNumber():
    randomNumber = random.randint (1, 100)
    return randomNumber

def askUserForNumber( message = "Guess the number: " ):
    userNumber = int(input(message))
    return userNumber

def checkUserNumber( userNumber, randomNumber ):
    if userNumber > randomNumber:
        return "Too High"
    elif userNumber < randomNumber:
        return "Too Low"
    else:
        return "Congratulations!"
        


def main():
    userCongratulated = False
    letsStart = True
    
    while userCongratulated or letsStart:
        randomNumber = generateRandomNumber()
        userNumber = askUserForNumber()
        message = checkUserNumber( userNumber, randomNumber )

        while message != "Congratulations!":
            print (message)
            userNumber = askUserForNumber( "Try again: " )
            message = checkUserNumber( userNumber, randomNumber )

        print( message )
        userCongratulated = True
        

main()
