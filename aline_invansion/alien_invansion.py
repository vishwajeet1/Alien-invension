# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 00:57:43 2019

@author: Vishwajeet
"""
#import sys
import pygame
from setting import Setting
from alien import Alien
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from bullet import Bullet
from game_stats import GameStats
from game_over import GameOver
from botton import Botton
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    ai_setting=Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alien invansion")
    
    #ship
    ship=Ship(screen,ai_setting)
    
    #make bullets
    bullets=Group()

    #make an alien
    alien=Group()
    gf.create_alien_fleet(ai_setting,screen,alien,ship)
    
    #stats
    stats=GameStats(ai_setting)
    sb=Scoreboard(ai_setting,screen,stats)
    #botton
    play_botton=Botton(screen,ai_setting,"play")
    
    #GameOver
    gameover=GameOver(screen,ai_setting)
    while True:
        gf.check_events(ai_setting,screen,ship,bullets,play_botton,stats,alien)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(bullets,alien,ai_setting,screen,ship,stats,sb)
            gf.update_alien(ai_setting,stats,screen,ship,alien,bullets)
        gf.update_screen(ai_setting,screen,ship,bullets,alien,stats,gameover,play_botton,sb)
run_game()