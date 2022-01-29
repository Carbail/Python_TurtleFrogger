import time
from turtle import Screen
from pj import *
from coches import Coches
from marcador import Marcador

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Rana chafadita")

pj = Pj()
coches=Coches()
marcador=Marcador()

screen.listen()
screen.onkey(pj.sube,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    coches.genera_coche()
    coches.mover_coches()
#Fallo
    for coche in coches.todos_coches:
        if coche.distance(pj)<20:
            game_is_on=False
#llegada
    if pj.completo() == True:
        coches.level_up()
        marcador.subenivel()
        marcador.actualiza()
        pj.reset()
    

screen.exitonclick()