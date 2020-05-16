import pygame

ancho=640
alto=480

def Ejes(p,c):
    pygame.draw.line(p,[255,0,0],[c[0],0],[c[0],alto])
    pygame.draw.line(p,[255,0,0],[0,c[1]],[ancho,c[1]])
    pygame.display.flip()

def ACart(c,pto):
    x=pto[0]-c[0]
    y=c[1]-pto[1]
    return [x,y]

def Apant(c,pto):
    x=c[0]+pto[0]
    y=c[1]-pto[1]
    return [x,y]

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([640,480])
    centro=[300,220]
    Ejes(pantalla,centro)
    cont = 0
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print 'click', ACart(centro,event.pos)
                cont+=1
                if cont == 1:
                    A=event.pos
                    print 'A posicio pantalla',A
                if cont == 2:
                    B=event.pos
                    print 'B posicion pantalla', B
                    pygame.draw.line(pantalla,[0,255,0],A,B)
                    cont=0

                    #CALCULAR EL CANONICO

                    Ac = ACart(centro,A)
                    Bc = ACart(centro,B)
                    v= [ Bc[0]-Ac[0], Bc[1]-Ac[1] ]
                    pygame.draw.line(pantalla,[255,255,255], centro,Apant(centro,v))
                    pygame.display.flip()
