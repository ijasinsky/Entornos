import pygame
from elementos import Nave, Fondo

pygame.init()

pantalla = pygame.display.set_mode((1200,800))
reloj = pygame.time.Clock()
FPS = 60
# Imgavion = pygame.image.load("Entornos/imagenes/58e900c5eb97430e819064d5.png")
# avion = pygame.transform.scale(Imgavion, (190,130))
# avion_rect = avion.get_rect()


salir = False

# posIzda = 30
# posTop = 30
nave = Nave()
fondo = Fondo()    
while not salir:
    reloj.tick(FPS)
    #gestionar eventoss
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        nave.moverIzquierda()
    if teclas[pygame.K_RIGHT]:
        nave.moverDerecha()
    # if teclas[pygame.K_UP]:
    #     posTop -= 1
    # if teclas[pygame.K_DOWN]:
    #     posTop += 1

    #gestionaar cambios
    # pantalla.fill((0,15,80))
    fondo.dibujar()
    nave.dibujar()
    
    # pygame.draw.rect(pantalla, (25,25,250), pygame.Rect(posIzda,posTop,60,60))

    # pantalla.blit(avion, (posIzda, posTop))
    # #redibujar el juego
    pygame.display.flip()
    

pygame.quit()