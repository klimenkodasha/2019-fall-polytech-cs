img1, img2 = 0, 0

def setup():
    global img1, img2
    size(700,700)
    background(100)
    smooth()
    img1 = loadImage('xxx.jpg')
    img2 = loadImage('ggg.jpg')
    
def draw():
    global img1, img2
    myTintBO = map(mouseX, 0, width, 0, 255)
    myTintVP = map(mouseX, 0, width, 255, 0)
    tint(200, myTintVP)
    image(img1, 0, 0)
    tint(200, myTintBO)
    image(img2, 0, 0)
