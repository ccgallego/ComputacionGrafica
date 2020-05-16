import pygame

if __name__ == '__main__':

    pygame.init()
    pantalla=pygame.display.set_mode([900,700])
    tux=pygame.image.load('astro.jpg')
    fin=False
    pos_x=0
    vel_x=0
    reloj=pygame.time.Clock()
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        pos=pygame.mouse.get_pos()
        if pos[0] >= 500:
            vel_x=-2
        elif pos[0] <= 100:
            vel_x=+2
        else:
            vel_x=0
        print pos
        pantalla.blit(tux,[pos_x,0])
        pygame.display.flip()
        pos_x+=vel_x
        pantalla.fill([255,255,255])
