#Python Chapter 2, Project 4 
#Write a program that takes the radius of a sphere (a floating-point number) as input, and then outputs the sphere's diameter, circumference, surface area, and volume.

import math

sphere_radius = float(input("The radius of the sphere = "))
sphere_diameter = float(sphere_radius * 2)

print("The diameter of the sphere is: " + str(sphere_diameter))
print("The circumference of the sphere is: " + str(sphere_diameter * math.pi))
print("The surface area of the sphere is: " + str(4 * math.pi * math.pow(sphere_radius,2)))
print("The volume of the sphere is: " + str(4/3 * math.pi * math.pow(sphere_radius,3)))





#Output
#The radius of the sphere = 
#3
#The diameter of the sphere is: 6.0
#The circumference of the sphere is: 18.84955592153876
#The surface area of the sphere is: 113.09733552923255
#The volume of the sphere is: 113.09733552923254


#** Process exited - Return Code: 0 **
#Press Enter to exit terminal