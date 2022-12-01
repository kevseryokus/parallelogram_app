
def rightSlash (piece):
    for i in range(int(piece)):
        print("/",end="")


def leftSlash (piece):
    for i in range(int(piece)):
        print("\\",end="")

def skipLine(piece):
    for i in range(int(piece)):
        print()

def space(piece):
    for i in range(int(piece)):
        print(" ",end="")

def upSide(diameter):
    startingSpace = diameter/2-1
    for i in range(int(diameter/2)):
        space(startingSpace-i)
        rightSlash(1)
        space(i*2)
        leftSlash(1)
        skipLine(1)

def lowSide (diameter):
    startingSpace = diameter-2
    for i in range(int(diameter/2)):
        space(i)
        leftSlash(1)
        space(startingSpace-i*2)
        rightSlash(1)
        skipLine(1)

def parallelogram(diameter):
    upSide (diameter)
    lowSide (diameter)

parallelogram(4)
























