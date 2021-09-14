import turtle as trt

trt.shape('turtle')
trt.speed(10)
line = 0.1
corner = 5

for i in range(3600):
    trt.forward(line)
    trt.left(corner)
    line += corner / 1000
