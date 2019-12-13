def setup():
    size(500,500)
    smooth()
    background(50)
    strokeWeight(2)
    stroke(250)

cx, cy, cRadius, counter, mcolor = 250, 250, 200, 0, 0
def draw():
    global cx, cy, cRadius, counter, mcolor
    x1 = sin(counter)*cRadius + cx
    y1 = cos(counter)*cRadius + cy
    mcolor += 1
    counter += 2*PI/255
    stroke(mcolor)
    line(cx, cy, x1, y1)
    
    if counter > 2*PI:
        counter = 0
        mcolor = 0
        background(50)

def keyPressed():
    if key =='s':
        saveFrame('40.png')
    
