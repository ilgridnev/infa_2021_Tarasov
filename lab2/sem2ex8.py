import turtle as trt

trt.shape('turtle')
trt.speed(3)
line = 10
corner = 90
add = 3
for i in range(30):
    trt.forward(line)
    trt.left(corner)
    line += add
