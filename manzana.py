import pygame
from pygame.locals import *    
 
pygame.init()
 
ancho = 1000
alto = 800
velocidad_X = 1
velocidad_Y = 2
terminado = False
 
Ventana = pygame.display.set_mode( (ancho, alto) )

 
Manzana = pygame.image.load("apple.png")
rectanguloManzana = Manzana.get_rect()
rectanguloManzana.left = 200
rectanguloManzana.top = 100
 

 
 
while not terminado:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: terminado = True
 
   
    rectanguloManzana.left += velocidad_X
    rectanguloManzana.top += velocidad_Y
    if rectanguloManzana.left < 0 or rectanguloManzana.right > ancho:
        velocidad_X = -velocidad_X
    if rectanguloManzana.top < 0 or rectanguloManzana.bottom > alto:
        velocidad_Y = -velocidad_Y
 
    Ventana.fill( (0,0,0) )
    Ventana.blit(Manzana, rectanguloManzana)
    pygame.display.flip()
 
pygame.quit()
