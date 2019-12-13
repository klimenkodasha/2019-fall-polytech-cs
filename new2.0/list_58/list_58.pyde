class MyEllipse:
    centerX, centerY, angle, s, weight = 0, 0, 0, 0, 0
    
    def __init__(self, centerX, centerY, angle, s, weight):
        self.centerX, self.centerY, self.angle, self.s, self.weight = centerX, centerY, angle, s, weight
    
    def render(self):
        fill(200, self.s/20)
        x1 = self.centerX - cos(self.angle)*self.s/2
        y1 = self.centerY + sin(self.angle)*self.s/2
        
        stroke(250, 100)
        strokeWeight(self.weight)
        ellipse(x1, y1, self.s, self.s)
        
ellipseObj = 0

def setup():
    global ellipseObj
    size(500, 500)
    smooth()
    background(10)
    ellipseObj = MyEllipse(width/2, width/2, 0, 150, 1)
    
counter = 0

def draw():
    global counter, ellipseOBJ
    counter += 0.01
    if counter > TWO_PI:
        counter = 0
    ellipseObj.s = sin(counter*4)*mouseX
    ellipseObj.render()
