
# Chapter 2, Project 3
# Write a program that the clerks at Five Star Retro Video can use to calculate the total charge for a customer's video rentals. 

new_video_cost = int(3.00)
old_video_cost = int(2.00)

new_video_quantity = input("Enter the number of new videos: ")
old_video_quantity = input("Enter the number of oldies videos: ")

total_new_video_cost = float(new_video_quantity) * float(new_video_cost)
total_old_video_cost = float(old_video_quantity) * float(old_video_cost)

total_cost = float(total_new_video_cost) + float(total_old_video_cost)

print("The total cost of the videos is $" + str(total_cost))