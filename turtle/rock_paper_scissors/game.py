import turtle
import random

# scores of player and computer
g_scorePlayer = 0
g_scoreComputer = 0

# create screen
screen = turtle.Screen()
screen.bgcolor('lightgreen')
screen.setup(width=600, height=500)

# register shapes
shapes = ['rock.gif', 'paper.gif', 'scissors.gif']

# return a random shape
def rand_shape():
    return random.choice(shapes)

screen.addshape('rock.gif')
screen.addshape('paper.gif')
screen.addshape('scissors.gif')

# draw a vertical line to split the window evenly
splitPen = turtle.Turtle()
splitPen.ht()
splitPen.speed(0)
splitPen.up()
splitPen.goto(0, -250)
splitPen.down()
splitPen.color('white')
splitPen.pensize(3)
splitPen.left(90)
splitPen.forward(500)

# Player side
player = turtle.Turtle()
player.shape('rock.gif')
player.up()
player.speed(0)
player.goto(-150, -50)

# player's score
penScorePlayer = turtle.Turtle()
penScorePlayer.up()
penScorePlayer.ht()
penScorePlayer.goto(-150, 150)
penScorePlayer.write("Your Score: 0", align="center", font=('Times', 20, 'bold'))

# computer side
computer = turtle.Turtle()
computer.shape('paper.gif')
computer.up()
computer.speed(0)
computer.goto(150, -50)

# computer's score
penScoreComputer = turtle.Turtle()
penScoreComputer.up()
penScoreComputer.ht()
penScoreComputer.goto(150, 150)
penScoreComputer.write("Computer Score: 0", align="center", font=('Times', 20, 'bold'))

# update score UI
def update_score():
    penScorePlayer.clear()
    penScorePlayer.write("Your Score: %d" % g_scorePlayer, align="center", font=('Times', 20, 'bold'))
    penScoreComputer.clear()
    penScoreComputer.write("Computer Score: %d" % g_scoreComputer, align="center", font=('Times', 20, 'bold'))
    
def rock():
    global g_scoreComputer, g_scorePlayer
    
    player.shape("rock.gif")
    shapeComputer = rand_shape()
    computer.shape(shapeComputer)
    
    if shapeComputer == 'paper.gif':
        g_scoreComputer += 1
    elif shapeComputer == 'scissors.gif':
        g_scorePlayer += 1
    
    update_score()
    
def paper():
    global g_scoreComputer, g_scorePlayer

    player.shape('paper.gif')
    shapeComputer = rand_shape()
    computer.shape(shapeComputer)
    
    if shapeComputer == 'scissors.gif':
        g_scoreComputer += 1
    elif shapeComputer == 'rock.gif':
        g_scorePlayer += 1
    
    update_score()

def scissors():
    global g_scoreComputer, g_scorePlayer

    player.shape('scissors.gif')
    shapeComputer = rand_shape()
    computer.shape(shapeComputer)
    
    if shapeComputer == 'rock.gif':
        g_scoreComputer += 1
    elif shapeComputer == 'paper.gif':
        g_scorePlayer += 1
    
    update_score()
    
# keyboard events handling
screen.listen()
screen.onkey(rock, "r")
screen.onkey(paper, "p")
screen.onkey(scissors, "s")

screen.mainloop()



