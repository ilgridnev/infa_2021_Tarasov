import turtle as trt
import math

trt.shape('turtle')
trt.speed(5)


def Nemesis(line, num):
    for k in range(num):
        trt.forward(line)
        trt.left(180 - 180 / num)


side = 200
n1 = 5
n2 = 11
trt.left(180)

Nemesis(side, n1)

trt.penup()
trt.goto(10, 0)
trt.left(180)
trt.pendown()

Nemesis(side, n2)

trt.left(1080)
