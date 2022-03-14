from hashlib import new
import turtle
from Enemy import enemys

ventana = turtle.Screen()
ventana.title("Juego de la Serpiente con Python")
ventana.bgcolor("Black")
ventana.setup(width=600,height=600)
ventana.tracer(0)

enemy=enemys(turtle.Turtle())
enemy.start('x','y')

ventana.mainloop()