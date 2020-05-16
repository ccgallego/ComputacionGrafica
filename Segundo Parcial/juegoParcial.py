import pygame
import random

ancho = 800
alto = 600

class Jugador(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=0
        self.image= self.m[self.accion][0]
        self.rect = self.image.get_rect()
        self.i=0
        self.salud=3
        self.rect.y=0
        self.var_y=0
        self.var_x=0
        self.con=0
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
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=1
        self.image= self.m[self.accion][0]
        self.rect = self.image.get_rect()
        self.i=0
        self.rect.x=850
        self.vel_x=-5
        self.salud=2
        self.con=0
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
            self.rect.x+=self.vel_x

        self.i+=1
        if self.i >= len(self.m[self.accion]):
            self.i=0
        self.image=self.m[self.accion][self.i]



class Bala(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([10,5])
        self.image.fill([255,255,255])
        self.rect = self.image.get_rect()
        self.vel_x=10
    def update(self):
        self.rect.x+=self.vel_x

if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    fondo=pygame.image.load('fondo.jpg')
    #GRUPOS
    todos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()

    balas=pygame.sprite.Group()
    balas_e=pygame.sprite.Group()

    fuente=pygame.font.Font(None,25)
    texto1=fuente.render("Jugador 1:",False,[255,255,255])
    texto2=fuente.render("Jugador 2:",False,[100,255,255])

    imagen = pygame.image.load("jugador1.png").convert_alpha()
    imagen2= pygame.image.load("jugador2.png").convert_alpha()
    imagen3= pygame.image.load("enemigo.png").convert_alpha()
    info=imagen.get_rect()
    info2=imagen3.get_rect()

    an_img3=info2[2]
    al_img3=info2[3]

    an_corte3=an_img3/9
    al_corte3=al_img3/4

    an_img=info[2]
    al_img = info[3]
    #print an_img,al_img
    an_corte= an_img/ 4
    al_corte=al_img / 4
    limites=[4,4,4,4]
    limites2=[8,8,8,8]
    m=[]
    m2=[]
    m3=[]
    go=False
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

    for y in range(4):
        fila3=[]
        for i in range(limites2[y]):
            cuadro3=imagen3.subsurface(i*an_corte3,y*al_corte3,an_corte3,al_corte3)
            fila3.append(cuadro3)
        m3.append(fila3)

    num_enemigos=15

    for i in range(num_enemigos):
        e=Enemigo(m3)
        e.rect.y=random.randrange(alto)

        enemigos.add(e)
        todos.add(e)

    jugador=Jugador(m)
    jugador2=Jugador(m2)
    enemigo=Enemigo(m3)
    jugador.rect.y=500
    jugador.rect.x=80
    jugador2.rect.y=500
    jugador2.rect.x=30
    todos.add(jugador)
    jugadores.add(jugador)
    jugadores.add(jugador2)
    todos.add(jugador2)
    jugadores.add(enemigo)
    todos.add(enemigos)

    reloj=pygame.time.Clock()
    con=0
    fin=False
    go=False
    while not  fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jugador.var_x=+10
                    jugador.var_y=0
                    jugador.accion=2
                if event.key == pygame.K_LEFT:
                    jugador.var_x=-10
                    jugador.var_y=0
                    jugador.accion=1
                if event.key == pygame.K_DOWN:
                    jugador.var_y=+10
                    jugador.var_x=0
                    jugador.accion=0
                if event.key == pygame.K_UP:
                    jugador.var_y=-10
                    jugador.var_x=0
                    jugador.accion=3
                if event.key == pygame.K_SPACE:
                    b=Bala()
                    b.rect.x = jugador.rect.x
                    b.rect.y = jugador.rect.y+20
                    balas.add(b)
                    todos.add(b)
                if event.key == pygame.K_d:
                    jugador2.var_x=+10
                    jugador2.var_y=0
                    jugador2.accion=2
                if event.key == pygame.K_a:
                    jugador2.var_x=-10
                    jugador2.var_y=0
                    jugador2.accion=1
                if event.key == pygame.K_s:
                    jugador2.var_y=+10
                    jugador2.var_x=0
                    jugador2.accion=0
                if event.key == pygame.K_w:
                    jugador2.var_y=-10
                    jugador2.var_x=0
                    jugador2.accion=3
                if event.key == pygame.K_p:
                    b=Bala()
                    b.rect.x = jugador2.rect.x
                    b.rect.y = jugador2.rect.y+20
                    balas.add(b)
                    todos.add(b)
            if event.type == pygame.KEYUP:
                jugador.var_x=0
                jugador.var_y=0
                jugador2.var_x=0
                jugador2.var_y=0
        jugador.image=m[0+jugador.con][jugador.accion]
        jugador2.image=m2[0+jugador2.con][jugador2.accion]

        #Logica del juego
        for e in enemigos:
            if e.disparar:
                b=Bala()
                b.vel_x=-10
                b.rect.x = e.rect.x
                b.rect.y = e.rect.y
                todos.add(b)
                balas_e.add(b)
                e.disparar=False
                e.tempdis=random.randrange(150)

        for b in balas_e:
            if b.rect.x > ancho:
                balas_e.remove(b)
                todos.remove(b)
            ls_colbe=pygame.sprite.spritecollide(b,jugadores,False)
            for j in ls_colbe:
                j.salud-=1
                balas_e.remove(b)
                todos.remove(b)

        #Colision de Balas
        eliminados=0
        for b in balas:
            ls_colb=pygame.sprite.spritecollide(b,enemigos,True)
            for e in ls_colb:
                enemigos.remove(e)
                todos.remove(e)
                balas.remove(b)
                todos.remove(b)
                eliminados+=1

        for j in jugadores:
            if j.salud == 0:
                jugadores.remove(j)
                todos.remove(j)
                go=True
        if go:
            break

        jud1=fuente.render(str(jugador.salud),False,[255,255,255])
        jud2=fuente.render(str(jugador2.salud),False,[255,255,255])


        todos.update()
        pantalla.fill([0,0,0])
        pantalla.blit(fondo,[0,0])
        todos.draw(pantalla)

        pantalla.blit(texto1,[10,alto-600])
        pantalla.blit(jud1,[110,alto-600])
        pantalla.blit(texto2,[160,alto-600])
        pantalla.blit(jud2,[260,alto-600])
        #pantalla.blit(fondo,[0,0])
        pygame.display.flip()
        reloj.tick(10)
    if go:
        fintxt= fuente.render("Fin del juego",False,[255,0,0])
        pantalla.fill([0,255,0])
        pantalla.blit(fintxt,[250,200])
        pygame.display.flip()
        while not fin:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin=True
