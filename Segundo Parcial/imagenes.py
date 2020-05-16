import pygame

if __name__ == '__main__':

    pygame.init()
    pantalla=pygame.display.set_mode([640,480])
    tux=pygame.image.load('mario.png')
    fin=False
    pos_x=100
    pos_y=100
    vel_x=0
    vel_y=0
    reloj=pygame.time.Clock()
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    vel_x=+5
                if event.key == pygame.K_LEFT:
                    vel_x=-5
                if event.key == pygame.K_SPACE:
                    vel_x=0
                    vel_y=0
                if event.key == pygame.K_DOWN:
                    vel_x=0
                    vel_y=+5
                if event.key == pygame.K_UP:
                    vel_x=0
                    vel_y=-5

        pantalla.fill([255,255,255])
        pantalla.blit(tux,[pos_x,pos_y])
        pygame.display.flip()
        pos_x+=vel_x
        pos_y+=vel_y
        reloj.tick(40)
