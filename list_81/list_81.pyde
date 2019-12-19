drawingSVG = PShape()
def setup():
    global drawingSVG
    background(100)
    smooth()
    strokeWeight(1)
    drawingSVG = loadShape('drawing.svg')
    size(500, 500)
    
def draw():
    global drawingSVG
    fill(10,15)
    rect(0,0,width, height)
    mCursor = map(mouseX, 0, width, 100, 155)
    fill(10,100)
    drawingSVG.disableStyle()
    shape(drawingSVG, 0, 0)
    border = drawingSVG.getChild("path3721")
    for i in range(border.getVertexCount()):
        vx = border.getVertexX(i)*3+20
        vy = border.getVertexY(i)*3+15
        lx = vx + random(-150, 150)
        ly = vy + random(-150, 150)
        lineColor = mCursor + random(-100, 100)
        stroke(lineColor ,100)
        line(vx, vy, lx, ly)
        fill(200, 50)
        noStroke()
        ellipse(vx, vy, 3,3)
