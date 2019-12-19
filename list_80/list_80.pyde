img, img2, img3, img4 = 0, 0, 0, 0

def setup():
    global img, img4
    background(100)
    smooth()
    size(670, 436)
    noStroke()
    img = loadImage('bloom.png')
    img4 = loadImage('winx-stella.png')
    
def draw():
    global img, img4, img2, img3
    if frameCount == 1:
        image(img, 0, 0)
        
    val2 = int(random(0,150))
    val3 = int(random(0,150))
    img2 = img.get(mouseX + val2,0,20,height)
    img3 = img.get(mouseX + val3,0,5,height)
    blendMode(SUBTRACT)
    tint(255,20)
    image(img2,mouseX + val2, random(0,height))
    noTint()
    blendMode(BLEND)
    image(img3,mouseX - val3, 0)
    image(img4,0, 0)
    
def keyPressed():
    if key=='s':
        saveFrame("80_"+str(frameCount)+".jpg")
