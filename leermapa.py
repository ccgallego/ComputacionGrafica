import ConfigParser
import pygame

interprete=ConfigParser.ConfigParser()
interprete.read('mapa.map')

print interprete.get('nivel','origen')
print interprete.get('nivel','mapa')
mapa= interprete.get('nivel','mapa')
mapa=mapa.split('\n')
print mapa
print len(mapa)


if __name__ == '__main__':

    pygame.init()
    pantalla=pygame.display.set_mode([900,400])
    imagen=pygame.image.load('terrenogen.png')
    info=imagen.get_rect()
    an_img=info[2]
    al_img = info[3]
    #print an_img,al_img
    an_corte= an_img/ 32
    al_corte=al_img / 12

    limites=[32,32,32,32,32,32,32,32,32,32,32,32]
    m=[]
    x_corte=0
    for y in range(12):
        fila=[]
        for i in range(limites[y]):
            cuadro=imagen.subsurface(i*an_corte,y*al_corte,an_corte,al_corte)
            fila.append(cuadro)
        m.append(fila)


    for f in range(len(mapa)):
        s=0
        for i in mapa[f]:
             x=int(interprete.get(i,'x'))
             y=int(interprete.get(i,'y'))
             pantalla.blit(m[y][x],[0+s,0])
             s+=32
        

    fin=False
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True



        pygame.display.flip()
