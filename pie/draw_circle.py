#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : draw_circle.py
# @Date  : 2018/12/24

import sys
import time
import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Circle")
pos_x = 300
pos_y = 250
vel_x = 2
vel_y = 1
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill((0, 0, 200))

    # move
    radius = 50
    width = 0
    pos_x += vel_x
    pos_y += vel_y
    # keep the circle on the screen
    if pos_x > 600 - radius or pos_x < radius:
        vel_x = -vel_x
    if pos_y > 500 - radius or pos_y < radius:
        vel_y = -vel_y
    time.sleep(0.005)
    # draw circle
    color = 255, 255, 0

    pygame.draw.circle(screen, color, (pos_x, pos_y), radius, width)
    pygame.display.update()
