import pygame
import elementos2

pygame.init()

#creamos pantalla
tamaño = (800, 600)
pantalla = pygame.display.set_mode(tamaño)

#reloj
reloj = pygame.time.Clock()
FPS = 60

#booleano de control
running = True

posicion = (200,200)
nave = elementos2.Nave(posicion)

 #crear grupo sprites
grupo_sprites = pygame.sprite.Group(nave)
grupo_sprites.add(elementos2.Nave((15,100)))
grupo_sprites.add(elementos2.Nave((400,100)))

#bucle principal
while running:
    #limitamos el bucle al framerate que hemos definido
    reloj.tick(FPS)

    #gestionar la salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    teclas = pygame.key.get_pressed()
    #Fondo
    pantalla.fill((255,255,255))
    #Segundo Sp
    grupo_sprites.update(teclas)
    grupo_sprites.draw(pantalla)

    #actualizamos pantalla
    pygame.display.flip()
#finalizamos el juego
pygame.quit()
