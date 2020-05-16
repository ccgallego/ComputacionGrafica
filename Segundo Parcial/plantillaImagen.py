import pygame

if __name__ == '__main__':

    pygame.init()
    pantalla=pygame.display.set_mode([900,700])
    tux=pygame.image.load('.jpg,png')
    fin=False
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

        pantalla.blit(tux,[0,0])
        pygame.display.flip()
        pantalla.fill([255,255,255])
