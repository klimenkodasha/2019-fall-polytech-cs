def setup():
    size(500,500)
    smooth()
    background(255)
    noStroke()
    colorMode(HSB)

flag = False
def draw():
    global flag
    if flag:
        for i in range(10):
            for j in range(5):
                fill(10, random(0, 255), random(10, 250))
                rect(j*40+50, i*40+50, 35, 35)
                rect((10-j)*40+10, i*40+50, 35, 35)

def mouseClicked():
    global flag
    if flag:
        flag = False
    else:
        flag= True
    
