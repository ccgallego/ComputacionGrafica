import pygame
import random

ancho = 900
alto = 500

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([30,30])
        self.image.fill([0,255,0])
        self.rect = self.image.get_rect()
        self.rect.x=100
        self.vel_x=0

    def update(self):
        self.rect.x += self.vel_x

class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([30,30])
        self.image.fill([0,0,255])
        self.rect = self.image.get_rect()
        self.vel_x=5

    def update(self):
        self.rect.x+=self.vel_x



if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    todos=pygame.sprite.Group()
    jugador=Jugador()
    todos.add(jugador)

    num_enemigos=10
    enemigos=pygame.sprite.Group()
    for i in range(num_enemigos):
        e=Enemigo()
        e.rect.x=random.randrange(ancho)
        e.rect.y=random.randrange(alto)
        enemigos.add(e)
        todos.add(e)

    reloj=pygame.time.Clock()

    fin=False
    #ciclo del programa
    while not  fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jugador.vel_x=2

        #logica juego

        #refresco de pantalla
        todos.update()
        pantalla.fill([0,0,0])
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
