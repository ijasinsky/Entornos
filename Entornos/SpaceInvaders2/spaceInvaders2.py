import pygame
import elementos2
import random
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
# grupo_sprites = pygame.sprite.Group(nave)
# grupo_sprites.add(elementos2.Nave((15,100)))
# grupo_sprites.add(nave)
# enemigo = elementos2.Enemigo((50,50))
# grupo_sprites.add(enemigo)
grupo_sprites_todos = pygame.sprite.Group()
grupo_sprites_enemigos = pygame.sprite.Group()
grupo_sprites_balas = pygame.sprite.Group()

grupo_sprites_todos.add(elementos2.Fondo((0,0)))
grupo_sprites_todos.add(nave)


#creacion de enemigos
ultimo_enemigo_creado = 0
frequencia_creacion_enemigos = 2000

#bucle principal
while running:
    #limitamos el bucle al framerate que hemos definido
    reloj.tick(FPS)

    #gestionar la salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    momento_actual = pygame.time.get_ticks()
    if(momento_actual > ultimo_enemigo_creado + frequencia_creacion_enemigos):
        cordX = random.randint(0,pantalla.get_width())
        cordY = 0
        enemigo = elementos2.Enemigo(((cordX, cordY)))
        grupo_sprites_todos.add(enemigo)
        grupo_sprites_enemigos.add(enemigo)
        ultimo_enemigo_creado = momento_actual

    teclas = pygame.key.get_pressed()
    # if teclas[pygame.K_LEFT]:
    #     nave.disparar(grupo_sprites_todos)
    #Fondo
    pantalla.fill((255,255,255))
    #Segundo Sp
    grupo_sprites_todos.update(teclas, grupo_sprites_todos, grupo_sprites_balas)
    grupo_sprites_todos.draw(pantalla)

    #actualizamos pantalla
    pygame.display.flip()
#finalizamos el juego
pygame.quit()
