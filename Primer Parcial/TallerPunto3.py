##Dibujar el plano cartesiano,capturar 2 puntos, dibujar un triangulo entre los dos puntos y el centro.
##Cada vez que se pulse la tecla espacio, mover el punto mas a la derecha 20 pixeles y redibujar el triangulo

import pygame
import math

ancho=640
alto=480

def ejes(p,c):
    pygame.draw.line(p,[255,0,0],(c[0], 0), (c[0], alto), 3)
    pygame.draw.line(p,[255,0,0],(0, c[1]), (ancho, c[1]), 3)
    pygame.display.flip()

def Acarte(c,pto):
    x=pto[0] - c[0]
    y=c[1] - pto[1]
    return [x,y]

def APant(c,pto):
    x=c[0]+pto[0]
    y=c[1]-pto[1]
    return [x,y]

def Escalar(s,pto):
    x=pto[0]/s[0]
    y=pto[1]/s[1]
    return [x,y]


if __name__ == '__main__':

    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    centro=[320,240]
    ejes(pantalla,centro)
    ls=[]
    cont=0
    fin=False
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                cont+=1
                if cont == 1:
                    A=event.pos
                    ls.append(list(A))
                    pygame.draw.circle(pantalla,[0,255,0],A,5)
                if cont == 2:
                    B=event.pos
                    ls.append(list(B))
                    ls.append(centro)
                    pygame.draw.circle(pantalla,[0,255,0],B,5)
                    pygame.draw.polygon(pantalla,[0,255,0],ls,5)
                    print ls

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    maximo = ls[0][0]
                    for i in range(len(ls)):
                        if ls[i][0] > maximo:
                            maximo = ls[i][0]
                            pto = ls[i]
                            pto[0]+=20
                        if len(ls)==3:
                            pantalla.fill([0,0,0])
                            ejes(pantalla,centro)
                            pygame.draw.polygon(pantalla,[0,255,0],ls,5)
            pygame.display.flip()
