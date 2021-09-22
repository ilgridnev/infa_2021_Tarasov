import turtle as trt
import math as mp

trt.shape(
    'turtle')
trt.speed(
    10)
trt.color('blue')
trt.width(5)

trt.penup()
trt.goto(-300, 0)
trt.pendown()

SIDE = 30
DIAG = SIDE * mp.sqrt(2)
SPACE = 20


def middle_side(q):
    trt.penup()
    if q == 1:
        trt.pendown()
    trt.forward(
        SIDE)
    trt.right(
        135)


def diag_side(q):
    trt.penup()
    if q == 1:
        trt.pendown()
    trt.forward(
        DIAG)
    trt.left(
        135)


def turn_side(q):
    trt.penup()
    if q == 1:
        trt.pendown()
    trt.forward(
        SIDE)
    trt.left(90)


def just_side(q):
    trt.penup()
    if q == 1:
        trt.pendown()
    trt.forward(
        SIDE)


def end_side(q):
    trt.penup()
    if q == 1:
        trt.pendown()
    trt.forward(SIDE)
    trt.penup()
    trt.right(180)
    trt.forward(SIDE * 2)
    trt.right(90)
    trt.forward(SIDE + SPACE)

writer = (
    middle_side, diag_side, middle_side,
    diag_side, turn_side, just_side,
    turn_side, turn_side, just_side,
    end_side
)
zero = (
    1, 0, 0,
    0, 1, 1,
    1, 0, 1,
    1
)
one = (
    0, 1, 0,
    0, 0, 1,
    1, 0, 0,
    0
)
two = (
    1, 0, 0,
    1, 1, 0,
    1, 0, 0,
    0
)
three = (
    1, 1, 1,
    1, 0, 0,
    0, 0, 0,
    0
)
four = (
    0, 0, 1,
    0, 0, 1,
    1, 0, 1,
    0
)
five = (
    1, 0, 1,
    0, 1, 1,
    0, 0, 1,
    0
)
six = (
    0, 1, 1,
    0, 1, 1,
    0, 0, 0,
    1
)
seven = (
    1, 1, 0,
    0, 0, 0,
    0, 0, 0,
    1
)
eight = (
    1, 0, 1,
    0, 1, 1,
    1, 0, 1,
    1
)
nine = (
    1, 0, 1,
    1, 0, 0,
    1, 0, 1,
    0
)
number = [
    zero, one, two,
    three, four, five,
    six, seven, eight,
    nine
]
ex = '141700'
for k in range(len(ex)):
    for i in range(len(writer)):
        writer[i](number[int(ex[k])][i])


