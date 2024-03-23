# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:06:40 2024

@author: cough
"""

import pygame
import random

def main():
    global gameOver
    pygame.init()
    
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("First Animation")
    
    



    backgroundImagePath = "C:/Users/cough/Downloads/sky.jpeg"
    background = pygame.image.load(backgroundImagePath).convert()
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    
    box = pygame.Surface((25, 25))
    box = box.convert()
    box.fill((0, 240, 0))
    box_x = (screen.get_width() - box.get_width()) // 2  
    box_y = (screen.get_height() - box.get_height()) // 2
    
    badBox = pygame.Surface((50,50))
    badBox = badBox.convert()
    badBox.fill((240, 0, 0))
    badBox_x = random.randint(0,640)
    badBox_y = random.randint(0, 100)
    
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    keepGoing = True
    gameOver = False
    gameOverTime = None
    msgDisplay = False
    
    while keepGoing:
        clock.tick(30)
        badBox_y += 4
        
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if pressed_keys[pygame.K_ESCAPE]:
                keepGoing = False
                
        if pressed_keys[pygame.K_a]:
            box_x -= 5
        if pressed_keys[pygame.K_d]:
            box_x += 5
        if pressed_keys[pygame.K_s]:
            box_y += 5
        if pressed_keys[pygame.K_w]:
            box_y -= 5
        
            
        if box_x + box.get_width() > screen.get_width():  
            box_x = screen.get_width() - box.get_width()
        if box_x < 0:
            box_x +=5
        if box_y + box.get_height() > screen.get_height():  
            box_y = screen.get_height() - box.get_height()
        if box_y < 0:
            box_y = 0
        if badBox_x > screen.get_width():
            badBox_x = random.randint(0, 100)
            badBox_y = 0
        if badBox_y > screen.get_height():  
            badBox_y = 0
            badBox_x = random.randint(0, 100)
        
       
        green_box_rect = pygame.Rect(box_x, box_y, box.get_width(), box.get_height())
        red_box_rect = pygame.Rect(badBox_x, badBox_y, badBox.get_width(), badBox.get_height())

        if green_box_rect.colliderect(red_box_rect):
            print("Game Over")
            gameOver = True
            gameOverTime = pygame.time.get_ticks()

        
        if gameOver:
            msgDisplay = True
            while msgDisplay:
                text_surface = font.render("Game Over", True, (255, 0, 0))
                text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
                screen.blit(text_surface, text_rect)
                pygame.display.flip()
                if pygame.time.get_ticks() - gameOverTime > 3000:  
                    msgDisplay = False
                    keepGoing = False


        
    
        
        screen.blit(background, (0, 0))
        screen.blit(box, (box_x, box_y))
        screen.blit(badBox, (badBox_x, badBox_y))
        pygame.display.flip()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()