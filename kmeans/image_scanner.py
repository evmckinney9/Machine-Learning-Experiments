from PIL import Image
#im = Image.open("image1.jpg")
#pix = im.load()
#im.size access dimension
#pix[x,y] access (R,G,B)
#im.save("image1_new.jpg")

def getRGB(im):
    dictTemp = {}
    pix = im.load()
    return pix

def getDimensions(im):
    pix = im.load()
    rangex = im.size[0]
    rangey = im.size[1]
    tempList = [rangex,rangey]
    return tempList

def getImage(filename):
    return Image.open(filename)
