import pygame
from typing import Any

class Planeta(pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        self.Planeta = pygame.transform.scale(pygame.image.load("Entornos\\Newgame\\Imagenes\\PlanetaconCañon.png").convert(), (350, 350))
        self.rect = self.Planeta.get_rect()
        self.rect.topleft = (posicion)

    def dibujar(self, posicion):

        pantalla = pygame.display.get_surface()
        
        pantalla.blit(self.Planeta, (posicion))