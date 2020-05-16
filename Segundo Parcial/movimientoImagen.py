import pygame
import random

ancho = 1056
alto = 550

if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    imagen = pygame.image.load("animals.png")
    info=imagen.get_rect()
    an_img=info[2]
    al_img = info[3]
    #print an_img,al_img
    an_corte= an_img/ 12
    al_corte=al_img / 8

    fila0=[]
    fila1=[]
    fila2=[]
    fila3=[]
    dir=[]


    vel_x=0
    vel_y=0

    x_corte=0
    y_corte=0
    for i in range(5):
        y_corte=0
        cuadro=imagen.subsurface(i*an_corte,y_corte*al_corte,an_corte,al_corte)
        fila0.append(cuadro)
        dir.append(fila0)

    for i in range(5):
        y_corte=1
        cuadro=imagen.subsurface(i*an_corte,y_corte*al_corte,an_corte,al_corte)
        fila1.append(cuadro)
        dir.append(fila1)
    for i in range(5):
        y_corte=2
        cuadro=imagen.subsurface(i*an_corte,y_corte*al_corte,an_corte,al_corte)
        fila2.append(cuadro)
        dir.append(fila2)
    for i in range(5):
        y_corte=3
        cuadro=imagen.subsurface(i*an_corte,y_corte*al_corte,an_corte,al_corte)
        fila3.append(cuadro)
        dir.append(fila3)


    reloj=pygame.time.Clock()
    i=0
    y=0
    x=0
    fin=False
    while not  fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    vel_x+=5
                    vel_y=0
                    dir=
                if event.key == pygame.K_LEFT:
                    vel_x-=5
                    vel_y=0
                if event.key == pygame.K_DOWN:
                    vel_y+=5
                    vel_x=0
                if event.key == pygame.K_UP:
                    vel_y-=5
                    vel_x=0



        #logica
        i+=1
        if i > 2:
            i=0

        #Refresco de pantalla

        pantalla.fill([0,0,0])
        pantalla.blit(dir[0][i],[x,y])
        x+=vel_x
        y+=vel_y
        #pantalla.blit(imagen,[0,0])
        pygame.display.flip()
        reloj.tick(20)
