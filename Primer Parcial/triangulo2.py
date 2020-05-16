import pygame

if __name__ == '__main__':
    pygame.init()
    contador=0
    puntos=[]
    pantalla=pygame.display.set_mode([600,600])
    var=5
    fin=False
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                contador+=1
                if contador == 1:
                    a=list(event.pos)
                    puntos.append(a)
                if contador == 2:
                    b=list(event.pos)
                    puntos.append(b)
                if contador == 3:
                    c=list(event.pos)
                    puntos.append(c)
                # if contador == 4:
                #     d=list(event.pos)
                #     puntos.append(d)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    for pto in puntos:
                        pto[0]-=var
                if event.key == pygame.K_d:
                    for pto in puntos:
                        pto[0]+=var
                if event.key == pygame.K_w:
                    for pto in puntos:
                        pto[1]-=var
                if event.key == pygame.K_s:
                    for pto in puntos:
                        pto[1]+=var
            pantalla.fill([0,0,0])
        for pto in puntos:
            pygame.draw.circle(pantalla,[0,255,0],pto,5)
        if len(puntos) == 3:
            pygame.draw.polygon(pantalla,[0,255,0],puntos,3)
        pygame.display.flip()
