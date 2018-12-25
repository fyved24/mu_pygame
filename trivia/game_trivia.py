#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : game_trivia.py
# @Date  : 2018/12/24

import sys
import pygame
from pygame.locals import *

font1 = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 24)
white = 0, 0, 0
cyan = 0, 255, 255
yellow = 255, 255, 0
purple = 255, 0, 255
green = 0, 255, 0
red = 255, 0, 0


class Trivia(object):
    def __init__(self, filename):
        self.data = []
        self.current = 0
        self.total = 0
        self.correct = 0
        self.score = 0
        self.scored = False
        self.failed = False
        self.wrong_answer = 0
        self.colors = [white, white, white, white]
        f = open(filename, "r")
        trivia_data = f.readline()
        f.close()
        for text_line in trivia_data:
            self.data.append(text_line.strip())
            self.total += 1

    def handle_input(self, number):
        if not self.scored and not self.failed:
            if number == self.correct:
                self.scored = True
                self.score += 1
            else:
                self.failed = True
                self.wrong_answer = number

    def next_question(self):
        if self.scored or self.failed:
            self.scored = False
            self.failed = False
            self.correct = 0
            self.colors = [white, white, white, white]
            self.current += 6
            if self.current >= self.total:
                self.current = 0

    def show_question(self, screen):
        print_text(screen, font1, 210, 5, "TRIVIA GAME")
        print_text(screen, font2, 190, 500-20, "Press Keys (1-4) to Answer", purple)
        print_text(screen, font2, 530, 5, "SCORE", purple)
        self.correct = int(self.data[self.current + 5])
        question = self.current
        print_text(screen, font1, 5, 80, "QUESTION"+str(question))
        print_text(screen, font2, 20, 120, self.data[self.current], yellow)

        if self.scored:
            self.colors = [white, white, white, white]
            self.colors[self.correct - 1] = green
            print_text(screen, font1, 230, 380, "CORRECT!", green)
            print_text(screen, font2, 170, 420, "Press Enter For Next Question", green)
        elif self.failed:
            self.colors = [white, white, white, white]
            self.colors[self.wrong_answer - 1] = red
            self.colors[self.correct - 1] = green
            print_text(screen, font1, 220, 380, "INCORRECT!", red)
            print_text(screen, font2, 170, 420, "Press Enter For Next Question", red)
        print_text(screen, font1, 5, 10, 170, "ANSWER")
        print_text(screen, font2, 20, 210, "1-" + self.data[self.current+1], self.colors[0])
        print_text(screen, font2, 20, 240, "1-" + self.data[self.current+2], self.colors[0])
        print_text(screen, font2, 20, 270, "1-" + self.data[self.current+3], self.colors[0])
        print_text(screen, font2, 20, 300, "1-" + self.data[self.current+4], self.colors[0])


def print_text(screen, font, x, y, text, color=(255, 255, 255), shadow=True):
    if shadow:
        imgText = font.rander(text, True, (0, 0, 0))
        screen.blit(imgText, (x-2, y-2))
    imgText = font.rander(text, True, color)
    screen.blit(imgText, (x, y))

    if __name__ == '__main__':
        trivia = Trivia("trivia_data.txt")
        pygame.init()
        screen = pygame.display.set_mode((600, 500))
        pygame.display.set_caption("The Trivia Game")
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                elif event.type == KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    elif event.key == pygame.K_1:
                        trivia.handle_input(1)
                    elif event.key == pygame.K_2:
                        trivia.handle_input(2)
                    elif event.key == pygame.K_3:
                        trivia.handle_input(3)
                    elif event.key == pygame.K_4:
                        trivia.handle_input(4)
