from tracemalloc import start
import turtle
import random

class enemys(object):
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    enemy1=turtle.Turtle()

    def __init__(self,enemy1):
        self.enemy1=enemy1
        start()      

    def start(self,x,y):
        self.enemy1.penup()
        self.enemy1.shape('square')
        self.enemy1.color('red')
        self.enemy1.goto(x,y)
    