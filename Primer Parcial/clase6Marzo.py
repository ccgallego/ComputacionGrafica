import pygame
ancho=600
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

if __name__ == '__main__':

    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    centro=[300,240]
    s=[2,2]
    lista=[[50,50],[100,50],[100,80]]
    tr=[]
    triangu=[]
    nueva_lista=[]
    ejes(pantalla,centro)
    for pto in lista:
        n_pto =APant(centro,pto)
        tr.append(n_pto)
    for pto1 in lista:
        new_pto=Escalar(s,pto1)
        triangu.append(new_pto)
    for punto in triangu:
        nuevo = APant(centro,punto)
        nueva_lista.append(nuevo)

    pygame.draw.polygon(pantalla,[255,0,0],tr,3)
    pygame.draw.polygon(pantalla,[0,255,0],nueva_lista,3)
    pygame.display.flip()

    fin=False
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            pygame.display.flip()
