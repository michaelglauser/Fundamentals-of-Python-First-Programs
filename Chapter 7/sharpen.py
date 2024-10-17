#Python Programs Chapter 7 Project 10
#Define a function named sharpen that performs color value transformations. 
#This function should expect an image and two integers as arguments.

def sharpen(image, degree, threshold): 
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b)/3
            if average < threshold:
                r = r - degree
                g = g - degree
                b = b - degree
                if r < 0:
                    r = 0
                if g < 0:
                    g = 0
                if b < 0:
                    b = 0
                image.setPixel(x, y, (r, g, b))
