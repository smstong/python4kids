import turtle
###############################################################################
# Notes:
# - turtle.TurtleScreen is actually a wrapper of tkinter.Canvas.
# 
###############################################################################

winWidth=800                # root window width
winHeight=600               # root window height
cvWidth = winWidth - 40     # canvas (screen) width
cvHeight = winHeight - 40   # canvas (screen) height

ptLeftTop = (-cvWidth/2, cvHeight/2) # Left top of canvas
ptLeftBottom = (-cvWidth/2, -cvHeight/2)
ptRightTop = (cvWidth/2, cvHeight/2)
ptRightBottom = (cvWidth/2, -cvHeight/2)

# Screen() is a function which returns a singleton object of class _Screen->TurleScreen->TurtleScreenBase
# which represent a tkinter Canvas contained by a root window
screen = turtle.Screen()

# set the root window size and pos
screen.setup(width=winWidth, height=winHeight, startx=None, starty=None)

# get canvas width/height
screen.screensize(cvWidth, cvHeight)
sw,sh = screen.screensize()
print(f'width: {sw}, height: {sh}')

# set canvas' background, color or picture
screen.bgcolor('yellow')
# screen.bgpic('xxx.gif')

# create a Turtle/Pen
pen1 = turtle.Turtle(shape="turtle")
pen2 = turtle.Turtle(shape="turtle")

# change pens' color
pen1.color('red')
pen2.color('green')

# move turtles
pen1.goto(ptLeftTop)
pen2.goto(ptRightBottom)

# draw a circle
pen1.circle(20)

# fill a circle
pen2.begin_fill()
pen2.circle(10)
pen2.end_fill()

# start the tkinter infinite loop
screen.mainloop()

