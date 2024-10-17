#Python Programs Chapter 3 Project 4
#Write a program that lets the user enter the initial height from which the ball is dropped and the number of times the ball is allowed to continue bouncing. Output should be the total distance traveled by the ball.

height_ball_dropped = int(input('Enter the height from which the ball is dropped: '))
number_of_bounces = int(input('Enter the number of times the ball is allowed to continue bouncing: '))
bounciness_index = float(input('Enter the bounciness index of the ball: '))


intdist = 0

for drop_a_ball in range(1,number_of_bounces+1):
    intrebound = height_ball_dropped * bounciness_index
    intdist += intrebound + height_ball_dropped
    height_ball_dropped = intrebound

print("The total distance traveled by the ball is: " + str(float(intdist)) + " units.")





