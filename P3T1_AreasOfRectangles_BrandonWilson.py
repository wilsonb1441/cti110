# P3T1
# Areas of Rectangles
# Brandon Wilson
# 23 June 2018

rectangle1Length = float( input("Enter length of rectangle 1: "))
rectangle1Width = float( input("Enter width of rectangle 1: "))
rectangle2Length = float( input("Enter length of rectangle 2: "))
rectangle2Width = float( input("Enter width of rectangle 2: "))
rectangle1Area = rectangle1Length * rectangle1Width
rectangle2Area = rectangle2Length * rectangle2Width

if rectangle1Area > rectangle2Area:
    print("Rectangle 1 is bigger than Rectangle 2")
elif rectangle2Area > rectangle1Area:
    print("Rectangle 2 is bigger than Rectangle 1")
else:
    print("Both rectangles are equal")
          
