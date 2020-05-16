import pygame
import random

ancho = 1056
alto = 550

if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    imagen = pygame.image.load("imagen.jpg")
    info=imagen.get_rect()
    an_img=info[2]
    al_img = info[3]
    #print an_img,al_img
    an_corte= an_img/ 6
    al_corte=al_img / 3

    fila=[]

    x_corte=0
    y_corte=2
    for i in range(6):
        cuadro=imagen.subsurface(i*an_corte,y_corte*al_corte,an_corte,al_corte-7)
        fila.append(cuadro)


    pantalla.blit(fila[5],[0,0])
    #pantalla.blit(imagen,[0,0])
    pygame.display.flip()

    fin=False
    while not  fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
