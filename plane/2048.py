#!/usr/bin/env python3
#-*-coding:utf-8-*-
import pygame
import sys
from settings import Settings
from bullet import Bullet
from plane import Plane
from enemy import Enemy

def check_events():
    """响应鼠标键盘事件"""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.quit()
def check_hit(enemy,bullet):
    """检查子弹是否击中目标"""
    if enemy.x<bullet.x and bullet.x<(enemy.x+enemy.image.get_width()) and enemy.y<bullet.y and bullet.y<(enemy.y+enemy.image.get_height()):
        enemy.restart()
        bullet.active=False
        return True
    return False

def check_crash(enemy,plane):
    """检查敌机与我方是否碰撞"""
    if (plane.x + 0.7*plane.image.get_width() > enemy.x) and (plane.x + 0.3*plane.image.get_width() < enemy.x + enemy.image.get_width()) and (plane.y + 0.7*plane.image.get_height() > enemy.y) and (plane.y + 0.3*plane.image.get_width() < enemy.y + enemy.image.get_height()):
        return True
    return False

def  run_game():
    """运行游戏"""
    pygame.init()
    game_settings=Settings()
    plane=Plane()
    pygame.mixer.music.load('bgm.mp3')
    pygame.mixer.music.play(-1,1.0)
    screen=pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption('飞机大战')
    background=pygame.image.load('images/background.jpg')
    bullets=[]
    enemys=[]
    score=0

    for i in range(5):
        bullets.append(Bullet())
        if i>2:
            enemys.append(Enemy())

    count_b=len(bullets)
    index_b=0   #子弹数
    interval_b=0    #子弹间隔
    gameover=False

    while True:
        fonts=pygame.font.SysFont(None,32)
        text=fonts.render('Score: %d'%score,1,(0,0,0))
        if not gameover:
            check_events()
            screen.fill(game_settings.bg_color)
            screen.blit(background,(0,0))
            screen.blit(text,(0,0))
            interval_b-=1
            if interval_b<0:
                bullets[index_b].restart()
                interval_b=50
                index_b=(index_b+1)%count_b

            for bullet in bullets:
                if bullet.active:
                    for enemy in enemys:
                        if check_hit(enemy,bullet):
                            score+=100
                            screen.blit(text,(0,0))
                    bullet.move()
                    screen.blit(bullet.image,(bullet.x,bullet.y))
            plane.move()
            screen.blit(plane.image,(plane.x,plane.y))

            for enemy in enemys:
                if check_crash(enemy,plane):
                    gameover=True
                enemy.move()
                screen.blit(enemy.image,(enemy.x,enemy.y))
            pygame.display.flip()
        else:
            exit()

run_game()
