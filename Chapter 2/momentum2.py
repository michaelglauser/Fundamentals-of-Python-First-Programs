#Python Programs Chapter 2 Project 6
#Modify project 5, so that it prints the object's kinetic energy, as well as its momentum.



import math


mass = input("Enter the mass of the object, in kilograms: ")
velocity = input("Enter the velocity of the object, in meters per second: ")

momentum = float(mass) * float(velocity)

print ("The total mass of the object is: " + str(int(mass)))
print ("The total velocity of the object is: " + str(velocity))
print("The total momentum of the object is: " + str(momentum))
print ("The kinetic energy of the object is " + str(1/2 * mass * math.pow(velocity,2)))