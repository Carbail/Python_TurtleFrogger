FINISH_LINE_Y = 280
from turtle import Turtle

class Pj(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0,-280)
        self.setheading(90)
    
    def sube(self):
        self.forward(10)
    
    def completo(self):
        if self.ycor() >= 280:
            return True
        else:
            return False
    
    def reset(self):
        self.goto(0,-280)
        