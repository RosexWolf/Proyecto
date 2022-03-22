from email.contentmanager import raw_data_manager
from re import A, S
from tkinter import Y
import turtle
import prueba as diseño
import time
import random
Parte = []
cabeza = diseño.cabezaS
comida = diseño.comida
while True: 
    diseño.ventana.update()
    diseño.movimiento()
    time.sleep(0.05)
    #choque de los bordes
    if cabeza.xcor() > 800 or cabeza.xcor() < -800 or cabeza.ycor() > 800 or cabeza.ycor() < -800:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direccion = 'quieta'
    #Colision comida 
    if cabeza.distance(comida) < 20:
        x = random.randint(-14,14)
        y = random.randint(-14,14)
        #Este 20 se tiene que verificar con los pixeles de la pantalla
        comida.goto(x*20,y*20)
        #Suma de cabezas nustra serpiente
        nueva_parte = diseño.creacion_cabezas('classic', 'black')
        nueva_parte.shapesize(stretch_len=1.5, stretch_wid=1.5)
        nueva_parte.direccion = 'quieta'
        Parte.append(nueva_parte)
    
    #mover partes 

    partes_totales = len(Parte)

    for i in range(partes_totales -1, 0, -1):
        x = Parte[i-1].xcor()
        y = Parte[i-1].ycor()
        Parte[i].goto(x,y)


    if partes_totales > 0:
        x = cabeza.xcor()
        y= cabeza.ycor()
        Parte[0].goto(x,y)
    
