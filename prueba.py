import turtle 

ventana = turtle.Screen()
ventana.title('El juego de la serpiente que come y engorda, porque quiere quedar como una esfera')
ventana.setup(width=800, height=800)
ventana.bgcolor('crimson')


#Creacion turtugas
def creacion_cabezas(forma,color):
    cabeza=turtle.Turtle()
    cabeza.speed(0)
    cabeza.penup()
    cabeza.shape(forma)
    cabeza.color(color)
    cabeza.goto(0,0)
    return cabeza

cabezaS = creacion_cabezas('classic','black')
cabezaS.shapesize(stretch_wid=1.5, stretch_len= 1.5, outline=5)
comida = creacion_cabezas('circle','cyan2')
comida.shapesize(stretch_wid=0.8, stretch_len= 0.8, outline= None)
comida.goto(30,100)
cabezaS.direccion = 'quieta'


#Funciones teclado
def arriba():
    cabezaS.direccion= 'arriba'
def abajo():
    cabezaS.direccion= 'abajo'
def izquierda():
    cabezaS.direccion= 'izquierda'
def derecha():
    cabezaS.direccion= 'derecha'

#Teclado
ventana.listen()
ventana.onkeypress(arriba,'Up')
ventana.onkeypress(abajo,'Down')
ventana.onkeypress(izquierda,'Left')
ventana.onkeypress(derecha,'Right')


#Movimiento
def movimiento():
    if cabezaS.direccion == 'arriba' :
        y = cabezaS.ycor()
        cabezaS.sety(y+20)
    if cabezaS.direccion == 'abajo':
        y = cabezaS.ycor()
        cabezaS.sety(y-20)
    if cabezaS.direccion == 'izquierda':
        x = cabezaS.xcor()
        cabezaS.setx(x-20)
    if cabezaS.direccion == 'derecha':
        x = cabezaS.xcor()
        cabezaS.setx(x+20)
    



