#Pixel Art - http://www.101computing.net/pixel-art-in-python/

import turtle

pen = turtle.Turtle()
screen = turtle.Screen()

BOXSIZE = 2

pen.speed(0)
pen.color("#000000")

screen.tracer(100,0)

# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
    pen.begin_fill()
    # 0 deg.
    pen.forward(intDim)
    pen.left(90)
    # 90 deg.
    pen.forward(intDim)
    pen.left(90)
    # 180 deg.
    pen.forward(intDim)
    pen.left(90)
    # 270 deg.
    pen.forward(intDim)
    pen.end_fill()
    pen.setheading(0)
    return


# for i in range(50):
#     pen.forward(i*10)
#     pen.right(123)


#Here is how your PixelArt is stored (using a "list of lists")
pixels     = [[0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0]]
pixels.append([0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0])
pixels.append([0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,0])
pixels.append([0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,0])
pixels.append([0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0])
pixels.append([1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1])
pixels.append([1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1])
pixels.append([1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1])
pixels.append([1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1])
pixels.append([1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1])
pixels.append([1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1])
pixels.append([1,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1])
pixels.append([0,1,1,0,0,0,1,0,0,1,0,0,0,1,1,0])
pixels.append([0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0])
pixels.append([0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0])
pixels.append([0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0])





def printPixels(pixels):   
    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            if pixels[i][j] == 1:
                box(BOXSIZE)
            pen.penup()
            pen.forward(BOXSIZE)
            pen.pendown()	
        pen.penup()
        pen.backward(BOXSIZE*len(pixels[i]))
        pen.right(90)
        pen.forward(BOXSIZE)
        pen.left(90)
        pen.pendown()
    return

pen.penup()
# pen.setpos(-310,290)
pen.setpos(300,-250)
pen.pendown()

printPixels(pixels)
print(pen.pos())

turtle.done()

# 	