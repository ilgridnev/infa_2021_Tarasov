import random as rnd
import turtle as trt
import math


number_of_parts = 30
steps_of_time_number = 1000

SIDE = 300
dt = 1
alfa = 30
beta = 10

trt.penup()
trt.goto(SIDE, SIDE)
trt.pendown()
trt.goto(SIDE, -SIDE)
trt.goto(-SIDE, -SIDE)
trt.goto(-SIDE, SIDE)
trt.goto(SIDE, SIDE)

pool = [trt.Turtle(shape='circle') for i in range(number_of_parts)]

x = [(rnd.random() - 0.5) * 600 for i in range(number_of_parts)]
y = [(rnd.random() - 0.5) * 600 for i in range(number_of_parts)]
Vx = [(rnd.random() - 0.5) * 20 for i in range(number_of_parts)]
Vy = [(rnd.random() - 0.5) * 20 for i in range(number_of_parts)]

for i in range(number_of_parts):
    pool[i].penup()
    pool[i].speed(50)
    pool[i].goto(x[i], y[i])


for t in range(steps_of_time_number):
    for i in range(len(pool)):
        x[i] += Vx[i] * dt
        y[i] += Vy[i] * dt
        if y[i] + Vy[i]*dt > SIDE or y[i] + Vy[i]*dt < -SIDE:
            Vy[i] = -Vy[i]
        if x[i] + Vx[i]*dt > SIDE or x[i] + Vx[i]*dt < -SIDE:
            Vx[i] = -Vx[i]
        for k in range(len(pool)):
            leng = (x[i] - x[k])*(x[i] - x[k]) + \
                   (y[i] - y[k])*(y[i] - y[k])
            if leng < 900 and leng > 0:
                ax = alfa*(x[i] - x[k]) / leng
                ay = alfa*(y[i] - y[k]) / leng
                Vx[i] += ax * dt
                Vy[i] += ay * dt
            if leng > 0:
                ax = beta*(x[k] - x[i]) / leng
                ay = beta*(y[k] - y[i]) / leng
                Vx[i] += ax * dt
                Vy[i] += ay * dt
        pool[i].goto(x[i], y[i])
