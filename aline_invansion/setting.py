# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 01:15:28 2019

@author: Vishwajeet
"""

class Setting():
    def __init__(self):
        self.screen_width=1200
        self.screen_height=720
        self.bg_color=(255,255,255)
        
        # ship speed
        self.ship_speed=4
        self.ship_limit=1
        
        #bulet 
        self.bullet_speed=1
        self.bullet_width=210
        self.bullet_height=10
        self.bullet_color=(255,130,0)
        self.bullet_allow=10
        
        #alien
        self.alien_speed = 2
        self.alien_drop_speed = 25
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        # How quickly the game speeds up
        self.speed_up=1.2
        self.score_scale=1.5
        
        self.initial_dynamic_setting()
        
    def initial_dynamic_setting(self):
        self.ship_speed=4
        self.bullet_speed=3
        self.alien_speed=2
        self.alien_point=50
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction=1
        
    def increase_speed(self):
        self.ship_speed*=self.speed_up
        self.alien_speed*=self.speed_up
        self.bullet_speed*=self.speed_up
        self.alien_point=int( self.alien_point * self.score_scale)
        print(self.alien_point)