import pygame
import math
class Nave:
    def __init__(self) -> None:
        self.x = 100
        self.y = 500
        imagenes_cargadas = [pygame.image.load("C:\\Users\\alumne-DAM\\Documents\\Entornos\\Entornos\\imagenes\\58e900c5eb97430e819064d5_1.png"), 
                         pygame.image.load("C:\\Users\\alumne-DAM\\Documents\\Entornos\\Entornos\\imagenes\\58e900c5eb97430e819064d5_2.png")]
        self.imagenes = [pygame.transform.scale(imagenes_cargadas[0], (130,190)),
                         pygame.transform.scale(imagenes_cargadas[1], (130,190))]
        self.contador = 0

    def moverDerecha(self):
        self.x += 1
        pantalla = pygame.display.get_surface()
        limite = pantalla.get_width()
        self.x = min(self.x, limite - self.imagenes[0].get_width())

    def moverIzquierda(self):
        self.x -= 1
        limite = 0
        self.x = max(self.x, limite)
    
    def dibujar(self):
        # aumenta contador
        self.contador = (self.contador + 1) % 40
        #cojo el punteri a la pantalla
        pantalla = pygame.display.get_surface()
        #
        seleccionada = self.contador // 20
        pantalla.blit(self.imagenes[seleccionada], (self.x, self.y))

class Fondo:
    def __init__(self) -> None:
        #localizar la pantalla
        pantalla = pygame.display.get_surface()
        #Cargamos la imagen 
        imagen = pygame.image.load("C:\\Users\\alumne-DAM\\Documents\\Entornos\\Entornos\\imagenes\\fondo2.jpeg")
        #Escalamos la imagen para que encaje en el ancho de la pantalla
        self.fondo = pygame.transform.scale(imagen,(pantalla.get_width(), imagen.get_height()))
        #Scroll
        self.scroll = 0
        #cuantas piezas de fondo necesitamos
        self.piezas = math.ceil(pantalla.get_height() / self.fondo.get_height()) + 1
    
    def dibujar(self):
        self.scroll +=1
        
        #localizar la pantalla
        pantalla = pygame.display.get_surface()

        if self.scroll > self.fondo.get_height():
            self.scroll = 0

        for i in range(0, self.piezas):
            pantalla.blit(self.fondo,(0, - self.fondo.get_height() + i * self.fondo.get_height() + self.scroll))