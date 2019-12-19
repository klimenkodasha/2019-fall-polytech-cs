class MyPoint:
    x, y, = 0, 0
    
    def __init__(self, newX, newY):
        self.x, self.y = newX, newY
        
    def isDistanceLessThen(self, _dist, _point):
        result = False
        currentDist = dist(_point.x, _point.y, self.x, self.y)
        if currentDist < _dist:
            result = True
        return result
    
myPoints = []
currentPoint, currentDist = 0, 10.0

def setup():
    size(500,500)
    smooth()
    background(255)
    strokeWeight(1)
    
def draw():
    global currentPoint, myPoints
    stroke(0,20)
    currentPoint = MyPoint(mouseX, mouseY)
    myPoints.append(currentPoint)
    upDate()
    
def upDate():
    global myPoints, currentDist, currentPoint
    for pointFromArray in myPoints:
        if pointFromArray.isDistanceLessThen(currentDist,currentPoint):
            line(pointFromArray.x, pointFromArray.y, currentPoint.x, currentPoint.y)

def keyPressed():
    global currentDist
    if key == 's':
        saveFrame('72.png')
    for i in range(10):
        if key == str(i) and i!=0:
            currentDist = 10*i
        elif key == '0':
            currentDist = 100
