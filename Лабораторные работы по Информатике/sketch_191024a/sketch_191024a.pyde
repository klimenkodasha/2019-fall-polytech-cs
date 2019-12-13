def setup() :
    size(800, 800)
    noLoop()
    

def draw(): 

    background(700)
    smooth()
    strokeWeight(50)
    stroke(200)

    translate(width/2, height/2 - 100)
    line(-100,0,100,0)

    translate(0, 100)
    scale(1.5, 1.5)
    line(-100,0,100,0)

    translate(0, 100)
    scale(1.5, 1.5)
    line(-100,0,100,0)
 
