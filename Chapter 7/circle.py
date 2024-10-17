#Python Programs Chapter 7 Project 1
#Define a function drawCircle.
#This function should expect a Turtle object, the coordinates of the circle’s center point, and the circle’s radius as arguments.
#The function should draw the specified circle.
#The algorithm should draw the circle’s circumference by turning 3 degrees and moving a given distance 120 times.
#Calculate the distance moved with the formula 2.0 * p * radius / 120.0. 

from turtle import Turtle
from math import pi

def Turtle(width = 500
height = 500
using_IDLE = True
colormode = 255):


def draw_circle(turtle_obj, radius, coordinate_x = 0, coordinate_y = 0):
    turtle_obj.up()
    turtle_obj.goto(coordinate_x, coordinate_y-radius) #set the circle’s center point
    turtle_obj.down()
    turtle_obj.color('red', 'yellow') #pen color is red, fill color is yellow
    turtle_obj.begin_fill()
    distance_moved = (pi * radius * 2.0)/120.0
    for i in range(120):
        turtle_obj.forward(distance_moved)
        turtle_obj.left(3)
    turtle_obj.end_fill()


def main():
    t = Turtle()
    t.hideturtle()
    while True:
        radius = input("Enter a positive number for radius: ")
        t.clear()
        try:
            radius = abs(float(radius))
            print(t.position())
            draw_circle(t, radius)
        except ValueError:
            break


if __name__ == "__main__":
    main()