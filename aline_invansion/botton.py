# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:34:33 2019

@author: Vishwajeet
"""
import pygame.font


class Botton:
    def __init__(self,screen,ai_setting,msg):
        
        """initialize botton attribute"""
        self.screen=screen
        self.screen_rect=screen.get_rect()
        
        """ set dimeansion for botton"""
        
        self.width,self.hight=200,50
        self.botton_color=(0,255,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)
        
        #build the botton in mid
        
        self.rect=pygame.Rect(0,0,self.width,self.hight)
        self.rect.center=self.screen_rect.center
        
        # The button message needs to be prepped only once.
        self.prep_msg(msg)
        
    def prep_msg(self,msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image=self.font.render(msg,True,self.text_color,self.botton_color)
        self.msg_image_rect =self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center  
        
        
    def draw_botton(self):
            # Draw blank button and then draw message.
            self.screen.fill(self.botton_color,self.rect)
            self.screen.blit(self.msg_image,self.msg_image_rect)