COLORES = ["red", "orange", "yellow", "green", "blue", "purple"]
CARRILES = range(-250,250,10)
from turtle import Turtle
import random

class Coches:
    def __init__(self):
        self.todos_coches = []
        self.nivel=0
        
    def genera_coche(self):
        
        #cada vez que llamamos hay un % de generar coche, sirve para modular dif
        coches_nivel= random.randint(1,6)
        if coches_nivel==1:
            nuevo_coche = Turtle ("square")
            nuevo_coche.shapesize(stretch_wid=1, stretch_len=2)
            nuevo_coche.penup()
            nuevo_coche.color(random.choice(COLORES))
            random_y= random.choice(CARRILES)
            nuevo_coche.goto(300, random_y)
            self.todos_coches.append(nuevo_coche)
        coches_extra=range(0,self.nivel%3)
        for extra in coches_extra:
            if extra != 0:
                coches_nivel= random.randint(1,4)
                if coches_nivel==1:
                    nuevo_coche = Turtle ("square")
                    nuevo_coche.shapesize(stretch_wid=1, stretch_len=2)
                    nuevo_coche.penup()
                    nuevo_coche.color(random.choice(COLORES))
                    random_y= random.choice(CARRILES)
                    nuevo_coche.goto(300, random_y)
                    self.todos_coches.append(nuevo_coche)                
        
        
    def mover_coches(self):
        for coche in self.todos_coches:
            coche.backward(5+1*self.nivel) 
    
    def level_up(self):
        self.nivel +=1
        for coche in self.todos_coches:
            coche.hideturtle()           
        self.todos_coches=[]

        
    
        
