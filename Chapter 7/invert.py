#Python Programs Chapter 7 Project 7
#Define and test a function named invert. 
#This function expects an image as an argument and resets each RGB component to 255 minus that component.

def invert(image):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = 255 - r
            g = 255 - g
            b = 255 - b
            image.setPixel(x, y, (r, g, b))
