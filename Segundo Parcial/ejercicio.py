import pygame

ancho = 900
alto = 480

if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    centro=[300,220]
    pantalla.fill((255,255,255))
    posx=0
    posy=0
    reloj=pygame.time.Clock()
    vel_x=0
    vel_y=0
    fin=False

    #ciclo del programa
    while not  fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    vel_x=+2
                    vel_y=0
                if event.key == pygame.K_LEFT:
                    vel_x=-2
                    vel_y=0
                if event.key == pygame.K_UP:
                    vel_y=-2
                    vel_x=0
                if event.key == pygame.K_DOWN:
                    vel_y=+2
                    vel_x=0
                if event.key == pygame.K_SPACE:
                    vel_x=0

        #refresco de la pantalla
        pantalla.fill([255,255,255])
        mario=pygame.image.load('mario2.jpg')
        pantalla.blit(mario,[posx,posy])
        if posx > ancho-mario.get_rect()[2]:
            posx=ancho-mario.get_rect()[2]
        if posy > alto-mario.get_rect()[3]:
            posy=alto-mario.get_rect()[3]


        pygame.display.flip()
        posx+=vel_x
        posy+=vel_y
        reloj.tick(60)
