#dibujar un cuadrilatero en la pantalla y cuando se le de espacio se vaya agrandando los 4 esquinas
import pygame
import math

ancho=640
alto=480

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
    #ejes(pantalla,centro)
    cuadrado =[]
    p1=[100,100]
    p2=[100,50]
    p3=[200,50]
    p4=[200,100]
    cuadrado.append(p1)
    cuadrado.append(p2)
    cuadrado.append(p3)
    cuadrado.append(p4)
    # ls=[]
    # for pto in cuadrado:
    #     n_pto=APant(centro,pto)
    #     ls.append(n_pto)
    fin=False
    pygame.draw.polygon(pantalla,[0,255,0],cuadrado,5)
    pygame.display.flip()
    ang=45
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    maximo = cuadrado[0][0]
                    minimo= cuadrado[0][0]
                    for i in range(len(cuadrado)):
                        if cuadrado[i][0] > maximo:
                            maximo = cuadrado[i][0]
                            pto=cuadrado[i]
                            pto[0]+=20
                            if cuadrado[i][0] < maximo:
                                minimo = cuadrado[i][0]
                                pto2=cuadrado[i]
                                pto2[0]-=20
                        if len(cuadrado)==4:
                            pantalla.fill([0,0,0])
                            pygame.draw.polygon(pantalla,[0,255,0],cuadrado,5)
                    pygame.display.flip()
