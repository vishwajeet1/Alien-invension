# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 01:33:27 2019

@author: Vishwajeet
"""
import pygame
class Ship():
    def __init__(self,screen,ai_setting):
        self.screen=screen
        self.ai_setting=ai_setting
        #load the ship and retangle it
        self.image=pygame.image.load('image/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        
        #start new ship at the bottom center of screen
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        
        #ship speed init
        self.center=float(self.rect.centerx)
        
        #movement flag
        self.moving_right=False
        self.moving_left=False
    
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center +=self.ai_setting.ship_speed
        if self.moving_left and  self.rect.left>0:
            self.center -=self.ai_setting.ship_speed
       
        self.rect.centerx=self.center
        
    def blitme(self):
        #Draw the ship at the currnet location.
        self.screen.blit(self.image,self.rect)
        
    def center_ship(self):
        self.center=self.screen_rect.centerx
        
    