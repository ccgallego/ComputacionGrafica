import pygame
import math

ancho=900
alto=450

Verde=[0,255,0]
Blanco=[255,255,255]

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([30,30])
        self.image.fill([0,255,0])
        self.rect = self.image.get_rect()
        self.rect.y=100
        self.vel_x=0
        self.vel_y=0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
class Muro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([60,60])
        self.image.fill(Blanco)
        self.rect = self.image.get_rect()

if __name__ == '__main__':

    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])

    #Grupos
    todos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    muros=pygame.sprite.Group()

    #Creamos el jugador
    jugador=Jugador()
    todos.add(jugador)
    jugadores.add(jugador)

    #Creamos el Muro
    m=Muro()
    m.rect.x=200
    m.rect.y=200
    todos.add(m)
    muros.add(m)

    m=Muro()
    m.rect.x=400
    m.rect.y=200
    todos.add(m)
    muros.add(m)

    reloj=pygame.time.Clock()
    fin=False
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jugador.vel_x=5
                    jugador.vel_y=0
                if event.key == pygame.K_LEFT:
                    jugador.vel_x=-5
                    jugador.vel_y=0
                if event.key == pygame.K_UP:
                    jugador.vel_x=0
                    jugador.vel_y=-5
                if event.key == pygame.K_DOWN:
                    jugador.vel_x=0
                    jugador.vel_y=5
            if event.type == pygame.KEYUP:
                jugador.vel_x=0
                jugador.vel_y=0

        #logica del juego
        ls_col = pygame.sprite.spritecollide(jugador,muros,False)
        for m in ls_col:
            if (jugador.vel_x >0) and (jugador.rect.right >= m.rect.left):
                jugador.vel_x=0
                jugador.rect.right = m.rect.left

            if (jugador.vel_y > 0) and (jugador.rect.bottom >= m.rect.top):
                jugador.vel_y=0
                jugador.rect.bottom = m.rect.top

            if (jugador.vel_x < 0) and (jugador.rect.left <= m.rect.right):
                jugador.vel_x=0
                jugador.rect.left = m.rect.right

            if (jugador.vel_y < 0) and (jugador.rect.top <= m.rect.bottom):
                jugador.vel_y=0
                jugador.rect.top = m.rect.bottom
        #Refresco
        todos.update()
        pantalla.fill([0,0,0])
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(40)
