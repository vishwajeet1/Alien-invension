# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 00:09:34 2019

@author: Vishwajeet
"""

class GameStats():
    """Track statistics for Alien Invasion."""
    def __init__(self,ai_setting):
        self.ai_setting=ai_setting
        self.high_score=0
        self.reset_stats()
        self.game_active=False
        
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ship_left= self.ai_setting.ship_limit
        self.score=0
        
        