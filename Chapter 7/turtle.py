#Python Programs Chapter 7 Project 3
#Write a script that draws the Koch snowflake.

from turtle import Turtle

t = Turtle()
  
def turtle_snowflake_fractal(distance, levels): 
    if levels == 0: 
        t.forward(distance) 
        return
    distancePerSide = distance / 3
    turtle_snowflake_fractal(distancePerSide, levels - 1) 
    t.right(60) 
    turtle_snowflake_fractal(distancePerSide, levels - 1) 
    t.left(120) 
    turtle_snowflake_fractal(distancePerSide, levels - 1) 
    t.right(60) 
    turtle_snowflake_fractal(distancePerSide, levels - 1) 

def main(): 
    distance = 200
    levels = int(input( "Enter the level (0 or greater): "))
    for part in range(3):     
        turtle_snowflake_fractal(distance, levels) 
        t.left(120)

if __name__ == "__main__":
    main()
input("Press enter/return to quit.")

