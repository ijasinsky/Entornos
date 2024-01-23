import math
import pygame
from typing import Any

class Planeta(pygame.sprite.Sprite):
    def __init__(self) -> None:
        self.x = 100
        self.y = 50
        super().__init__()
        self.Planeta = pygame.transform.scale(pygame.image.load("Entornos\\Newgame\\Imagenes\\PlanetaconCañon.png"), (300, 300))

    def moverDerecha(self):
        self.x += 1
        pantalla = pygame.display.get_surface()
        limite = pantalla.get_width()
        self.x = min(self.x, limite - self.planeta.get_width())

    def moverIzquierda(self):
        self.x -= 1
        limite = 0
        self.x = max(self.x, limite)

    def dibujar(self):

        pantalla = pygame.display.get_surface()
        
        pantalla.blit(self.Planeta, (self.x, self.y))

class Fondo(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pantalla = pygame.display.get_surface()
        imagen = (pygame.image.load("Entornos\\Newgame\\Imagenes\\Planeta.png"))
        
        self.fondo = pygame.transform.scale(imagen,(pantalla.get_width(), imagen.get_height()))
        self.scroll = 0
        self.piezas = math.ceil(pantalla.get_height() / self.fondo.get_height()) + 1

    def dibujar(self):
        self.scroll +=1
        
        #localizar la pantalla
        pantalla = pygame.display.get_surface()

        if self.scroll > self.fondo.get_height():
            self.scroll = 0

        for i in range(0, self.piezas):
            pantalla.blit(self.fondo,(0, - self.fondo.get_height() + i * self.fondo.get_height() + self.scroll))

class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load())

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect.y -= 5