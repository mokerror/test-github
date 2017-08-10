import pygame

class Bullet():
    """子弹"""
    def __init__(self):
        self.x=0
        self.y=1
        self.image=pygame.image.load('images/bullet.png')
        self.active=False

    def move(self):
        if self.active:
            self.y-=3
        if self.y<0:
            self.avtive=False

    def restart(self):
        mouse_x,mouse_y=pygame.mouse.get_pos()
        self.x=mouse_x-self.image.get_width()/2
        self.y=mouse_y-self.image.get_height()/2
        self.active=True
