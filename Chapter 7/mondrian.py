#Python Programs Chapter 7 Project 4
#Design, implement, and test a script that uses a recursive function to draw these patterns.

from turtle import Turtle, Screen
import random

t = Turtle()

def rectangle_function(x1, y1, x2, y2):  
    Screen().colormode(255)
    t.fillcolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    t.begin_fill()
    t.up()
    t.setpos(x1, y1)
    t.down()
    for rectangleHalf in range(2):
        t.forward(x2 - x1)
        t.left(90)
        t.forward(y2 - y1)
        t.left(90)
    t.end_fill()

def recursive_function (x1, y1, x2, y2, level):
    if level > 0:
        rectangle_function(x1, y1, x2, y2)

        position = random.choice(["vertical", "horizontal"])
        if position == "horizontal":
            recursive_function(x1, y1, x2, ((y2 - y1) // 3 + y1), level - 1)
            recursive_function(x1, ((y2 - y1) // 3 + y1), x2, y2, level - 1)
        else:
            recursive_function(x1, y1, ((x2 - x1) // 3 + x1), y2, level - 1)
            recursive_function(((x2 - x1) // 3 + x1), y1, x2, y2, level - 1)

def main(level = 4, x1 = -100, y1 = 100, x2 = 100, y2 = -100):
    t.hideturtle()
    recursive_function(x1, y1, x2, y2, level)

if __name__ == "__main__":
    main()

