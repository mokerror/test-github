import pygame
import random
class Enemy():
    """敌机"""
    def restart(self):
        self.x=random.randint(0,250)
        self.y=random.randint(-400,-50)
        self.speed=random.random()+1

    def __init__(self):
        self.restart()
        self.image=pygame.image.load('images/enemy.png')

    def move(self):
        if self.y<600:
            self.y+=self.speed
        else:
            self.restart()
