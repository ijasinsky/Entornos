import pygame
import elementos2
import random
import pygame_menu
pygame.init()

#creamos pantalla
tamaño = (1000, 800)
pantalla = pygame.display.set_mode(tamaño)

#reloj
reloj = pygame.time.Clock()
FPS = 60

font = pygame.font.Font(None, 30)





 #crear grupo sprites
# grupo_sprites = pygame.sprite.Group(nave)
# grupo_sprites.add(elementos2.Nave((15,100)))
# grupo_sprites.add(nave)
# enemigo = elementos2.Enemigo((50,50))
# grupo_sprites.add(enemigo)



#creacion de enemigos
ultimo_enemigo_creado = 0
frequencia_creacion_enemigos = 2000

def set_difficulty(value, difficulty):
    global frequencia_creacion_enemigos
    frequencia_creacion_enemigos = difficulty



def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():

    #booleano de control
    running = [True]

    global ultimo_enemigo_creado
    global reloj
    global frequencia_creacion_enemigos
    global FPS

    posicion = (300,100)
    nave = elementos2.Nave(posicion)
    global grupo_sprites_balas
    global grupo_sprites_enemigos
    global grupo_sprites_todos

    grupo_sprites_todos = pygame.sprite.Group()
    grupo_sprites_enemigos = pygame.sprite.Group()
    grupo_sprites_balas = pygame.sprite.Group()

    grupo_sprites_todos.add(elementos2.Fondo((0,0)))
    # grupo_sprites_todos.add(elementos2.Fondo((0,-pantalla.get_height())))
    grupo_sprites_todos.add(nave)

    pausado = False

        #bucle principal
    while running[0]:
        #limitamos el bucle al framerate que hemos definido
        reloj.tick(FPS)

        #gestionar la salida
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running[0] = False

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_ESCAPE]:
            running[0] = False
        if teclas[pygame.K_q]:
            pausado = not pausado
        #Fondo
        pantalla.fill((255,255,255))

        if not pausado:
            #Se crea enemigos
            momento_actual = pygame.time.get_ticks()
            if(momento_actual > ultimo_enemigo_creado + frequencia_creacion_enemigos):
                cordX = random.randint(0,pantalla.get_width())
                cordY = -0
                enemigo = elementos2.Enemigo(((cordX, cordY)))
                grupo_sprites_todos.add(enemigo)
                grupo_sprites_enemigos.add(enemigo)
                ultimo_enemigo_creado = momento_actual
        
            else:
                
                texto = font.render("Pausa", True, "White")
                pantalla.blit(texto, (pantalla.get_width() / 2, pantalla.get_height()/2))

            grupo_sprites_todos.update(teclas, grupo_sprites_todos, grupo_sprites_balas, grupo_sprites_enemigos, running)
            grupo_sprites_todos.draw(pantalla)

        #actualizamos pantalla
        pygame.display.flip()

menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')
menu.add.selector('Difficulty :', [('Hard', 200), ('Easy', 2000)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(pantalla)
#finalizamos el juego
pygame.quit()
