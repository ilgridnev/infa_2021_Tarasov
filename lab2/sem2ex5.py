import turtle as trt

trt.shape('turtle')

a = 30
b = 10


for i in range(10):
    for k in range(4):
        trt.left(90)
        trt.forward(a)
    trt.penup()
    trt.forward(b)
    trt.right(90)
    trt.forward(b)
    trt.left(90)
    a += 2*b
    trt.pendown()
