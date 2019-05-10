# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 01:13:53 2019

@author: Vishwajeet
"""
import pygame

class GameOver():
    def __init__(self,screen,ai_setting):
        self.screen=screen
        self.ai_setting=ai_setting
        #load the ship and retangle it
        self.image=pygame.image.load('image/game_over.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        
        #start new ship at the bottom center of screen
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        
        
    def blitme(self):
        #Draw the ship at the currnet location.
        self.screen.blit(self.image,self.rect)
        