import pygame
import random

ancho = 600
alto = 600

class Jugador(pygame.sprite.Sprite):
    def _init_(self,m):
        pygame.sprite.Sprite._init_(self)
        self.m=m
        self.accion=0
        self.image= self.m[self.accion][0]
        self.rect = self.image.get_rect()
        self.i=0
        self.rect.y=0
        self.var_y=0
        self.var_x=0
        self.con=0
        self.dir=0
    def update(self):
        self.rect.x+=self.var_x
        self.rect.y+=self.var_y
        self.i+=1
        if self.i >= len(self.m[self.accion]):
            self.i=0
        self.image=self.m[self.accion][self.i]

        if self.con<2:
            self.con+=1
        else:
            self.con=0

class Enemigo(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite._init_(self)
        self.image= pygame.Surface([30,30])
        self.image.fill([0,0,255])
        self.rect = self.image.get_rect()
        self.rect.y=-40
        self.vel_y=2
        self.temp = random.randrange(50)
        self.tempdis=random.randrange(50)
        self.disparar=False

    def update(self):
        if self.tempdis > 0:
            self.tempdis-=1
        else:
            self.disparar=True
        if self.temp > 0:
            self.temp-=1
        else:
            self.rect.y+=self.vel_y




if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])

    #GRUPOS
    todos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()


    imagen = pygame.image.load("jugador1.png").convert_alpha()
    imagen2= pygame.image.load("jugador2.png").convert_alpha()
    info=imagen.get_rect()
    an_img=info[2]
    al_img = info[3]
    #print an_img,al_img
    an_corte= an_img/ 4
    al_corte=al_img / 4
    limites=[4,4,4,4]
    m=[]
    m2=[]
    x_corte=0
    for y in range(4):
        fila=[]
        for i in range(limites[y]):
            cuadro=imagen.subsurface(i*an_corte,y*al_corte,an_corte,al_corte)
            fila.append(cuadro)
        m.append(fila)

    for y in range(4):
        fila2=[]
        for i in range(limites[y]):
            cuadro2=imagen2.subsurface(i*an_corte,y*al_corte,an_corte,al_corte)
            fila2.append(cuadro2)
        m2.append(fila2)

    jugador=Jugador(m)
    jugador2=Jugador(m2)
    todos.add(jugador)
    jugadores.add(jugador)
    jugadores.add(jugador2)
    todos.add(jugador2)

    reloj=pygame.time.Clock()
    con=0
    fin=False
    while not  fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jugador.var_x=+5
                    jugador.var_y=0
                    jugador.accion=2
                if event.key == pygame.K_LEFT:
                    jugador.var_x=-5
                    jugador.var_y=0
                    jugador.accion=1
                if event.key == pygame.K_DOWN:
                    jugador.var_y=+5
                    jugador.var_x=0
                    jugador.accion=0
                if event.key == pygame.K_UP:
                    jugador.var_y=-5
                    jugador.var_x=0
                    jugador.accion=3
                if event.key == pygame.K_d:
                    jugador2.var_x=+5
                    jugador2.var_y=0
                    jugador2.accion=2
                if event.key == pygame.K_a:
                    jugador2.var_x=-5
                    jugador2.var_y=0
                    jugador2.accion=1
                if event.key == pygame.K_s:
                    jugador2.var_y=+5
                    jugador2.var_x=0
                    jugador2.accion=0
                if event.key == pygame.K_w:
                    jugador2.var_y=-5
                    jugador2.var_x=0
                    jugador2.accion=3
            if event.type == pygame.KEYUP:
                jugador.var_x=0
                jugador.var_y=0
                jugador2.var_x=0
                jugador2.var_y=0
        jugador.image=m[0+jugador.con][jugador.dir]
        jugador2.image=m[0+jugador2.con][jugador2.dir]
        if con<2:
            con+=1
        else:
            con=0
        todos.update()
        pantalla.fill([0,0,0])
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(10)
