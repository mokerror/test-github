import pygame

class Plane():
    def __init__(self):
        """初始化飞船"""
        self.x=200
        self.y=400
        self.image=pygame.image.load('images/plane.png')

    def move(self):
        mouse_x,mouse_y=pygame.mouse.get_pos()
        self.x=mouse_x-self.image.get_width()/2
        self.y=mouse_y-self.image.get_height()/2
