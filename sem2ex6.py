import turtle as trt


print('Insert n:')
legs = int(input())
arm = 100
corner = 360 / legs
trt.shape('turtle')

for i in range(legs):
    trt.forward(arm)
    trt.stamp()
    trt.right(180)
    trt.forward(arm)
    trt.left(180 - corner)
