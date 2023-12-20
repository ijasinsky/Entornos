from typing import Any
import pygame

class Nave(pygame.sprite.Sprite):
    def __init__(self, posicion):
        super().__init__()
        self.manolos = [pygame.image.load("C:\\Users\\alumne-DAM\\Documents\\Entornos\\Entornos\\imagenes\\58e900c5eb97430e819064d5_1.png"), pygame.image.load("C:\\Users\\alumne-DAM\\Documents\\Entornos\\Entornos\\imagenes\\58e900c5eb97430e819064d5_2.png")]
        self.indice_manolo = 0
        self.image = self.manolos[self.indice_manolo]
        self.contador_imagen = 0
        #Cargamos imagen
        self.image = pygame.image.load("C:\\Users\\alumne-DAM\\Documents\\Entornos\\Entornos\\imagenes\\58e900c5eb97430e819064d5_1.png")
        self.rect = self.image.get_rect()
        #actualizar la posicion dek rectangulo para que coincida con "posicion"
        self.rect.topleft = posicion
        self.ultimo_disparo = 0

    def update(self, *args: Any, **kwargs: Any) -> None:
        teclas = args[0]
        pantalla = pygame.display.get_surface()

        grupo_sprites_todos = args[1]
        grupo_sprites_balas = args[2]

        if teclas[pygame.K_LEFT]:
            self.rect.x -= 2
            self.rect.x = max(0, self.rect.x)
        if teclas [pygame.K_SPACE]:
            self.disparar(grupo_sprites_todos, grupo_sprites_balas)
        if teclas[pygame.K_RIGHT]:
            self.rect.x += 2
            self.rect.x = min(pantalla.get_width()-self.image.get_width(), self.rect.x)
            #gestionar animacion
        self.contador_imagen = (self.contador_imagen + 1) % 40
        self.indice_manolo = self.contador_imagen // 20
        self.image = self.manolos[self.indice_manolo]

    def disparar(self, grupo_sprites_todos, grupo_sprites_balas):
        momento_actual = pygame.time.get_ticks()
        if momento_actual > self.ultimo_disparo + 200:
            x = self.rect.x + self.image.get_width() / 2
            y = self.rect.y
            bala = Bala((x,y))
            grupo_sprites_todos.add(bala)
            grupo_sprites_balas.add(bala)
            self.ultimo_disparo = momento_actual

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, posicion):
        super().__init__()
        #Cargamos imagen
        manolo = pygame.image.load("C:\\Users\\alumne-DAM\\Documents\\Entornos\\Entornos\\imagenes\\58e900c5eb97430e819064d5_1.png")
        self.image = pygame.transform.rotate(manolo, 180)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        #actualizar la posicion del rectangulo para que coincida con "posicion"
        self.rect.topleft = posicion

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect.y += 1

        pantalla = pygame.display.get_surface()
        if(self.rect.y > pantalla.get_height()):
            self.kill()

            #capturar args[2]
            grupo_sprites_balas = args[2]
            bala_colision = pygame.sprite.spritecollideany(self,grupo_sprites_balas, pygame.sprite.collide_mask)
            if bala_colision:
                self.kill()
                bala_colision.kill()

class Fondo(pygame.sprite.Sprite):
    def __init__(self, posicion):
        super().__init__()
        #Cargamos imagen
        imagenes_cargada = pygame.image.load("C:\\Users\\alumne-DAM\\Documents\\Entornos\\Entornos\\imagenes\\fondo2.jpeg")
        pantalla = pygame.display.get_surface()
        self.image = pygame.transform.scale(imagenes_cargada,(pantalla.get_width(), pantalla.get_height()))
        self.rect = self.image.get_rect()
        #actualizar la posicion del rectangulo para que coincida con "posicion"
        self.rect.topleft = (0,0)

class Bala(pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        self.image = pygame.Surface((5,10))
        self.image.fill((255,0,0))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = posicion

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect.y -= 5