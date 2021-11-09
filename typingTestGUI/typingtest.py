import pygame
import sys
import time
import random
from pygame.locals import*

class game():
    def __init__(self):
        self.w = 750
        self.h = 500
        self.reset = True
        self.active = False
        self.input_text = ""
        self.words = ""
        self.time_start = 0
        self.total_time = 0
        self.accuracy = "0%"
        self.results = "Time 0 : Accuracy 0% : WPM 0"
        self.wpm = 0
        self.end = False
        self.HEAD_C = (255,213,102)
        self.TEXT_C = (240,240,240)
        self.RESULT_C = (255,70,70)

        pygame.init()
        self.open_img = pygame.image.load("typing.png")
        self.open_img = pygame.transform.scale(self.open_img,(self.w,self.h))

        self.bg_img = pygame.image.load("bg.jpg")
        self.bg_img = pygame.transform.scale(self.bg_img,(500,750))

        # self.scren = pygame.display.set_mode(self.w,self.h)
        pygame.display.set_caption("Typing Test Speed")
game()