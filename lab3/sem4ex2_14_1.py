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

fence_alfa = 13
fence_start_y = 100
fence_start_x = 0

pog.draw.rect(screen, blue, (0, 0, 600, 500))
pog.draw.rect(screen, green, (0, 150, 550, 600))
pog.draw.rect(screen, brown, (fence_start_x, fence_start_y, 45*fence_alfa, 30*fence_alfa))
pog.draw.line(screen, black, (fence_start_x, fence_start_y + 30 * fence_alfa), (fence_start_x + 45 * fence_alfa, fence_start_y + 30 * fence_alfa))

h = 4 * fence_alfa
x = fence_start_x + 4 * fence_alfa

while x < fence_start_x + 45 * fence_alfa:
    pog.draw.line(screen, black, (x, fence_start_y),  (x, fence_start_y + 30*fence_alfa))
    x += h

pog.draw.polygon(screen, brown, [(460, 360), (420, 380),
                                 (470, 460), (510, 440)])
pog.draw.polygon(screen, brown, [(420, 380), (470, 460),
                                 (360, 440)])
pog.draw.polygon(screen, brown, [(470, 460), (510, 440),
                                 (510, 530), (470, 590)])
pog.draw.polygon(screen, brown, [(360, 440), (470, 460),
                                 (470, 590), (360, 550)])
pog.draw.polygon(screen, black, [(470, 460), (510, 440),
                                 (510, 530), (470, 590)], 2)
pog.draw.polygon(screen, black, [(460, 360), (420, 380),
                                 (470, 460), (510, 440)], 1)
pog.draw.polygon(screen, black, [(420, 380), (470, 460),
                                 (360, 440)], 1)
pog.draw.polygon(screen, black, [(360, 440), (470, 460),
                                 (470, 590), (360, 550)], 2)
pog.draw.ellipse(screen, black, (385, 475, 55, 70))

pog.draw.ellipse(screen, black, (375, 530, 20, 10), 1)
pog.draw.ellipse(screen, black, (360, 545, 20, 15), 1)
pog.draw.ellipse(screen, bull, (370, 535, 15, 20))
pog.draw.ellipse(screen, black, (370, 535, 15, 20), 1)
pog.draw.ellipse(screen, black, (350, 555, 20, 10), 1)
pog.draw.ellipse(screen, black, (350, 560, 10, 10), 1)
pog.draw.ellipse(screen, black, (330, 565, 25, 10), 1)
pog.draw.ellipse(screen, black, (315, 568, 20, 10), 1)
pog.draw.ellipse(screen, black, (295, 570, 25, 5), 1)
pog.draw.ellipse(screen, black, (290, 565, 10, 15), 1)
pog.draw.ellipse(screen, black, (275, 575, 20, 5), 1)
pog.draw.ellipse(screen, black, (265, 575, 20, 10), 1)

bull_start_x = 50
bull_start_y = 550
bull_orient = 0
bull_size = 10

pog.draw.rect(screen, bull, (bull_start_x - 8 * bull_size * bull_orient,
                             bull_start_y,
                             8*bull_size, 8*bull_size))
pog.draw.ellipse(screen, bull, (bull_start_x - 16 * bull_size * bull_orient,
                                 bull_start_y + bull_size*4,
                                 bull_size*16, bull_size*6))
pog.draw.ellipse(screen, bull, (bull_start_x - bull_size - 2 * bull_size * bull_orient,
                                 bull_start_y + bull_size * 6,
                                 bull_size * 4, bull_size * 9))
pog.draw.ellipse(screen, bull, (bull_start_x + 6 * bull_size - 15 * bull_size * bull_orient,
                                 bull_start_y + bull_size * 8,
                                 bull_size * 4, bull_size * 9))
pog.draw.ellipse(screen, bull, (bull_start_x + 11 * bull_size - 30 * bull_size * bull_orient,
                                bull_start_y + 3 * bull_size,
                                bull_size * 8, bull_size * 5))
pog.draw.ellipse(screen, bull, (bull_start_x + 11 * bull_size - 26 * bull_size * bull_orient,
                                bull_start_y + 3 * bull_size,
                                bull_size * 4, bull_size * 4))
pog.draw.ellipse(screen, bull, (bull_start_x + 16 * bull_size - 36 * bull_size * bull_orient,
                                bull_start_y + 5 * bull_size,
                                4 * bull_size, 5 * bull_size))
pog.draw.ellipse(screen, bull, (bull_start_x + 18 * bull_size - 38 * bull_size * bull_orient,
                                bull_start_y + 9 * bull_size,
                                bull_size * 2, bull_size * 5))
pog.draw.ellipse(screen, bull, (bull_start_x + 13 * bull_size - 28 * bull_size * bull_orient,
                                bull_start_y + 7 * bull_size,
                                bull_size * 2, bull_size * 5))
