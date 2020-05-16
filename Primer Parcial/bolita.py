import pygame
ancho=640
alto=480

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ancho,alto])
    reloj=pygame.time.Clock()
    pos=[10,10]
    pygame.draw.circle(pantalla,[0,255,0],pos,5)
    pygame.display.flip()
    x=0
    y=0
    dir=0
    dir2=0
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print event.pos
        x+=10
        pos[0]=x
        pantalla.fill([0,0,0])
        pygame.draw.circle(pantalla,[0,255,0],pos,5)
        pygame.display.flip()
        reloj.tick(10)
            # x+=10
            # pos[0]=x
            # pantalla.fill([0,0,0])
            # pygame.draw.circle(pantalla,[0,255,0],pos,5)
            # pygame.display.flip()
            # reloj.tick(10)
            # while pos[1] < 470:
            #     y+=10
            #     pos[1]=y
            #     pantalla.fill([0,0,0])
            #     pygame.draw.circle(pantalla,[0,255,0],pos,5)
            #     pygame.display.flip()
            #     reloj.tick(10)
            # if pos[0]<=630 and pos[1]<=470:
            #     y-=10
            #     pos[1]=y
            #     pantalla.fill([0,0,0])
            #     pygame.draw.circle(pantalla,[0,255,0],pos,5)
            #     pygame.display.flip()
            #     reloj.tick(10)











        #print x
