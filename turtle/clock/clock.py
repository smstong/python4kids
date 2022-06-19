import turtle
import time
import math

turtle.mode('logo') # clockwise, must be called at first

facePen = turtle.Turtle()
secHand = turtle.Turtle()
minHand = turtle.Turtle()
hourHand = turtle.Turtle()
digitalPen = turtle.Turtle()

facePen.up()
facePen.speed(0)
facePen.color('black')
facePen.ht()

digitalPen.ht()
digitalPen.speed(0)
digitalPen.color('white')
digitalPen.up()

secHand.up()
secHand.speed(0)
secHand.color('red')
secHand.pensize(2)
secHand.ht()

minHand.up()
minHand.speed(0)
minHand.color('green')
minHand.pensize(5)
minHand.shape('arrow')

hourHand.up()
hourHand.speed(0)
hourHand.color('black')
hourHand.pensize(10)
hourHand.shape('arrow')


def draw_face():
    facePen.goto(220,0)
    facePen.pensize(10)
    facePen.down()
    facePen.circle(220)
    facePen.up()

    facePen.setheading(0)
    facePen.goto(0,0)
    facePen.pensize(1)
    for i in range(60):
        facePen.up()
        facePen.setheading(i*6)
        facePen.goto(0,0)
        facePen.forward(200)
        facePen.down()
        if i % 5 == 0:
            facePen.backward(20)
            n = i//5
            
            facePen.up()
            facePen.backward(20) # point to write text
            facePen.setheading(180)
            facePen.forward(20) # move text to the center of the point instead of above it
            facePen.write(12 if n==0 else n, move=False, align='center',
                          font=('Arial', 20, 'bold'))
        else:
            facePen.backward(10)
        facePen.up()

    
def update_clock():
    t = time.localtime()

    draw_hand_sec(t)
    draw_hand_hour(t)
    draw_hand_min(t)
    draw_digital(t)
    turtle.update() # redraw screen
    
    turtle.ontimer(update_clock, 1000)

def draw_digital(t):
    digitalPen.goto(0, 0)
    digitalPen.clear()
    digitalPen.write('%d-%d-%d %d:%d:%s' % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec),
                     align='center', font=('Arial', 20, 'bold'))
    
def draw_hand_sec(t):
    angle = t.tm_sec*6
    secHand.clear()
    secHand.goto(0,0)
    secHand.setheading(angle)
    secHand.down()
    secHand.forward(200)
    secHand.up()
    
def draw_hand_min(t):
    angle = (t.tm_min + t.tm_sec/60) * 6
    minHand.clear()
    minHand.goto(0,0)
    minHand.setheading(angle)
    minHand.down()
    minHand.forward(180)
    minHand.up()
    
def draw_hand_hour(t):
    angle = (t.tm_hour + t.tm_min/60 + t.tm_sec/3600) * 30
    hourHand.clear()
    hourHand.goto(0,0)
    hourHand.setheading(angle)
    hourHand.down()
    hourHand.forward(170)
    hourHand.up()

def main():
    screen = turtle.Screen()
    screen.setup(width=500, height=500)
    screen.title("Clock")
    screen.bgcolor('lightblue')
    screen.tracer(False) # disable animation
    
    draw_face()
    update_clock()
    turtle.mainloop()

if __name__ == '__main__':
    main()


