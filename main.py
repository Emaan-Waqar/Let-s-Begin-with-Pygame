import pygame
pygame.init()

width,height= 800,600
pygame.display.set_mode((width,height))
pygame.display.set_caption("Basic Pygame Window")

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.display.flip()   
pygame.quit()    