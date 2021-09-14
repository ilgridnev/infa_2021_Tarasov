import turtle as trt
import math

def Circus(rad, q):
    corn = 5
    for i in range(72):
        trt.forward(rad * (corn / 180 * math.pi))
        if q == 1:
            trt.left(corn)
        else:
            trt.right(corn)

def Dugin(rad, q):
    corn = 5
    for i in range(36):
        trt.forward(rad * (corn / 180 * math.pi))
        if q == 1:
            trt.left(corn)
        else:
            trt.right(corn)


trt.shape('turtle')
trt.speed(10)
trt.left(90)

radius_face = 100
radius_eye = 15
radius_mouth = 50
q = 1
n = 10

trt.penup()
trt.goto(0, -50)
trt.color('black')
trt.pendown()
trt.forward(100)
trt.penup()
trt.goto(-50, 0)
trt.right(90)
trt.pendown()
trt.forward(100)
trt.left(90)
trt.penup()

trt.penup()
trt.goto(radius_face, 0)
trt.pendown()

trt.color('yellow')
trt.begin_fill()
Circus(radius_face, q)
trt.end_fill()

trt.penup()
trt.goto(-40, 40)
trt.pendown()

trt.color('blue')
trt.begin_fill()
Circus(radius_eye, q)
trt.end_fill()

trt.penup()
trt.goto(40, 40)
trt.pendown()

trt.color('red')
trt.begin_fill()
q = 0
Circus(radius_eye, q)
trt.end_fill()

trt.penup()
trt.goto(0, -20)
trt.width(7)
trt.color('black')
trt.pendown()
trt.forward(40)
trt.penup()
trt.goto(radius_mouth, -int(radius_mouth / 2))
trt.right(180)
trt.pendown()
trt.color('cyan')
Dugin(radius_mouth, q)