pog.draw.ellipse(screen, bull, (bull_start_x + 16 * bull_size - 35 * bull_size * bull_orient,
                                bull_start_y + 13 * bull_size,
                                bull_size * 3, bull_size * 1.5))
pog.draw.ellipse(screen, bull, (bull_start_x + 11 * bull_size - 25 * bull_size * bull_orient,
                                bull_start_y + 11 * bull_size,
                                bull_size * 3, bull_size * 1.5))
pog.draw.ellipse(screen, bull, (bull_start_x - 3 * bull_size + 1 * bull_size * bull_orient,
                                bull_start_y + 14 * bull_size,
                                bull_size * 5, bull_size * 2))
pog.draw.ellipse(screen, bull, (bull_start_x + 4 * bull_size - 12 * bull_size * bull_orient,
                                bull_start_y + 16 * bull_size,
                                bull_size * 5, bull_size * 2))
pog.draw.rect(screen, black, (bull_start_x - 8 * bull_size * bull_orient,
                              bull_start_y,
                             8*bull_size, 8*bull_size), 1)
pog.draw.ellipse(screen, bull, (bull_start_x - bull_size - 8 * bull_size * bull_orient,
                                bull_start_y,
                                bull_size * 2, bull_size * 3))
pog.draw.ellipse(screen, black, (bull_start_x - bull_size - 8 * bull_size * bull_orient,
                                bull_start_y,
                                bull_size * 2, bull_size * 3), 1)
pog.draw.ellipse(screen, bull, (bull_start_x + bull_size * 7 - 8 * bull_size * bull_orient,
                                bull_start_y,
                                bull_size * 2, bull_size * 3))
pog.draw.ellipse(screen, black, (bull_start_x + bull_size * 7 - 8 * bull_size * bull_orient,
                                bull_start_y,
                                bull_size * 2, bull_size * 3), 1)

pog.draw.ellipse(screen, white, (bull_start_x + 1.5 * bull_size - 5 * bull_size * bull_orient,
                                bull_start_y + 3 * bull_size,
                                bull_size * 2, bull_size))
pog.draw.ellipse(screen, black, (bull_start_x + 1.5 * bull_size - 5 * bull_size * bull_orient,
                                bull_start_y + 3 * bull_size,
                                bull_size * 2, bull_size), 1)
pog.draw.ellipse(screen, black, (bull_start_x + 2 * bull_size - 5 * bull_size * bull_orient,
                                bull_start_y + 3 * bull_size,
                                bull_size , bull_size))
pog.draw.ellipse(screen, white, (bull_start_x + 4.5 * bull_size - 11 * bull_size * bull_orient,
                                bull_start_y + 3 * bull_size,
                                bull_size * 2, bull_size))
pog.draw.ellipse(screen, black, (bull_start_x + 4.5 * bull_size - 11 * bull_size * bull_orient,
                                bull_start_y + 3 * bull_size,
                                bull_size * 2, bull_size), 1)
pog.draw.ellipse(screen, black, (bull_start_x + 5 * bull_size  - 11 * bull_size * bull_orient,
                                bull_start_y + 3 * bull_size,
                                bull_size, bull_size))
pog.draw.arc(screen, black, (bull_start_x + bull_size - 8 * bull_size * bull_orient,
                             bull_start_y + 6 * bull_size,
                             bull_size * 6, bull_size * 4), 0.4, 2.75)
pog.draw.polygon(screen, white, [(bull_start_x + 2.3 * bull_size - 4.6 * bull_size * bull_orient,
                                  bull_start_y + 6.2 * bull_size),
                                 (bull_start_x + 1.7 * bull_size - 3.4 * bull_size * bull_orient,
                                  bull_start_y + 6.6 * bull_size),
                                 (bull_start_x + 1.7 * bull_size - 3.4 * bull_size * bull_orient,
                                  bull_start_y + 5.3 * bull_size)])
pog.draw.polygon(screen, white, [(bull_start_x + 5.7 * bull_size - 11.4 * bull_size * bull_orient,
                                  bull_start_y + 6.2 * bull_size),
                                 (bull_start_x + 6.3 * bull_size - 12.6 * bull_size * bull_orient,
                                  bull_start_y + 6.6 * bull_size),
                                 (bull_start_x + 6.3 * bull_size - 12.6 * bull_size * bull_orient,
                                  bull_start_y + 5.3 * bull_size)])
pog.display.update()
clock = pog.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pog.event.get():
        if event.type == pog.QUIT:
            finished = True
        if event.type == pog.MOUSEBUTTONDOWN:
            print(pog.mouse.get_pos())


pog.quit()
