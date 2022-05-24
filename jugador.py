import pygame,random

#Configuracion de la pantalla
Width = 400         #Ancho de pantalla
Height = 400        #Alto de pantalla
FPS = 60            #Frames por segundo

RED=(0,0,0)

#Inicializacion de pygame y crear ventana
pygame.init()
pygame.mixer.init()                 #Para el sonido
screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()         #Para los FPS

class Cuerpo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #Aspecto jugador
        self.image = pygame.transform.scale(pygame.image.load("Proyecto2/icono.jpg"),(15,15)).convert() 
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect()    #Rectangulo que encierra el sprite
        self.rect.centerx = 10
        self.rect.bottom = 10
        self.speed_x = 0
        self.speed_y = 0
    
    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        keyState = pygame.key.get_pressed()
        if keyState[pygame.K_RIGHT]:
            self.speed_x = 5
        if keyState[pygame.K_LEFT]:
            self.speed_x = -5
        if keyState[pygame.K_DOWN]:
            self.speed_y = 5
        if keyState[pygame.K_UP]:
            self.speed_y = -5
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y 
        
        xp=self.rect.x

        #Choque con bordes
        if self.rect.x >= 390:
            self.rect.x = 385
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.y >= 390:
            self.rect.y = 385
        if self.rect.y <= 0:
            self.rect.y = 0
        return xp

    def añadir(screen):
        for i in range(len(serpiente)):
            serpiente[i].__init__()

    def seguimiento():
        for i in range(len(serpiente)-1):
            serpiente[len(serpiente)-i-1].x = serpiente[len(serpiente)-i-2].x
            serpiente[len(serpiente)-i-1].y = serpiente[len(serpiente)-i-2].y
    
    def main():
        global serpiente
        serpiente = [Cuerpo(screen)]

all_sprites = pygame.sprite.Group()
