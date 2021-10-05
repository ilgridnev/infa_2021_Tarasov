import pygame as pog

pog.init()

FPS = 30
screen = pog.display.set_mode((550, 750))

white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
green = (55, 200, 113)
blue = (95, 188, 211)
red = (255, 0, 0)
brown = (200, 171, 55)
bull = (108, 103, 83)


def fence(
        fence_start_x,
        fence_start_y,
        fence_alfa
):
    '''
    Функция рисует забор на экране.
    sсreen - объект, соответсвующий отображаемому дисплею
    fence_start_x, fence_start_y, - координаты левого верхнего угла изображения
    fence_alfa - параметр пропорционального увеличения/уменьшения размера
    выбран стандартный для забора цвет
    '''
    pog.draw.rect(
        screen,
        (200, 171, 55),
        (fence_start_x, fence_start_y,
         45 * fence_alfa, 30 * fence_alfa)
    )
    pog.draw.line(
        screen,
        black,
        (fence_start_x,
         fence_start_y + 30 * fence_alfa),
        (fence_start_x + 45 * fence_alfa,
         fence_start_y + 30 * fence_alfa)
    )
    h = 4 * fence_alfa
    x = fence_start_x + 4 * fence_alfa

    while x < fence_start_x + 45 * fence_alfa:
        pog.draw.line(
            screen,
            (0, 0, 0),
            (x, fence_start_y),
            (x, fence_start_y + 30 * fence_alfa)
        )
        x += h


def bulldog(
        bull_start_x,
        bull_start_y,
        bull_size,
        bull_orient
):
    '''
    Функция рисует бульдога на экране.
    bull_start_x - х координата вернего дальнего угла головы, где "дальний" означает противоположный от тела"
    bull_start_y - у координата верхней грани головы
    bull_size - параметр пропорционального увеличения размера
    bull_orient - переменная, принимающая значения 0 или 1, для того чтобы пес смотрел влево и вправо соответственно
    '''
    bull = (108, 103, 83)
    black = (0, 0, 0)
    white = (255, 255, 255)
    pog.draw.rect(
        screen,
        bull,
        (bull_start_x - 8 * bull_size * bull_orient,
         bull_start_y,
         8 * bull_size,
         8 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x - 16 * bull_size * bull_orient,
         bull_start_y + 4 * bull_size,
         16 * bull_size,
         6 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x - bull_size - 2 * bull_size * bull_orient,
         bull_start_y + 6 * bull_size,
         4 * bull_size,
         9 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x + 6 * bull_size - 15 * bull_size * bull_orient,
         bull_start_y + 8 * bull_size,
         4 * bull_size, 9 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x + 11 * bull_size - 30 * bull_size * bull_orient,
         bull_start_y + 3 * bull_size,
         8 * bull_size, 5 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x + 11 * bull_size - 26 * bull_size * bull_orient,
         bull_start_y + 3 * bull_size,
         4 * bull_size, 4 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x + 16 * bull_size - 36 * bull_size * bull_orient,
         bull_start_y + 5 * bull_size,
         4 * bull_size, 5 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x + 18 * bull_size - 38 * bull_size * bull_orient,
         bull_start_y + 9 * bull_size,
         2 * bull_size, 5 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x + 13 * bull_size - 28 * bull_size * bull_orient,
         bull_start_y + 7 * bull_size,
         2 * bull_size, 5 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x + 16 * bull_size - 35 * bull_size * bull_orient,
         bull_start_y + 13 * bull_size,
         3 * bull_size, 1.5 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x + 11 * bull_size - 25 * bull_size * bull_orient,
         bull_start_y + 11 * bull_size,
         3 * bull_size, 1.5 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x - 3 * bull_size + bull_size * bull_orient,
         bull_start_y + 14 * bull_size,
         5 * bull_size, 2 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x + 4 * bull_size - 12 * bull_size * bull_orient,
         bull_start_y + 16 * bull_size,
         5 * bull_size, 2 * bull_size)
    )
    pog.draw.rect(
        screen,
        black,
        (bull_start_x - 8 * bull_size * bull_orient,
         bull_start_y,
         8 * bull_size, 8 * bull_size),
        1
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x - bull_size - 8 * bull_size * bull_orient,
         bull_start_y,
         2 * bull_size, 3 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        black,
        (bull_start_x - bull_size - 8 * bull_size * bull_orient,
         bull_start_y,
         2 * bull_size, 3 * bull_size),
        1
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x + 7 * bull_size - 8 * bull_size * bull_orient,
         bull_start_y,
         2 * bull_size, 3 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        black,
        (bull_start_x + 7 * bull_size - 8 * bull_size * bull_orient,
         bull_start_y,
         2 * bull_size, 3 * bull_size),
        1
    )
    pog.draw.ellipse(
        screen,
        white,
        (bull_start_x + 1.5 * bull_size - 5 * bull_size * bull_orient,
         bull_start_y + 3 * bull_size,
         2 * bull_size, bull_size)
    )
    pog.draw.ellipse(
        screen,
        black,
        (bull_start_x + 1.5 * bull_size - 5 * bull_size * bull_orient,
         bull_start_y + 3 * bull_size,
         2 * bull_size, bull_size),
        1
    )
    pog.draw.ellipse(
        screen,
        black,
        (bull_start_x + 2 * bull_size - 5 * bull_size * bull_orient,
         bull_start_y + 3 * bull_size,
         bull_size, bull_size)
    )
    pog.draw.ellipse(
        screen,
        white,
        (bull_start_x + 4.5 * bull_size - 11 * bull_size * bull_orient,
         bull_start_y + 3 * bull_size,
         2 * bull_size, bull_size)
    )
    pog.draw.ellipse(
        screen,
        black,
        (bull_start_x + 4.5 * bull_size - 11 * bull_size * bull_orient,
         bull_start_y + 3 * bull_size,
         2 * bull_size, bull_size),
        1
    )
    pog.draw.ellipse(
        screen,
        black,
        (bull_start_x + 5 * bull_size - 11 * bull_size * bull_orient,
         bull_start_y + 3 * bull_size,
         bull_size, bull_size)
    )
    pog.draw.arc(
        screen,
        black,
        (bull_start_x + bull_size - 8 * bull_size * bull_orient,
         bull_start_y + 6 * bull_size,
         6 * bull_size, 4 * bull_size),
        0.4, 2.75
    )
    pog.draw.polygon(
        screen,
        white,
        [
            (bull_start_x + 2.3 * bull_size - 4.6 * bull_size * bull_orient,
             bull_start_y + 6.2 * bull_size),
            (bull_start_x + 1.7 * bull_size - 3.4 * bull_size * bull_orient,
             bull_start_y + 6.6 * bull_size),
            (bull_start_x + 1.7 * bull_size - 3.4 * bull_size * bull_orient,
             bull_start_y + 5.3 * bull_size)
        ]
    )
    pog.draw.polygon(
        screen,
        white,
        [
            (bull_start_x + 5.7 * bull_size - 11.4 * bull_size * bull_orient,
             bull_start_y + 6.2 * bull_size),
            (bull_start_x + 6.3 * bull_size - 12.6 * bull_size * bull_orient,
             bull_start_y + 6.6 * bull_size),
            (bull_start_x + 6.3 * bull_size - 12.6 * bull_size * bull_orient,
             bull_start_y + 5.3 * bull_size)
        ]
    )
    pog.draw.polygon(
        screen,
        black,
        [
            (bull_start_x + 2.3 * bull_size - 4.6 * bull_size * bull_orient,
             bull_start_y + 6.2 * bull_size),
            (bull_start_x + 1.7 * bull_size - 3.4 * bull_size * bull_orient,
             bull_start_y + 6.6 * bull_size),
            (bull_start_x + 1.7 * bull_size - 3.4 * bull_size * bull_orient,
             bull_start_y + 5.3 * bull_size)
        ],
        1
    )
    pog.draw.polygon(
        screen,
        white,
        [
            (bull_start_x + 5.7 * bull_size - 11.4 * bull_size * bull_orient,
             bull_start_y + 6.2 * bull_size),
            (bull_start_x + 6.3 * bull_size - 12.6 * bull_size * bull_orient,
             bull_start_y + 6.6 * bull_size),
            (bull_start_x + 6.3 * bull_size - 12.6 * bull_size * bull_orient,
             bull_start_y + 5.3 * bull_size)
        ],
        1
    )


