#Dibujar un cuadrilatero en el plano cartesiano en el primer cuadrante, al pulsar la tecla espacio
#rotarlo en sentido horario 45 grados

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

def RotacionHoraria(pto,ang):
    n_ang=math.radians(ang)
    x=int(pto[0]*math.cos(n_ang)+pto[1]*math.sin(n_ang))
    y=int(-pto[0]*math.sin(n_ang)+pto[1]*math.cos(n_ang))
    return [x,y]

if __name__ == '__main__':

    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    centro=[320,240]
    ejes(pantalla,centro)
    cuadrado =[]
    p1=[100,100]
    p2=[100,50]
    p3=[200,50]
    p4=[200,100]
    cuadrado.append(p1)
    cuadrado.append(p2)
    cuadrado.append(p3)
    cuadrado.append(p4)
    ls=[]
    nls=[]
    for pto in cuadrado:
        n_pto=APant(centro,pto)
        ls.append(n_pto)
    fin=False
    pygame.draw.polygon(pantalla,[0,255,0],ls,5)
    pygame.display.flip()
    ang=45
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                pantalla.fill([0,0,0])
                ejes(pantalla,centro)
                if event.key == pygame.K_SPACE:
                    cuadrado[0]=RotacionHoraria(cuadrado[0],ang)
                    cuadrado[1]=RotacionHoraria(cuadrado[1],ang)
                    cuadrado[2]=RotacionHoraria(cuadrado[2],ang)
                    cuadrado[3]=RotacionHoraria(cuadrado[3],ang)
                    pygame.draw.polygon(pantalla,[0,255,0],[APant(centro,cuadrado[0]),APant(centro,cuadrado[1]),APant(centro,cuadrado[2])
                    ,APant(centro,cuadrado[3])],5)
                    pygame.display.flip()
