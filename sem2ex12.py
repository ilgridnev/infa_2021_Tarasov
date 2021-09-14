import turtle as trt
import math

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

radius_big = 30
radius_small = 5
q = 0
n = 10

for i in range(n):
    Dugin(radius_big, q)
    Dugin(radius_small, q)



