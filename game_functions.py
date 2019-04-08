# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 02:02:00 2019

@author: Vishwajeet
"""
#import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from game_over import GameOver

def check_alien_bottom(ai_setting,stats,screen,ship,alien,bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect=screen.get_rect()
    for aliens in alien.sprites():
        if aliens.rect.bottom>=screen_rect.bottom:
            ship_hit(ai_setting,stats,screen,ship,alien,bullets)
            break

def ship_hit(ai_setting,stats,screen,ship,alien,bullets):
   
    """Respond to ship being hit by alien."""
    if stats.ship_left>0:
        # Decrement ships_left.
        stats.ship_left-=1
        
        # Empty the list of aliens and bullets.
        alien.empty()
        bullets.empty()
        
        # Create a new fleet and center the ship.
        create_alien_fleet(ai_setting,screen,alien,ship)
        ship.center_ship()
        
        #pause
        sleep(1)
    else:
        alien.empty()
        bullets.empty()
        stats.game_active=False

def get_number_rows(ai_setting,ship_height,alien_height):
    available_space_y= (ai_setting.screen_height - (3 * alien_height) - ship_height)
    number_row=int(available_space_y/(2*alien_height))
    return number_row

def get_number_alien(ai_setting,alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x=ai_setting.screen_width - alien_width
    number_alien_x=int(available_space_x/(2*alien_width))
    return number_alien_x

def create_alien(ai_setting,screen,alien,alien_number,row_number):
    aliens=Alien(ai_setting,screen)
    alien_width=aliens.rect.width
    aliens.x = alien_width + 2*alien_width*alien_number
    aliens.rect.x=aliens.x
    aliens.rect.y=aliens.rect.height + 2*aliens.rect.height *row_number 
    alien.add(aliens)

def create_alien_fleet(ai_setting,screen,alien,ship):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    aliens=Alien(ai_setting,screen)
    
    number_alien_x=get_number_alien(ai_setting,aliens.rect.width)
    number_row=get_number_rows(ai_setting,ship.rect.height,aliens.rect.height)
    #create the first row
    
    for row_number in range(number_row):
        for alien_number in range(number_alien_x):
            create_alien(ai_setting,screen,alien,alien_number,row_number)

        # Create an alien and place it in the row.


def change_fleet_direction(ai_setting,alien):
    """Drop the entire fleet and change the fleet's direction."""
    for aliens in alien.sprites():
        aliens.rect.y+=ai_setting.alien_drop_speed
    ai_setting.fleet_direction*=-1

def check_fleet_edge(ai_setting,alien):
    """Respond appropriately if any aliens have reached an edge."""
    for aliens in alien.sprites():
        if aliens.check_edge():
            change_fleet_direction(ai_setting,alien)
            break
    
def update_alien(ai_setting,stats,screen,ship,alien,bullets):
    check_fleet_edge(ai_setting,alien)
    alien.update()
    # Look for alien-ship collisions.
    check_alien_bottom(ai_setting,stats,screen,ship,alien,bullets)
    if pygame.sprite.spritecollideany(ship,alien):
        ship_hit(ai_setting,stats,screen,ship,alien,bullets)
    
            
        
    
    
def check_keydown_event(event,ai_setting,ship,screen,bullets):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.
        fire_bullets(bullets,ai_setting,screen,ship)
        
def check_keyup_event(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False
        
def fire_bullets(bullets,ai_setting,screen,ship):
    if len(bullets)< ai_setting.bullet_allow:
        new_bullet=Bullet(ai_setting,screen,ship)
        bullets.add(new_bullet)
    
    

def check_events(ai_setting,screen,ship,bullets):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
               check_keydown_event(event,ai_setting,ship,screen,bullets)
            elif event.type == pygame.KEYUP:
                check_keyup_event(event,ship)
def check_bullets_collision(bullets,aliens,ai_setting,screen,ship):
    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien. 
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    #1st flase means bullets wil not disable after hitting allien
    #2nd flase means ship will not destroy
    if len(aliens)==0:
        # Destroy existing bullets and create new fleet.
        bullets.empty()
        create_alien_fleet(ai_setting,screen,aliens,ship)
    
def update_bullets(bullets,aliens,ai_setting,screen,ship):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    check_bullets_collision(bullets,aliens,ai_setting,screen,ship)
                    
        
def update_screen(ai_settings,screen,ship,bullets,alien,stats,gameover):    
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.draw(screen)
    print(stats.ship_left)
    if stats.ship_left<=0:
        gameover.blitme()
        
    pygame.display.flip()
    
    