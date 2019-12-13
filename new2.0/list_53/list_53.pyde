class FunnyRect:
    cx, cy, fsize = 0, 0, 0
    
    def setCenter(self, x, y):
        self.cx = x
        self.cy = y
    
    def setSize(self,s):
        self.fsize = s
    
    def render(self):
        rect(self.cx, self.cy, self.fsize, self.fsize)
        
funnyRectObj, funnyRectObj1, counter  = FunnyRect(), FunnyRect(), 0

def setup():
    global funnyRectObj, funnyRectObj1
    size(600, 600)
    smooth()
    noStroke()
    rectMode(CENTER)
    funnyRectObj.setSize(50)
    funnyRectObj1.setSize(20)
    
def draw():
    global funnyRectObj, funnyRectObj1, counter
    background(255)
    fill(50)
    objX = mouseX + sin(counter)*150
    objY = mouseY + cos(counter)*150
    funnyRectObj.setCenter(mouseX, mouseY)
    funnyRectObj.render()
    funnyRectObj1.setCenter(objX, objY)
    funnyRectObj1.render()
    counter += 0.05
