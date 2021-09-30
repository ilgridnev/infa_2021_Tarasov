import turtle as trt
import math as mp

trt.shape(
    'turtle')
trt.speed(
    10)
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

number = [
    'zero.txt', 'one.txt', 'two.txt',
    'three.txt', 'four.txt', 'five.txt',
    'six.txt', 'seven.txt', 'eight.txt',
    'nine.txt'
]


opn = open(
    'number.txt', 'r'
)
example = opn.readline()
example = example.rstrip()

for k in range(len(example)):
    opnum = open(number[int(example[k])], 'r')
    rule = opnum.readline()
    rule = rule.rstrip()

    for i in range(len(writer)):
        writer[i](int(rule[i]))

