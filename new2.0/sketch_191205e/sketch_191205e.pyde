def setup ():
    size (800, 800)
    smooth ()               
    background (0)
    strokeWeight (1)
 
i = 205
k = 1
flug = 1
def upDate (i,k):
    i = i + k
    if(i == 255):
       k=-1
    if(i == 0):
       k=1


def draw ():
    global myRandom, myY1, myY2
    stroke(200, 10)
    myRandom = random (-20,20)
    myY1 = mouseY - myRandom
    myY2 = mouseY + myRandom
    line(10, myY1 , 500, myY2)
    upDate (i,k)
