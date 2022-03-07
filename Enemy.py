import turtle

window=turtle.Screen()
window.bgcolor('grey')



class enemy(object):
    element=turtle.Turtle()
    position=[]
    def __init__(self,element,position):
        self.element=element
        self.position=position
    def begin(self):
        self.element.penup()
        self.element.shape('turtle')
        self.element.color('red')
        self.element.goto(self.position[0],self.position[1])
        turtle.speed(1)
    def Move(self): 
        turtle.position()
        turtle.forward(25)
        turtle.position()
        turtle.backward(-75)
        turtle.position()
        

enemy=enemy(turtle.Turtle(),[0,0])

enemy.begin()
enemy.Move()


window.mainloop()