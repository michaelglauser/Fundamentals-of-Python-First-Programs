#Python Programs Chapter 7 Project 5
#Define and test a function named posterize. This function expects an image and a tuple of RGB values as arguments. 


from images import Image
import os, os.path

def posterize(rgbTuple, image):
    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b)/3
            if average < 128:
                image.setPixel(x, y, rgbTuple)
            else:
                image.setPixel(x, y, whitePixel)

def main(filename=' ', R=-1, G=-1, B=-1):
    while not str(os.path.exists(filename)) or not filename.endswith('.gif'): 
        filename = input("Enter file name path: ")
    image = Image(filename)
    while R < 0 or R > 255:
        R = int(input ("Enter the R value: "))
    while G < 0 or G > 255:
        G = int(input ("Enter the G value: "))
    while B < 0 or B > 255:
        B = int(input ("Enter the B value: "))
        
    posterize((R,G,B), image)
    image.draw()
    
if __name__ == "__main__":
    main()
