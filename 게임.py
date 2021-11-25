import pygame  
import random
import os

pygame.init()  



BLACK = (0, 0, 0)
size = [600, 800]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

def runGame():
    poop_image = pygame.image.load('poop.png')
    poop_image = pygame.transform.scale(poop_image, (50, 50))
    poops = []

    for i in range(5):
        rect = pygame.Rect(poop_image.get_rect())
        rect.left = random.randint(0, size[0])
        rect.top = -100
        dy = random.randint(3, 9)
        poops.append({'rect': rect, 'dy': dy})

    worm_image = pygame.image.load('worm.png')
    worm_image = pygame.transform.scale(worm_image, (100, 100))
    worm = pygame.Rect(worm_image.get_rect())
    worm.left = size[0] // 2 - worm.width // 2
    worm.top = size[1] - worm.height
    worm_dx = 0
    worm_dy = 0

    global done
    while not done:
        clock.tick(30)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    worm_dx = -5
                elif event.key == pygame.K_RIGHT:
                    worm_dx = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    worm_dx = 0
                elif event.key == pygame.K_RIGHT:
                    worm_dx = 0

        for poop in poops:
            poop['rect'].top += poop['dy']
            if poop['rect'].top > size[1]:
                poops.remove(poop)
                rect = pygame.Rect(poop_image.get_rect())
                rect.left = random.randint(0, size[0])
                rect.top = -100
                dy = random.randint(3, 9)
                poops.append({'rect': rect, 'dy': dy})

        worm.left = worm.left + worm_dx

        if worm.left < 0:
            worm.left = 0
        elif worm.left > size[0] - worm.width:
            worm.left = size[0] - worm.width

        screen.blit(worm_image, worm)

        for poop in poops:
            if poop['rect'].colliderect(worm):
                done = True
            screen.blit(poop_image, poop['rect'])

        pygame.display.update()


runGame()
pygame.quit()
