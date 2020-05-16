import pygame


if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([640,480])
    pos=[10,10]
    reloj=pygame.time.Clock()
    pygame.draw.circle(pantalla,[0,255,0],pos,10)
    pygame.display.flip()
    var_y=0
    var_x=0
    x=0
    y=0
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                print 'tecla'
                if event.key == pygame.K_RIGHT:
                    var_x=+1
                if event.key == pygame.K_DOWN:
                    var_y=+1
                if event.key == pygame.K_UP:
                    var_y=-1
                if event.key == pygame.K_LEFT:
                    var_x=-1
                if event.key == pygame.K_SPACE:
                    var_y=0
                    var_x=0

        pos[0]+=var_x
        pos[1]+=var_y
        pantalla.fill([0,0,0])
        pygame.draw.circle(pantalla,[0,255,0],pos,10)
        pygame.display.flip()
        if pos[0]==630 or pos[0]==10:
            var_x=0
            reloj.tick(100)
        if pos[1]==470 or pos[1]==10:
            var_y=0
            reloj.tick(100)
