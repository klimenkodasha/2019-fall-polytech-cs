class MyLine:
    centerX, centerY, l, angle, weight = 0, 0, 0, 0, 0
    
    def render(self):
        x1 = self.centerX - cos(self.angle)*self.l/2
        y1 = self.centerY + sin(self.angle)*self.l/2
        x2 = self.centerX + cos(self.angle)*self.l/2
        y2 = self.centerY - sin(self.angle)*self.l/2
        stroke(50, 100)
        strokeWeight(self.weight)
        line(x1, y1, x2, y2)
        strokeWeight(5)
        stroke(50)
        line(x2, y2, x2, y2)
        line(x1, y1, x1, y1)
        
lineObj, counter, radius = MyLine(), 0, 0

def setup():
    global lineObj, radius
    radius = 50
    size(500, 500)
    smooth()
    background(255)
    lineObj.centerX = width/2
    lineObj.centerY = height/2
    lineObj.l = 350
    lineObj.angle = PI/4
    lineObj.weight = 1
    
def draw():
    global counter, lineObj, radius
    counter += 0.05
    if counter > TWO_PI:
        counter = 0
        radius += 50
    lineObj.centerX = width/2 + sin(counter)*radius
    lineObj.centerY = width/2 + cos(counter)*radius
    lineObj.angle = counter*2
    lineObj.render()
    
def keyPressed():
    if key =='s':
        saveFrame('56.png')
