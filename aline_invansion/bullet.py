# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 19:53:09 2019

@author: Vishwajeet
"""
import sys
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_setting,screen,ship):
        super(Bullet,self).__init__()
        
        self.screen=screen
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect=pygame.Rect(0,0, ai_setting.bullet_width, ai_setting.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        
        # Store the bullet's position as a decimal value.
        self.y=float(self.rect.y)
        
        self.bullet_color=ai_setting.bullet_color
        self.bullet_speed=ai_setting.bullet_speed
        
    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y-=self.bullet_speed
        self.rect.y=self.y
    def draw_bullet(self):
        """Draw bullet to screen"""
        pygame.draw.rect(self.screen,self.bullet_color,self.rect)
    