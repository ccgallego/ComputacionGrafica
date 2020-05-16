import pygame
ancho=640
alto=480

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ancho,alto])
    reloj=pygame.time.Clock()
    lptos=[]
    a=[100,100]
    b=[200,200]
    lptos.append(a)
    lptos.append(b)
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        for p in lptos:
            pygame.draw.circle(pantalla,[0,255,0],p,5)
        pygame.display.flip()
