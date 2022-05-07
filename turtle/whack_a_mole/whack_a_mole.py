import turtle
import random

g_score = 0  # score of the game

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.screensize(canvwidth=780, canvheight=580)
screen.bgcolor('yellow')

# register a gif picture as a shape
screen.register_shape('mole.gif')
screen.register_shape('hammer.gif')

mole = turtle.Turtle()
pen = turtle.Turtle()
hammer = turtle.Turtle()

pen.ht()
pen.penup()

hammer.penup()
hammer.speed(0)

# select the shape registed
mole.shape('mole.gif')
hammer.shape('hammer.gif')

def show_score():
    pen.hideturtle()
    pen.clear()
    pen.color('red')
    pen.home()
    pen.write('YOUR SCORE: ' + str(g_score), align='center', font=("Arial", 20, 'normal'))



# move turtle randomly
def move_random():
    sw, sh = screen.screensize()
    minX = -sw/2
    maxX = sw/2
    minY = -sh/2
    maxY = sh/2
    x = random.randint(minX,maxX)
    y = random.randint(minY, maxY)
    mole.penup()
    mole.speed(3)
    mole.goto(x,y)
    

# callback function for timer
def on_timer():
    move_random()
    screen.ontimer(on_timer, 100)

# callback function for click on turtle
def on_click(x, y):
    global g_score
    g_score += 1
    show_score()

def on_screen_click(x,y):
    print(x,y)
    hammer.goto(x,y)
    hammer.st()
    
    
mole.onclick(on_click)
    
screen.ontimer(on_timer, 100)
screen.onclick(on_screen_click)


screen.mainloop()
