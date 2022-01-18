from pygame import *
import random


init()
sc = display.set_mode([1000, 1000])
flag = True
sc.fill((0, 0, 0))
fps = 24
clock = time.Clock()
while flag:
    for ev in event.get():
        if ev.type == QUIT:
            flag = False
            break
    display.flip()
    clock.tick(fps)