num = 60
mx, my =  [0 for x in range(num)], [0 for x in range(num)]

def setup():
    size(640, 360)
    noStroke()
    fill(255, 153)

def draw():
    global mx, my, num
    background(51)
    which = frameCount % num
    mx[which] = mouseX
    my[which] = mouseY
    for i in range(num):
        index = (which + 1 + i)%num
        ellipse(mx[index], my[index], i, i)
