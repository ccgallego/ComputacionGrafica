import pygame
import random

ancho = 1056
alto = 550



if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    imagen = pygame.image.load("ken.png")
    info=imagen.get_rect()
    an_img=info[2]
    al_img = info[3]
    #print an_img,al_img
    an_corte= an_img/ 7
    al_corte=al_img / 10
    limites=[4,4,3,5,2,4,5,5,7,1]
    m=[]
    x_corte=0
    y_corte=0
    for y in range(10):
        fila=[]
        for i in range(limites[y]):
            cuadro=imagen.subsurface(i*an_corte,y_corte*al_corte,an_corte,al_corte-7)
            fila.append(cuadro)
            m.append(fila)

    reloj=pygame.time.Clock()

    fin=False
    while not  fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True


        pantalla.fill([0,0,0])
        pantalla.blit(m[0][0],[0,0])

        #pantalla.blit(imagen,[0,0])
        pygame.display.flip()
        reloj.tick(20)
