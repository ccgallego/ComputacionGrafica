import pygame

if __name__ == '__main__':

    pygame.init()
    pantalla=pygame.display.set_mode([640,480])
    fin=False
    var=3
    ls=[]
    ls2=[]
    cont=0
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                cont+=1
                if cont == 1:
                    a=list(event.pos)
                    ls.append(a)
                if cont == 2:
                    b=event.pos
                    ls.append(b)
                if cont == 3:
                    c=list(event.pos)
                    ls.append(c)
                for pto in ls:
                    pygame.draw.circle(pantalla,[0,255,0],pto,10)
                    pygame.display.flip()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    a[0]-=var
                    b[0]-=var
                    c[0]-=var
                    pantalla.fill([0,0,0])
                    pygame.draw.circle(pantalla,[0,150,110],a,10)
                    pygame.draw.circle(pantalla,[120,150,0],b,10)
                    pygame.draw.circle(pantalla,[0,255,200],c,10)
                if event.key == pygame.K_w:
                    a[1]-=var
                    b[1]-=var
                    c[1]-=var
                    pantalla.fill([0,0,0])
                    pygame.draw.circle(pantalla,[0,150,110],a,10)
                    pygame.draw.circle(pantalla,[120,150,0],b,10)
                    pygame.draw.circle(pantalla,[0,255,200],c,10)
                if event.key == pygame.K_s:
                    a[1]+=var
                    b[1]+=var
                    c[1]+=var
                    pantalla.fill([0,0,0])
                    pygame.draw.circle(pantalla,[0,150,110],a,10)
                    pygame.draw.circle(pantalla,[120,150,0],b,10)
                    pygame.draw.circle(pantalla,[0,255,200],c,10)
                if event.key == pygame.K_d:
                    a[0]+=var
                    b[0]+=var
                    c[0]+=var
                    pantalla.fill([0,0,0])
                    pygame.draw.circle(pantalla,[0,150,110],a,10)
                    pygame.draw.circle(pantalla,[120,150,0],b,10)
                    pygame.draw.circle(pantalla,[0,255,200],c,10)
                pygame.display.flip()