pog.draw.rect(
    screen,
    blue,
    (0, 0, 600, 600)
)
pog.draw.rect(
    screen,
    green,
    (0, 250, 550, 600)
)

fence(100, 10, 12)
fence(0, 200, 7)
fence(300, 300, 6)
fence(0, 320, 6)

bulldog(550, 450, 4, 1)

pog.draw.polygon(
    screen,
    brown,
    [(460, 360), (420, 380),
     (470, 460), (510, 440)
     ]
)
pog.draw.polygon(
    screen,
    brown,
    [(420, 380), (470, 460),
     (360, 440)
     ]
)
pog.draw.polygon(
    screen,
    brown,
    [(470, 460), (510, 440),
     (510, 530), (470, 590)
     ]
)
pog.draw.polygon(
    screen,
    brown,
    [(360, 440), (470, 460),
     (470, 590), (360, 550)
     ]
)
pog.draw.polygon(
    screen,
    black,
    [(470, 460), (510, 440),
     (510, 530), (470, 590)
     ],
    2
)
pog.draw.polygon(
    screen,
    black,
    [(460, 360), (420, 380),
     (470, 460), (510, 440)
     ],
    1
)
pog.draw.polygon(
    screen,
    black,
    [(420, 380), (470, 460),
     (360, 440)
     ],
    1
)
pog.draw.polygon(
    screen,
    black,
    [(360, 440), (470, 460),
     (470, 590), (360, 550)
     ],
    2
)
pog.draw.ellipse(
    screen,
    black,
    (385, 475, 55, 70)
)

pog.draw.ellipse(
    screen,
    black,
    (375, 530, 20, 10),
    1
)
pog.draw.ellipse(
    screen,
    black,
    (360, 545, 20, 15),
    1
)
pog.draw.ellipse(
    screen,
    bull,
    (370, 535, 15, 20)
)
pog.draw.ellipse(
    screen,
    black,
    (370, 535, 15, 20),
    1
)
pog.draw.ellipse(
    screen,
    black,
    (350, 555, 20, 10),
    1
)
pog.draw.ellipse(
    screen,
    black,
    (350, 560, 10, 10),
    1
)
pog.draw.ellipse(
    screen,
    black,
    (330, 565, 25, 10),
    1
)
pog.draw.ellipse(
    screen,
    black,
    (315, 568, 20, 10),
    1
)
pog.draw.ellipse(
    screen,
    black,
    (295, 570, 25, 5),
    1
)
pog.draw.ellipse(
    screen,
    black,
    (290, 565, 10, 15),
    1
)
pog.draw.ellipse(
    screen,
    black,
    (275, 575, 20, 5),
    1
)
pog.draw.ellipse(
    screen,
    black,
    (265, 575, 20, 10),
    1
)

bulldog(50, 400, 10, 0)
bulldog(300, 550, 8, 1)
bulldog(330, 530, 25, 0)
pog.display.update()
clock = pog.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pog.event.get():
        if event.type == pog.QUIT:
            finished = True

pog.quit()
