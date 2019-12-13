xCoordinate = []

def setup():
    global xCoordinate
    size(500, 500)
    smooth()
    noStroke()
    for i in range(10):
        xCoordinate.append(35*i + 90)
        
def draw():
    global xCoordinate
    background(50)
    for coordinate in xCoordinate:
        fill(200)
        ellipse(coordinate, 250, 30, 30)
        fill(0)
        ellipse(coordinate, 250, 3, 3)
        
def keyPressed():
    if key == 's':
        saveFrame('60.png')
