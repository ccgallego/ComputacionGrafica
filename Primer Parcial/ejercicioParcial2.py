import pygame
import math
ancho = 600
alto = 480
contador=0
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
    centro=[300,240]
    ejes(pantalla,centro)
    fin=False
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                contador+=1
                if contador ==1:
                    a=event.pos
                if contador ==2:
                    b=event.pos
                    pygame.draw.line(pantalla,[255,0,0],a, b,4)
                if contador==3:
                    c=event.pos
                    als=event.pos[0]
                if contador ==4:
                    d=event.pos
                    dls=event.pos[0]
                    pygame.draw.line(pantalla,[0,255,0],c, d,4)
                    pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                pantalla.fill([0,0,0])
                pygame.draw.line(pantalla,[255,0,0],a, b,4)
                if event.key == pygame.K_a:
                    dls+=15
                    als-=15
                    pygame.draw.line(pantalla,[0,255,0],c, (dls,als),4)
                    pygame.display.flip()
