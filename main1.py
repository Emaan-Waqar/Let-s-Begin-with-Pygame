import pygame
pygame.init()
width,height=800,600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("..")
image=pygame.image.load("chess.png")
image=pygame.transform.scale(image,(300,600))

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((255,255,255))
    screen.blit(image,(50,50))
    pygame.display.flip()
pygame.quit()            
