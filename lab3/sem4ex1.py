import pygame as pog

pog.init()

FPS = 30
screen = pog.display.set_mode((500, 500))

white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

pog.draw.rect(screen, white, (0, 0, 500, 500))
pog.draw.circle(screen, yellow, (250, 250), 200)
pog.draw.circle(screen, black, (250, 250), 200, 1)
pog.draw.rect(screen, black, (150, 350, 200, 40))
pog.draw.circle(screen, red, (340, 200), 30)
pog.draw.circle(screen, black, (340, 200), 30, 1)
pog.draw.circle(screen, black, (340, 200), 15)
pog.draw.circle(screen, red, (150, 200), 40)
pog.draw.circle(screen, black, (150, 200), 15)
pog.draw.circle(screen, black, (150, 200), 40, 1)
pog.draw.polygon(screen, black, [(50, 100), (200, 182),
                                 (210, 172), (60, 90)])
pog.draw.polygon(screen, black, [(270, 193), (260, 183),
                                 (450, 120), (460, 130)])
pog.display.update()
clock = pog.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pog.event.get():
        if event.type == pog.QUIT:
            finished = True

pog.quit()
