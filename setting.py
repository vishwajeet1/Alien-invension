# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 01:15:28 2019

@author: Vishwajeet
"""

class Setting():
    def __init__(self):
        self.screen_width=1200
        self.screen_height=600
        self.bg_color=(255,255,255)
        
        # ship speed
        self.ship_speed=4
        self.ship_limit=1
        
        #bulet 
        self.bullet_speed=1
        self.bullet_width=20
        self.bullet_height=10
        self.bullet_color=(255,130,0)
        self.bullet_allow=10
        
        #alien
        self.alien_speed = 2
        self.alien_drop_speed = 50
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        