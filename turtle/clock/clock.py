import turtle
import datetime
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
    t = datetime.datetime.today()

    draw_hand_sec(t)
    draw_hand_hour(t)
    draw_hand_min(t)
    draw_digital(t)
    turtle.update() # redraw screen
    
    turtle.ontimer(update_clock, 100)

def draw_digital(t):
    digitalPen.goto(0, 0)
    digitalPen.clear()
    digitalPen.write('%d-%d-%d %02d:%02d:%02d' % (t.year, t.month, t.day, t.hour, t.minute, t.second),
                     align='center', font=('Arial', 20, 'bold'))
    
def draw_hand_sec(t):
    angle = (t.second + t.microsecond/1000000)*6
    secHand.clear()
    secHand.goto(0,0)
    secHand.setheading(angle)
    secHand.down()
    secHand.forward(200)
    secHand.up()
    
def draw_hand_min(t):
    angle = (t.minute + t.second/60) * 6
    minHand.clear()
    minHand.goto(0,0)
    minHand.setheading(angle)
    minHand.down()
    minHand.forward(180)
    minHand.up()
    
def draw_hand_hour(t):
    angle = (t.hour + t.minute/60 + t.second/3600) * 30
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


