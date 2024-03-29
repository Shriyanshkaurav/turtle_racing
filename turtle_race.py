import turtle
import time
import random

WIDTH, HEIGHT = 500,500
COLORS=['red','orange','blue','green','yellow','black','pink','brown','purple']



def get_number_of_racers():
    racers = 0
    while True:
        racers = input("input the number of racers(2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("input is not numeric...try again")
            continue

        if 2<=racers<=10:
            return racers
        else:
            print("number is not in range....Try again")    

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("TURTLE RACING")

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x, y = racer.pos()
            if y>= HEIGHT//2 -10:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH//(len(colors)+1)
    for i, color in enumerate(colors):
        racer =turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i +1) * spacingx,-HEIGHT//2 +20)
        racer.pendown()
        turtles.append(racer)
    return turtles

racers = get_number_of_racers()
init_turtle()


random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with color: ", winner)



'''
racer = turtle.Turtle()
racer.speed(1)
racer.penup()
racer.shape('turtle')
racer.color('red')
racer.forward(100)
racer.left(90)
racer.forward(100)
'''
