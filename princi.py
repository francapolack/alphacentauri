import pygame 
import sys
from pygame.locals import *
largo=400#la cambiaremos a la pantalla la vdd que no me se los parametros
ancho=400
pygame.init() 
pantalla=pygame.display.set_mode((largo,ancho))
pygame.display.set_caption("ALPHA CENTAURI")
icono=pygame.image.load(r"C:\Users\frmuu\Downloads\star.ico")
pygame.display.set_icon(icono)
while True:
    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
