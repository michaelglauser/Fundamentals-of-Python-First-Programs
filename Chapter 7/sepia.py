#Python Programs Chapter 7 Project 8
#Define and test a function named sepia that converts a color image to sepia. 
#This function should first call grayscale to convert the color image to grayscale.

def sepia(image):
    grayscale(image)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (red, green, blue) = image.getPixel(x, y)
            if red < 63:
                red = int(red * 1.1)
                blue = int(blue * 0.9)
            elif red < 192:
                red = int(red * 1.15)
                blue = int(blue * 0.85)
            else:
                red = min(int(red * 1.08), 255)
                blue = int(blue * 0.93)
