from pygame import *
import random
import PyQt5


class Circle:
    def __init__(self, x1, y1, x, y):
        self.x = x
        self.y = y
        self.xx = (x - x1) / 100
        self.yy = (y - y1) / 100
        self.color = (0, 255, 0)

    def move(self, step):
        self.x += step * self.xx
        if self.y > 985:
            self.xx *= 0.999
        self.y += step * self.yy
        while not 10 < self.x < 990 or not 10 < self.y < 990:
            if self.x < 10:
                self.x = 20 - self.x
                self.xx *= -1
                self.xx *= 0.7
            if self.y < 10:
                self.y = 20 - self.y
                self.yy *= -1
            if self.x > 990:
                self.x = 1980 - self.x
                self.xx *= -1
                self.xx *= 0.9
            if self.y > 990:
                self.y = 1980 - self.y
                self.yy *= -1
                self.yy *= 0.7
            if self.yy <= 990:
                self.yy = self.yy + step / 1000
        v = (abs(self.xx) + abs(self.yy)) / 5
        self.color = (min(255, v * 255), max(0, 255 - v * 255), 0)

    def draw(self):
        draw.circle(sc, self.color, (i.x, i.y), r)


init()
sc = display.set_mode([1000, 1000])
flag = True
sc.fill((0, 0, 0))
fps = 24
clock = time.Clock()
cir_list = []
r = 10
draw_yellow = False
move = True
while flag:
    for ev in event.get():
        if ev.type == QUIT:
            flag = False
            break
        elif ev.type == MOUSEBUTTONDOWN:
            x, y = mouse.get_pos()
            startx = x
            starty = y
            draw_yellow = True
        elif ev.type == MOUSEBUTTONUP:
            x, y = mouse.get_pos()
            cir = Circle(startx, starty, x, y)
            cir_list.append(cir)
            draw_yellow = False
        elif ev.type == MOUSEMOTION:
            x, y = mouse.get_pos()
        elif ev.type == KEYDOWN:
            if ev.key == K_SPACE:
                move = not move
            elif ev.key == K_x:
                for i in cir_list:
                    i.yy += 1
                    i.yy *= 2
                    i.xx += 1
                    i.xx *= 2
    sc.fill((0, 0, 0))
    step = int(clock.tick())
    for i in cir_list:
        if move:
            i.move(step)
        i.draw()
    if draw_yellow:
        cir = Circle(startx, starty, x, y)
        cir_list.append(cir)
        draw.circle(sc, (155, 0, 0), (startx, starty), r)
        draw.circle(sc, (155, 155, 0), (x, y), r)
    display.flip()
    print(len(cir_list))