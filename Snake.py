#Actividad 2 : Snake
#Alfaro González Arturo 
#Rodrigo Aldahir Rosete Flores

#Se importan las librerias correspondientes:
import random
from turtle import *
from random import randrange
from freegames import square, vector

#Se establecen los valores iniciales para la comida y la serpiente:
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#Se definen los posibles colores a utilizar:
colors = ["orange", "blue", "yellow", "black", "green"]

#Función para selecciónar de manera aleatoria un color:
def selectRandom(colors):
    #Selecciona aleatoriamente de la lista de colores:
    color = random.choice(colors)
    colors.remove(color)
    return color

#Cambia la dirección de la serpiente:
def change(x, y):
    aim.x = x
    aim.y = y

#Define y detecta los límites de la serpiente:
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

#Función para la movilidad de la serpiente:
def move():
    head = snake[-1].copy()
    head.move(aim)
    #Detecta los posibles escenarios en donde la serpiente pierde y la vuelve roja además de parar el juego:
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    #Si la serpiente alcanza la comida se establece una nueva posición para la comida de manera aleatoria en los valores definidps:
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    #Se define el cuerpo de la serpiente y alimento:
    for body in snake:
        square(body.x, body.y, 9, color_snake)

    square(food.x, food.y, 9, color_food)
    update()
    ontimer(move, 100)
    #Se establece el movimiento de la comida de manera aleatoria con los límites:
    lmao = randrange(0,10)
    if lmao == 9:
        food.x = food.x +10
        if food.x > 180:
            food.x = -180

    lmao = randrange(0,10)
    if lmao == 5:
        food.y = food.y +10
        if food.y > 180:
            food.y = -180

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
#Detección de jugabilidad:
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down') 
color_food = selectRandom(colors)
color_snake = selectRandom(colors)
move()
done()