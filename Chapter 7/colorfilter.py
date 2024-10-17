#Python Programs Chapter 7 Project 9
#Develop three algorithms for lightening, darkening, and color filtering as three related Python functions, lighten, darken, and colorFilter.

def lighten(image, lightening):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            
            r = r + lightening
            if r > 255: 
                r = 255
                
            g = g + lightening
            if g > 255:
                g = 255
                
            b = b + lightening
            if b > 255:
                b = 255
                 
            image.setPixel(x, y, (r, g, b))
                
def darken(image, darkening):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            
            r = r - darkening
            if r < 0:
                r = 0
                
            g = g - darkening
            if g < 0:
                g = 0
                
            b = b - darkening
            if b < 0:
                b = 0
                
            image.setPixel(x, y, (r, g, b))
