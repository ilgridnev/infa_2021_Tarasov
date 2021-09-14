import turtle as trt
import math

def Corn_God(rad, n):
    corn = 360 / n
    side = math.sin((corn / 2) / 180 * math.pi) * 2 * rad
    trt.pendown()
    trt.left(90 - corn / 2)
    for i in range(n):
        trt.left(corn)
        trt.forward(side)
    trt.right(90 - corn / 2)
    trt.penup()


trt.shape('turtle')
trt.speed(5)

radius = 50
add = 25

for n in range(3, 12, 1):
    Corn_God(radius, n)
    radius += add
    trt.forward(add)

