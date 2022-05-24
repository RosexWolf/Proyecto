import pygame, random


#Clase de la serpiente 
class Cuerpo:
    def __init__(self,ventana) -> None:
        self.x = 0
        self.y = 0
        self.dir = 0
        self.ventana = ventana
    #Aqui se dibuja la serpiente , en los dos ultimos parametros se puede cambiar el tamaño 
    #aunque creo que es mejor que le pase un sprite 
    def dibujar(self):
        pygame.draw.rect(self.ventana,(255,255,255),(self.x,self.y,10,10))
    #Definicion de el movimiento de la serpiente 
    def Moverse(self):
        if self.dir == 0:
            self.x += 10
        elif self.dir == 1:
            self.x -= 10
        elif self.dir == 2:
            self.y += 10
        elif self.dir == 3:
            self.y -=10

def refrescar(ventana):
    ventana.fill((0,0,0))
    for i in range(len(serpiente)):
        serpiente[i].dibujar()
#Esta funcion debe estar fuera del bucle principal y es la que va hacer que sigan a la cabeza 
def seguir_cabeza():
    for i in range(len(serpiente)-1):
        serpiente[len(serpiente)-i-1].x = serpiente[len(serpiente)-i-2].x
        serpiente[len(serpiente)-i-1].y = serpiente[len(serpiente)-i-2].y


def main():
    global serpiente 
    vetana = pygame.display.set_mode((400,400))
    vetana.fill((0,0,0))
    #Creacion del objeto serpiente, esta en una lista porque la serpiente se compone de varios objetos
    serpiente = [Cuerpo(vetana)]
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #Definicion de las teclas para moverse    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    serpiente[0].dir = 0
                if event.key == pygame.K_LEFT:
                    serpiente[0].dir = 1
                if event.key == pygame.K_DOWN:
                    serpiente[0].dir = 2
                if event.key == pygame.K_UP:
                    serpiente[0].dir = 3
        #Llamando a el metodo moverse y se le pone en la posicion cero osea la cabeza de la serpiente
        #Primer se tiene que llamar este metodo       
        serpiente[0].Moverse()
        #Luego a este porque dentro de este metodo que tendra el ciclo para que se creen mas partes del cuerpo
        refrescar(vetana)
        pygame.display.update()
        pygame.time.delay(100)
        #Esto es necesario ya que este if hace la colicion de la comida con la serpiente
        #Basicamente dice que se active el if si la serpiente llega a la misma posicion de la manzana
        #Llamada al metodo seguir cabeza
        seguir_cabeza()
        #Choque con los bordes
        if serpiente[0].x >= 400:
            serpiente[0].x = 0
        elif serpiente[0].x <= 0:
            serpiente[0].x = 390
        if serpiente[0].y >= 400:
            serpiente[0].y = 0
        elif serpiente[0].y <= 0:  
            serpiente[0].y = 390

# PD: Recurda que a la hora de implentar el codigo tiene que estar de la forma concecutiva en la que esta o no se va
# a ejecutar correctamente, lo que esta dentro del while tiene que permanecer en el index y el resto lo puedes sacar a un archivo
# a parte y luego llamarlo dentro del index

if __name__ == '__main__':

   main()
   pygame.quit()