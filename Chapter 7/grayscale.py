#Python Programs Chapter 7 Project 6
#Define a second version of the grayscale function that uses the allegedly crude method of simply averaging each RGB value.

def grayscale_function(image):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            averageLum = (r + g + b) // 3
            image.setPixel(x, y, (averageLum, averageLum, averageLum))
