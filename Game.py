import pygame

pygame.init()

run = True

pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hi")

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()



