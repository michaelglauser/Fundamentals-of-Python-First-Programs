#Python Programs Chapter 6 Project 8
#Write a script that tests Lee's function, and add code to trace the argument on each call.


def printAll(seq):
    print(f"seq: {seq}")
    if seq:
        print(seq[0])
        printAll(seq[1:])
        
printAll("hello")                          
printAll([5, 6, 7, 8, 9])  





