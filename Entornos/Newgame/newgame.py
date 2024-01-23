import pygame
from newgameplus import Planeta, Fondo, Bala
import sys
#Inicio Pygame
pygame.init()

Planeta = Planeta()
#Pantalla
ventana = pygame.display.set_mode((500, 400))
#Titulo
pygame.display.set_caption('Mi juego')
#Icono de ventana
icono = pygame.image.load("Entornos\\Newgame\\Imagenes\\png-transparent-universe-galaxy-milky-way-uranus-cartoon-s-blue-computer-wallpaper-sphere.png")
pygame.display.set_icon(icono)
#Fondo
fondo = pygame.transform.scale(pygame.image.load("Entornos\imagenes\istockphoto-971578384-170667a.webp"), (500, 400))
ventana.blit(fondo,(0,0))

Planeta.dibujar()
#Bucle de ejecución
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()