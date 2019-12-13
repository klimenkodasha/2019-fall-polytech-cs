a = [[0 for j in range(2)] for i in range(500)]
def setup():
    global a
    size(500, 500)
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = random(10,490)

def draw():
    global a
    background(0)
    smooth()
    noStroke()
    for i in range(len(a)):
        eDist = dist(mouseX, mouseY, a[i][0], a[i][1])
        eSize = map(eDist, 0, 200, 5, 100)
        eColor = map(eDist, 0, 200, 50, 255)
        fill(eColor, 200)
        cx = noise(mouseX)*10 + a[i][0]
        cy = noise(mouseY)*10 + a[i][1]
        ellipse(cx, cy, eSize, eSize)
