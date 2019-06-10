import datetime
import math

feet2meter = 0.09290304

def getAreaFeet(length_feet, width_feet):
    return length_feet * width_feet
    
def getAreaMeters(length_feet, width_feet):
    return length_feet * width_feet * feet2meter

def calcAreafuncname():
    length = input("What is the length of the room in feet? : ")
    width = input("What is the width of the room in feet? : ")
    print("You entered dimensions of " + length + " feet by " + width + " feet.")
    print("The area is " + str(getAreaFeet(float(length), float(width))) + " square feet " + str(getAreaMeters(float(length), float(width))) + " square meters")


calcAreafuncname()