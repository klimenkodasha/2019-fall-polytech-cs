class MySuperBall:
    x, y, radius, speed, counter = 0, 0, 0, 0, 0
    previousBall = 0
    vector = 1
    
    def render(self):
        noStroke()
        fill(200,100)
        ellipse(self.x, self.y, self.radius, self.radius)
        stroke(0)
        strokeWeight(1)
        if self.previousBall != 0:
            line(self.x, self.y, self.previousBall.x, self.previousBall.y)
            noStroke()
        fill(0)
        ellipse(self.x, self.y, 6, 6)
            
    def upDate(self):
        self.counter += self.speed*self.vector/500.0
        self.y = 250 +sin(self.counter)*200
        if self.counter > TWO_PI:
            self.vector *= -1
            
ballArray_one, ballArray_two = [], []

def setup():
    size(500, 500)
    smooth()
    myInit()
    
def myInit():
    global ballArray_one, ballArray_two
    number = 125
    step = float(width)/float(number)
    ballArray_one = [0 for j in range(number)]
    for i in range(len(ballArray_one)):
        tmp_obj = MySuperBall()
        variable = random(0, 5)
        tmp_obj.x = variable + step*i
        tmp_obj.y = random(-100,100)+250
        tmp_obj.radius = variable*10 + 5
        tmp_obj.speed = random(0.2,10)
        if i > 0:
            tmp_obj.previousBall = ballArray_one[i-1]
        ballArray_one[i] = tmp_obj
    ballArray_two = ballArray_one
    
def draw():
    global ballArray_one
    background(40)
    for currentBall in ballArray_one:
        currentBall.upDate()
        currentBall.render()
        
def keyPressed():
    if key=='a':
        myInit()
    if key=='q':
        ballArray_two[0].radius = 300
    if key=='s':
        saveFrame('70.png')
