#### calculate  distance and Bearing between 2 points

import math

print( "calculate Distance and Bearing")

xeast = int(input("Enter X East: "))
xnorth = int(input("Enter X North: "))

yeast = int(input("Enter Y East: "))
ynorth = int(input("Enter Y North: "))

distance = math.sqrt((xeast-yeast)**2 + (xnorth-ynorth)**2)

print("The Distance is: ")
print(distance)

if (yeast > xeast) :

    if (ynorth > xnorth) :
        bearing = 57.2598*math.atan((yeast-xeast)/(ynorth-xnorth))   ####### 57.2598 conversion factor from radians to degrees

print( "The Bearing is: ")
print(bearing)




