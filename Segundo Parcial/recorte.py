import pygame
import random

ancho = 1056
alto = 550

class Jugador(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=1
        self.image= self.m[self.accion][0]
        self.rect = self.image.get_rect()
        self.i=0
        self.rect.y=200
        self.vely=0
        self.velx=0
    def update(self):
        self.rect.y += self.vely
        self.rect.x += self.velx
        if self.accion==2:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
                self.accion=1
        elif self.accion==7:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                    self.i=0
                    self.accion=1
        else:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
        self.image=self.m[self.accion][self.i]

class Barril(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([50,80])
        self.image.fill([0,0,255])
        self.rect = self.image.get_rect()
        self.grito=pygame.mixer.Sound('grito.ogg')


if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])

    todos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    barriles=pygame.sprite.Group()


    imagen = pygame.image.load("ken.png").convert_alpha()
    info=imagen.get_rect()
    an_img=info[2]
    al_img = info[3]
    #print an_img,al_img
    an_corte= an_img/ 7
    al_corte=al_img / 10
    limites=[4,4,3,5,2,4,5,5,7,1]
    m=[]
    x_corte=0
    for y in range(10):
        fila=[]
        for i in range(limites[y]):
            cuadro=imagen.subsurface(i*an_corte,y*al_corte,an_corte,al_corte)
            fila.append(cuadro)
        m.append(fila)

    jugador=Jugador(m)
    b=Barril()
    b.rect.y=150
    b.rect.x=150
    todos.add(jugador)
    todos.add(b)
    jugadores.add(jugador)
    barriles.add(b)

    musica_f=pygame.mixer.Sound('music.ogg')
    musica_f.play()

    reloj=pygame.time.Clock()

    fin=False
    while not  fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    jugador.velx=0
                    jugador.vely=5
                if event.key == pygame.K_RIGHT:
                    jugador.vely=0
                    jugador.velx=5
                if event.key == pygame.K_LEFT:
                    jugador.velx=-5
                if event.key == pygame.K_UP:
                    jugador.vely=-5
                if event.key == pygame.K_a:
                    jugador.accion=2
                    jugador.i=0
                if event.key == pygame.K_s:
                    jugador.accion=7
                    jugador.i=0
            if event.type == pygame.KEYUP:
                jugador.velx=0
                jugador.vely=0

        if jugador.accion==2 or jugador.accion==7:
            ls_col=pygame.sprite.spritecollide(jugador,barriles,False)
            for b in ls_col:
                if b.rect.bottom >= (jugador.rect.bottom-10):
                    b.rect.x+=10
                    b.grito.play()

        todos.update()
        pantalla.fill([0,0,0])
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(20)
