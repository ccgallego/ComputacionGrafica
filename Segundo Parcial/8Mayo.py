import pygame
import random

ancho = 1056
alto = 550

class Cuadro(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([an,al])
        self.image.fill([0,0,255])
        self.rect = self.image.get_rect()
        self.rect.x=0
        self.click=False

reloj=pygame.time.Clock();



if __name__ == '__main__':
    #definicion de variables

    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])

    todos=pygame.sprite.Group()
    c=Cuadro(30,30)
    todos.add(c)
    
    fin=False
    while not  fin:
        pos=pygame.mouse.get_pos()
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if c.rect.collidepoint(pos):
                    c.click=True
            if event.type == pygame.MOUSEBUTTONUP:
                c.click=False

        if c.click:
            c.rect.center=pos

    pantalla.fill([0,0,0])
    todos.draw(pantalla)
    pygame.display.flip()
    reloj.tick(50)
