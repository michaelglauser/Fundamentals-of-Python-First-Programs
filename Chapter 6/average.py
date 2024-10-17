#Python Programs Chapter 6 Project 9
#Write a program that computes and prints the average of the numbers in a text file. 
#You should make use of two higher-order functions to simplify the design.


a=open('number_average.txt','r')
b = a.read()
y=b.split()
print('The list',y)

def addition_function(l):
    s=0
    for i in range (len(l)):
        s+=int(l[i])
    return s
def division_function(x,n):
    d=x/n
    return d
v=division_function(addition_function(y),len(y))
print('The average of the list is: ',v)
a.close()
