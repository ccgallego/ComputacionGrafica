import pygame


if __name__ == '__main__':

    pygame.init()
    pantalla=pygame.display.set_mode([640,480])
    fin=False
    circulos=[]
    circulo1=[0,0]
    circulo2=[0,0]
    var_x=0
    var_y =0
    contador =0
    pygame.display.flip()
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type==pygame.MOUSEBUTTONDOWN:
                contador+=1
                if contador==1:
                    circulo1[0] = event.pos[0]
                    circulo1[1] = event.pos[1]
                    print circulo1
                    circulos.append(circulo1)
                    pygame.draw.circle(pantalla,[255,0,0], circulos[0] , 5)
                    pygame.display.flip()
                if contador==2:
                    circulo2[0] = event.pos[0]
                    circulo2[1] = event.pos[1]
                    print circulo2
                    circulos.append(circulo2)
                    pygame.draw.circle(pantalla,[0,255,0], circulos[1] , 5)
                    pygame.display.flip()
                    print circulos

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print "arriba"
                var_y =-1
            if event.key == pygame.K_RIGHT:
                print "derecha"
                var_x =+1
            if event.key == pygame.K_LEFT:
                print "izquiera"
                var_x =-1
            if event.key == pygame.K_DOWN:
                print "abajo"
                var_y =+1
            if event.key == pygame.K_SPACE:
                print "DETENER"
                var_x=0
                var_y=0


        circulos=[circulo1,circulo2]
        circulos[0][0]+=var_x
        circulos[0][1]+=var_y
        circulos[1][0]+=var_x
        circulos[1][1]+=var_y
        if circulos[0][0]==10 or circulos[1][0]==630:
            var_x =0
        if circulos[0][1]==10 or circulos[1][1]==470:
            var_y =0
        pantalla.fill([0,0,0])
        pygame.draw.circle(pantalla,[255,0,0], circulos[0] , 5)
        pygame.draw.circle(pantalla,[255,0,0], circulos[1] , 5)
        pygame.display.flip()
