def setup():
    size(500,500)
    smooth()
    background(50)
    strokeWeight(5)
    stroke(250)
    noLoop()

cx, cy, cRadius = 250, 250, 200
def draw():
    global cx, cy, cRadius
    i = 0
    for j in range(0, 12):
        i = i + 2*PI/12
        x1 = cos(i)*cRadius + cx
        y1 = sin(i)*cRadius + cy
        line(x1, y1, x1, y1)
    line(cx, cy, cx, cy)

def keyPressed():
    if key =='s':
        saveFrame('39.png')
    
