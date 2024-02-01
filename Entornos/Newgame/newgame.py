import pygame
from newgameplus import Planeta
import sys
#Inicio Pygame
pygame.init()
tamaño = (1000, 800)
pantalla = pygame.display.set_mode(tamaño)

posicion = (230, 150)
Planeta = Planeta(posicion)
pantalla.fill((255,255,255))
#Pantalla
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Planeta')
#Titulo
pygame.display.set_caption('Mi juego')
#Icono de ventana
icono = pygame.image.load("Entornos\\Newgame\\Imagenes\\png-transparent-universe-galaxy-milky-way-uranus-cartoon-s-blue-computer-wallpaper-sphere.png")
pygame.display.set_icon(icono)
#Fondo
pantalla = pygame.transform.scale(pygame.image.load("Entornos\\Newgame\\Imagenes\\estrellas-sobre-fondo-cielo-nocturno_697972-329.jpg").convert(), (800, 600))
ventana.blit(pantalla,(0,0))
# Dibujar Planeta
Planeta.dibujar(posicion)


pygame.mouse.set_visible(0) #Oculto el puntero en 0
x,y = pygame.mouse.get_pos()
x = x/6
angulo = 180 - x

img = pygame.transform.rotate(Planeta, (angulo))
img_rect = img.get_rect()
img_rect.center = posicion
ventana.blit(img, img_rect)
#Bucle de ejecución
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()