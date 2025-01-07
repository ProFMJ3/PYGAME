import pygame
import sys

pygame.init()
canvas = pygame.display.set_mode((500, 500))

# TITLE OF CANVAS 
pygame.display.set_caption(title="My Board") 
exit = False
  
while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    pygame.display.update() 


