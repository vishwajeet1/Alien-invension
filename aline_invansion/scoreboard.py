# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 00:00:16 2019

@author: Vishwajeet
"""
import pygame.font

class Scoreboard():
    def __init__(self,ai_setting,screen,stats):
        
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.ai_setting=ai_setting
        self.stats=stats
        # Font settings for scoring information.
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        
        self.prep_score()
        self.prep_high_score()
         
    def prep_score(self):
        '''turn the score into rendering image'''
        round_score=int(round(self.stats.score,-1))
        score_str="{:,}".format(round_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_setting.bg_color)
        
        #Display the score at the top right of the screen.
        
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right= self.screen_rect.right -20
        self.score_rect.top=20
    
    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score=int(round(self.stats.high_score,-1))
        high_score_str="{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_setting.bg_color)
        
        #high score position
        
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.screen_rect.top
    
        
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)