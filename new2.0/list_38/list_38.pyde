def setup():
    size(500,500)
    smooth()
    background(150)
    strokeWeight(1)

flag = 1
def draw():
    global flag
    stroke(flag, 20)
    myY2 = mouseY + random(-10,10)*10
    myX2 = mouseX + random(-10,10)*10
    line(mouseX, mouseY, myX2, myY2)
    
def keyPressed():
    global flag
    if key=='w':
        flag = 255
    if key=='b':
        flag = 0
    if key =='s':
        saveFrame('38.png')
    
