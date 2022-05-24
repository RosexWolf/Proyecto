from tkinter.tix import Tree
import pygame
from pygame.locals import *
from jugador import *
import threading
import time

RED=(255,0,0)

class Enemy(pygame.sprite.Sprite):
    # Sprite for the player
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Proyecto2/icono.jpg"),(30,30)) #Aspecto Enemigo
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect()    #Rectangulo que encierra el sprite
        self.rect.centerx = 50
        self.rect.bottom = 200
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        #Seguir al Jugador

        all_sprites.update(self)

all_sprites = pygame.sprite.Group()



        
    