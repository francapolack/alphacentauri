import pygame 
import sys
from pygame.locals import *
largo=400#la cambiaremos a la pantalla la vdd que no me se los parametros
ancho=900
pygame.init() 
pantalla=pygame.display.set_mode((largo,ancho))
while True:
    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
