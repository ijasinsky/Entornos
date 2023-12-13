from typing import Any
import pygame

class Nave(pygame.sprite.Sprite):
    def __init__(self, posicion):
        super().__init__()
        #Cargamos imagen
        self.image = pygame.image.load("C:\\Users\\alumne-DAM\\Documents\\Entornos\\Entornos\\imagenes\\58e900c5eb97430e819064d5_1.png")
        self.rect = self.image.get_rect()
        #actualizar la posicion dek rectangulo para que coincida con "posicion"
        self.rect.topleft = posicion

    def update(self, *args: Any, **kwargs: Any) -> None:
        teclas = args[0]
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 2
        if teclas[pygame.K_RIGHT]:
            self.rect.x += 2
