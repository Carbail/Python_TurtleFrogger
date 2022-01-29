from turtle import Turtle
FONT = ("Robota", 24, "normal")


class Marcador(Turtle):
    def __init__(self):
        super().__init__()
        self.nivel=1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.actualiza()
       

    def actualiza(self):
        self.clear()
        self.write(f"Level: {self.nivel}", align="left", font=FONT)

    def subenivel(self):
        self.nivel+=1


