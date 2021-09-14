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


print()
print('N - number of pairs')
print('Input N:')
n = int(input())

trt.shape('turtle')
trt.speed(10)

radius = 40
add = 25
q = 1

for i in range(n):
    for k in range(2):
        Circus(radius, q)
        q = math.fabs(q - 1)
    trt.left(360 / (n * 2))



