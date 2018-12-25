#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : draw_rect.py
# @Date  : 2018/12/25

import sys
import time
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Rectangle")
pos_x = 300
pos_y = 250
vel_x = 2
vel_y = 1

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill((0, 0, 200))

    # move Rectangle

    pos_x += vel_x
    pos_y += vel_y
    # keep the rectangle in screen
    if pos_x > 500 or pos_x < 0:
        vel_x = - vel_x
    if pos_y > 400 or pos_y < 0:
        vel_y = - vel_y
    time.sleep(0.005)
    # draw the rectangle
    color = 255, 255, 0
    width = 0     # solid fill
    pos = pos_x, pos_y, 100, 100
    # 参数列表 表面, 颜色, 位置( x, y, 宽, 高), 边的粗细
    pygame.draw.rect(screen, color, pos, width)
    pygame.display.update()
