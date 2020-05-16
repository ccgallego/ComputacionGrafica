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
    x=pto[0]*s[0]
    y=pto[1]*s[1]
    return [x,y]

def RotacionHoraria(pto,ang):
    n_ang=math.radians(ang)
    x=pto[0]*math.cos(n_ang)+pto[1]*math.sin(n_ang)
    y=-pto[0]*math.sin(n_ang)-pto[1]*math.cos(n_ang)
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
    ejes(pantalla,centro)
    lista=[[50,50],[100,50],[100,80]]
    # lista=[[350,290],[350,340],[380,340]]
    n_lista=[]
    n_lista2=[]
    n_lista3=[]
    n_lista4=[]
    n_lista5=[]
    for pto in lista:
        n_pto = APant(centro,pto)
        n_lista.append(n_pto)
    # for puntos in lista:
    #     n_ptos =RotacionHoraria(puntos,90)
    #     n_lista2.append(n_ptos)
    # for ptos in n_lista2:
    #     punt = APant(centro,ptos)
    #     n_lista3.append(punt)

    pygame.draw.polygon(pantalla,[0,255,0],n_lista,3)
    pygame.display.flip()
    print lista
    # pygame.draw.polygon(pantalla,[255,0,0],n_lista3,3)
    angulo=90
    fin=False
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    for puntos in lista:
                        new_ptos = RotacionHoraria(puntos,angulo)
                        n_lista4.append(new_ptos)
                        lista=[]
                    for npto in n_lista4:
                        punt=APant(centro,npto)
                        n_lista5.append(punt)
                        pantalla.fill([0,0,0])
                        ejes(pantalla,centro)
                        lista=n_lista5[:]
                    pygame.draw.polygon(pantalla,[0,255,0],n_lista5,3)
                    print lista
                    n_lista5=[]
                    n_lista4=[]
        pygame.display.flip()
