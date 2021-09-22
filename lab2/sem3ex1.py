import turtle as trt
import random as rnd

trt.shape(
    'turtle')
trt.speed(
    10)

TIMER = 500

for i in range(
        TIMER):
    angle = 360 * rnd.random()
    leng = 50 * rnd.random() + 1
    trt.forward(
        leng)
    trt.left(
        angle)




