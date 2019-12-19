img0, img1, img2, img3 = 0, 0, 0, 0

def setup():
    global img0, img1, img2, img3
    background(100)
    smooth()
    size(900, 900)
    img0 = loadImage('bloom.png')
    img1 = loadImage('flora.png')
    img2 = loadImage('winx-stella.png')
    img3 = loadImage('tecna.png')
    
    
def draw():
    global img0, img1, img2, img3
    background(100)
    image(img0, 0, 0)
    image(img1, mouseX*0.7 - 50, 0)
    image(img2, 0, 0)
    image(img3, width - mouseX*1.5, 35)
