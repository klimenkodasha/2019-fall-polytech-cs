img1, img2, img3 = 0, 0, 0
isAnimate, currentFrame = True, 1

def setup():
    global img1, img2, img3
    background(100)
    smooth()
    size(800, 800)
    frameRate(12)
    img1 = loadImage('bloom.png')
    img2 = loadImage('flora.png')
    img3 = loadImage('winx-stella.png')
    
    
def draw():
    global img1, img2, img3, currentFrame, isAnimate
    background(100)
    if isAnimate:
        if currentFrame == 1:
            image(img1, mouseX, mouseY)
        elif currentFrame == 2:
            image(img2, mouseX, mouseY)
        elif currentFrame == 3:
            image(img3, mouseX, mouseY)
        currentFrame +=1
        if currentFrame >3:
            currentFrame = 1
    else:
        image(img1, mouseX, mouseY)
    
def keyPressed():
    global isAnimate
    isAnimate = not isAnimate
