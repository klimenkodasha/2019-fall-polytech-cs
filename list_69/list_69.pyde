class MySuperBall:
    x, y, radius, speed = 0, 0, 0, 0
    previousBall = 0
    vector = 1
    
    def render(self):
        noStroke()
        fill(200,100)
        ellipse(self.x, self.y, self.radius, self.radius)
        stroke(10)
        strokeWeight(2)
        if self.previousBall != 0:
            line(self.x, self.y, self.previousBall.x, self.previousBall.y)
            noStroke()
            fill(0)
            ellipse(self.x, self.y, 6, 6)
            
    def upDate(self):
        self.y += self.speed*self.vector
        if self.y>500 or self.y<0:
            self.vector *= -1
            
step = 30
ballArray_one, ballArray_two = [], []

def setup():
    size(500, 500)
    smooth()
    myInit()
    
def myInit():
    global ballArray_one, ballArray_two
    ballArray_one = [0 for j in range(15)]
    for i in range(len(ballArray_one)):
        tmp_obj = MySuperBall()
        variable = random(5, 30)
        tmp_obj.x = variable + step*i + 20
        tmp_obj.y = random(-100,100)+100
        tmp_obj.radius = variable*2 + 10
        tmp_obj.speed = random(0.2,10)
        if i > 0:
            tmp_obj.previousBall = ballArray_one[i-1]
        ballArray_one[i] = tmp_obj
    ballArray_two = ballArray_one
    
def draw():
    global ballArray_one
    background(50)
    for currentBall in ballArray_one:
        currentBall.upDate()
        currentBall.render()
        
def keyPressed():
    if key=='a':
        myInit()
    if key=='q':
        ballArray_two[0].radius = 300
