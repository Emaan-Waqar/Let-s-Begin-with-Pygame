import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("My first game screen")
image=pygame.image.load("img.png")
image=pygame.transform.scale(image,(300,300))

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((58,58,58))
    screen.blit(image,(100,100))
    pygame.display.flip()
pygame.quit()        