class FunnyRect:
    cx, cy, fsize = 0, 0, 0
    
    def setCenter(self, x, y):
        self.cx = x
        self.cy = y
    
    def setSize(self,s):
        self.fsize = s
    
    def render(self):
        rect(self.cx, self.cy, self.fsize, self.fsize)
        
funnyRectObj = FunnyRect()

def setup():
    global funnyRectObj
    size(600, 600)
    smooth()
    noStroke()
    rectMode(CENTER)
    funnyRectObj.setSize(50)
    
def draw():
    global funnyRectObj
    background(255)
    fill(50)
    funnyRectObj.setCenter(mouseX, mouseY)
    funnyRectObj.render()
