import pygame

if __name__ == '__main__':

    pygame.init()
    pantalla=pygame.display.set_mode([640,480])
    fin=False
    var=3
    a=[320,240]
    b=[320,240]
    c=[320,240]
    d=[320,240]
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    a[0]+=var
                    b[0]-=var
                    c[1]+=var
                    d[1]-=var
                    pantalla.fill([0,0,0])
                    pygame.draw.circle(pantalla,[0,150,110],a,10)
                    pygame.draw.circle(pantalla,[120,150,0],b,10)
                    pygame.draw.circle(pantalla,[0,255,200],c,10)
                    pygame.draw.circle(pantalla,[200,255,0],d,10)
                    pygame.display.flip()
