def setup():
    size(1000, 1000)
    smooth()
    background(0)
    strokeWeight(1)
i = 205
k = 1
flug = 1
def upDate(i,k):
    i=i+k
    if(i==255):
       k=-1
    if(i==0):
       k=1
    
def draw ():
    global i, k, flug
    stroke(i, 250)
    if (flug == 1):  
        line(mouseX , mouseY , 500, random(0,500))
    else: 
        line(mouseX , mouseY , 0, random(0,500))
        upDate(i,k)
        
def keyPressed():
    global flug 
    if (key=='q'):
        flug = -flug
   
 
