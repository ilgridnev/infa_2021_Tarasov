import turtle as trt


trt.shape(
    'circle')
trt.speed(
    10)

x = -300
y = 0.1

trt.goto(400, 0)
trt.goto(x, 0)

dt = 0.1
Vy = 60
Vx = 20
ay = -10

for i in range(8):
    while y > 0:
        x += Vx * dt
        y += Vy*dt + ay*dt**2/2
        Vy += ay*dt
        if y <= 0:
            y = 0
        trt.goto(x, y)
    Vy = -Vy * 0.8
    Vx *= 0.75
    y = 0.1