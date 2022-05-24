#Importamos las librerias que necesitamos para el proyecto
from ast import arg
from time import sleep
import pygame,sys
from pygame.locals import *
from enemigo import *
from jugador import *

#Configuracion de la pantalla
Width = 400         #Ancho de pantalla
Height = 400        #Alto de pantalla
FPS = 60            #Frames por segundo

# Colors (R,G,B)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
        
#Inicializacion de pygame y crear ventana
pygame.init()
pygame.mixer.init()                 #Para el sonido
screen = pygame.display.set_mode((Width,Height))

#Icono y titulo del juego
pygame.display.set_caption("The Last Star")
icono=pygame.image.load("Proyecto2/icono.jpg")

#Fondo de Pantalla
Fondo= pygame.transform.scale(pygame.image.load("Proyecto2/background.png"),(Width,Height)).convert()
x=0

#Para los FPS
clock = pygame.time.Clock()

#enemigo
enemigo1 = Enemy()
all_sprites.add(enemigo1)



#jugador
player = Cuerpo()
all_sprites.add(player)

#Game loop
running = True
while running:

    # keep loop running at the right speed
    clock.tick(FPS)
    
    # Fondo en movimiento
    x_relativa=x % Fondo.get_rect().width
    screen.blit(Fondo,(x_relativa - Fondo.get_rect().width,0))
    x-=1

    if x_relativa < Width:
        screen.blit(Fondo,(x_relativa,0))

    # Process input (events)
    for event in pygame.event.get():

        #check for closing window
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    #Dibujar enemigo, manzana y personaje
    all_sprites.draw(screen)

    #Icono del juego
    pygame.display.set_icon(icono) 

    #Movimiento del Jugador
    player.update()
    enemigo1.update()
    

    # Update
    pygame.display.update()
    pygame.time.delay(100)

pygame.quit()