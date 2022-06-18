import turtle
import time
import math

faceHand = turtle.Turtle(visible=False)
secHand = turtle.Turtle(visible=False)
minHand = turtle.Turtle(visible=False)
hourHand = turtle.Turtle(visible=False)

faceHand.up()
faceHand.speed(0)
faceHand.color('blue')

secHand.up()
secHand.speed(0)
secHand.color('red')
secHand.pensize(2)

minHand.up()
minHand.speed(0)
minHand.color('yellow')
minHand.pensize(5)

hourHand.up()
hourHand.speed(0)
hourHand.color('black')
hourHand.pensize(10)

def draw_face():
    for i in range(60):
        angle = i*6
        x = 200*math.cos(angle*math.pi/180)
        y = 200*math.sin(angle*math.pi/180)
        faceHand.goto(x,y)
        faceHand.setheading(angle)
        faceHand.down()
        faceHand.backward(10)
        faceHand.up()
    
def draw_hands():
    t = time.localtime()

    draw_hand_sec(t.tm_sec)
    draw_hand_hour(t.tm_hour)
    draw_hand_min(t.tm_min)
    
    turtle.ontimer(draw_hands, 1000)

def draw_hand_sec(sec):
    angle = 90 - sec * 6
    x = 200*math.cos(angle*math.pi/180)
    y = 200*math.sin(angle*math.pi/180)

    secHand.clear()
    secHand.goto(x*0.95, y*0.95)
    secHand.setheading(angle)
    secHand.down()
    secHand.goto(0,0)
    secHand.up()
    
    
def draw_hand_min(minute):
    angle = 90 - minute * 6
    x = 200*math.cos(angle*math.pi/180)
    y = 200*math.sin(angle*math.pi/180)

    minHand.clear()
    minHand.goto(x*0.9, y*0.9)
    minHand.setheading(angle)
    minHand.down()
    minHand.goto(0,0)
    minHand.up()
    
def draw_hand_hour(hour):
    angle = 90 - hour * 30
    x = 200*math.cos(angle*math.pi/180)
    y = 200*math.sin(angle*math.pi/180)

    hourHand.clear()
    hourHand.goto(x*0.8, y*0.8)
    hourHand.setheading(angle)
    hourHand.down()
    hourHand.goto(0,0)
    hourHand.up()

def main():
    screen = turtle.Screen()
    screen.title("Clock")
    screen.bgcolor('lightblue')
    draw_face()
    draw_hands()
    turtle.mainloop()

if __name__ == '__main__':
    main()


