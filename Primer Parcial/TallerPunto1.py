##Capturar 4 ptos con el raton,dibujar la figura y escalarla a la mitad

import pygame
import math

ancho=640
alto=480

# def ejes(p,c):
#     pygame.draw.line(p,[255,0,0],(c[0], 0), (c[0], alto), 3)
#     pygame.draw.line(p,[255,0,0],(0, c[1]), (ancho, c[1]), 3)
#     pygame.display.flip()

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

def RotacionHoraria(pto,ang):
    n_ang=math.radians(ang)
    x=pto[0]*math.cos(n_ang)+pto[1]*math.sin(n_ang)
    y=-pto[0]*math.sin(n_ang)+pto[1]*math.cos(n_ang)
    int(x)
    int(y)
    return [x,y]
def RotacionAntihoraria(pto,ang):
    n_ang=math.radians(ang)
    x=pto[0]*math.cos(n_ang)-pto[1]*math.sin(n_ang)
    y=pto[0]*math.sin(n_ang)+pto[1]*math.cos(n_ang)
    int(x)
    int(y)
    return [x,y]

if __name__ == '__main__':

    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    centro=[320,240]
    ##ejes(pantalla,centro)
    ls=[]
    lista=[]
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
                    pygame.draw.circle(pantalla,[0,255,0],B,5)
                if cont == 3:
                    C=event.pos
                    ls.append(list(C))
                    pygame.draw.circle(pantalla,[0,255,0],C,5)
                if cont == 4:
                    D=event.pos
                    ls.append(list(D))
                    pygame.draw.circle(pantalla,[0,255,0],D,5)
                    pygame.draw.polygon(pantalla,[0,255,0],ls,5)
                    ##pygame.draw.polygon(pantalla,[0,255,0],ls,5)
                if len(ls) == 4:
                    for ptos in ls:
                        npto = Escalar([2,2],ptos)
                        lista.append(npto)
                    pygame.draw.polygon(pantalla,[0,255,0],lista,5)
            pygame.display.flip()

            ##pygame.draw.polygon(pantalla,[0,255,0],ls,5)
