def setup():
    size(500,500)
    smooth()
    background(255)
    strokeWeight(1)

cx, cy, cRadius, counter, counter1 = 250, 250, 200, 0, 0
def draw():
    global cx, cy, cRadius, counter, counter1
    stroke(0, 30)
    nx = sin(counter1)*cRadius + cx
    ny = cos(counter1)*cRadius + cy
    x1 = nx - sin(counter)*200
    x2 = nx + sin(counter)*200
    y1 = ny - cos(counter)*200
    y2 = ny + cos(counter)*200
    line(x1, y1, x2, y2)
    
    counter += 0.1
    
    if counter > 2*PI:
        counter = 0
    counter1 += 0.01
    if counter1 > 2*PI:
        counter1 = 0

def keyPressed():
    if key =='s':
        saveFrame('41.png')
    
