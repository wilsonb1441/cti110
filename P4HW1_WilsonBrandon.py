#CTI-110
#Distance Traveled
#Brandon Wilson
#29 June 2018




vehicleSpeed = float( input("What is the speed of the vehicle?: "))
timeTraveled = int( input("How many hours traveled?: "))

print("\nHour","\tDistance Traveled")
for currentHour in range( 1, timeTraveled + 1 ):
    distanceTraveled = vehicleSpeed * currentHour
    print(currentHour,"\t",distanceTraveled)
