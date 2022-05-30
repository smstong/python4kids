import tkinter as tk
import random
import sys

# In order to align perfectlly,
# MoveX, MoveY should be DOT_SIZE step
# Apple location should be n*DOT_SIZE

DOT_SIZE=10

gameOver = False
moveX = DOT_SIZE
moveY = 0
score = 0

def on_key_pressed(event):
    global moveX, moveY
    print(event)
    key = event.keysym

    if key == "Left" and moveX <=0:
        moveX = -DOT_SIZE
        moveY = 0
    if key == "Right" and moveX >=0:
        moveX = DOT_SIZE
        moveY = 0
    if key == "Up" and moveY <=0:
        moveX = 0
        moveY = -DOT_SIZE
    if key == "Down" and moveY >=0:
        moveX = 0
        moveY = DOT_SIZE
    
def moveSnake():
    dots = canvas.find_withtag("dot")
    head = canvas.find_withtag("head")

    items = dots + head

    # move dots
    z = 0
    while z < len(items)-1:
        x1,y1 = canvas.coords(items[z])
        x2,y2 = canvas.coords(items[z+1])
        canvas.move(items[z], x2-x1, y2-y1)
        z += 1

    # move head
    canvas.move(head, moveX, moveY)
        
    
# check if the apple overlaps the snake head
def checkHitApple():
    global score
    apple = canvas.find_withtag("apple")
    head = canvas.find_withtag("head")

    x1,y1,x2,y2 = canvas.bbox(head)
    overlap = canvas.find_overlapping(x1,y1,x2,y2)    
    for obj in overlap:
        if obj == apple[0]:
            print("hit apple")
            x, y = canvas.coords(apple)
            # add a dot just behind the head
            canvas.create_image(x,y,image=imgDot, anchor=tk.NW, tag="dot")
            locateApple()
            score += 1
 
# check if snake hits wall or itself
def checkDead():
    global gameOver
    dots = canvas.find_withtag("dot")
    head = canvas.find_withtag("head")

    # hit itself
    x1,y1,x2,y2 = canvas.bbox(head)
    overlap = canvas.find_overlapping(x1,y1,x2,y2)

    for dot in dots:
        for obj in overlap:
            if obj == dot:
                print("hit itself:", canvas.coords(dot),canvas.coords(head))
                
                gameOver = True 

    # hit wall
    if x1 < 0 or  x1 > 290 or y1<0 or y1>290:
        gameOver = True
def drawScore():
    txtScore = canvas.find_withtag("score")
    canvas.itemconfigure(txtScore, text="Score: {0}".format(score))
#
def onTimer():
    print("on timer...")
    checkDead()
    drawScore()
    if gameOver == False:
        checkHitApple()
        moveSnake()
        canvas.after(100, onTimer)
    else:
        canvas.delete(tk.ALL)
        print("Game Over")
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                           text="Game over with score {0}".format(score), fill="white")
        
# draw an apple at random position        
def locateApple():
    apple = canvas.find_withtag("apple")
    if(len(apple) > 0):
        canvas.delete(apple[0])
        
    x = random.randint(0,27) * DOT_SIZE
    y = random.randint(0,27) * DOT_SIZE
    canvas.create_image(x,y, image=imgApple,anchor=tk.NW, tag="apple")
    
root = tk.Tk()
root.title("Snake")
root.bind("<Key>", on_key_pressed)
root.geometry("800x600")

canvas = tk.Canvas(background="black", width=300, height=300)
canvas.pack(expand=tk.YES, fill=tk.BOTH)

# load images
imgDot = tk.PhotoImage(file="dot.png")
imgHead = tk.PhotoImage(file="head.png")
imgApple = tk.PhotoImage(file="apple.png")

# draw snake
canvas.create_image(50,50, image=imgHead, anchor=tk.NW, tag="head")
canvas.create_image(30,50, image=imgDot, anchor=tk.NW, tag="dot")  # the last dot
canvas.create_image(40,50, image=imgDot, anchor=tk.NW, tag="dot")  # the second last dot

# draw apple
locateApple()

# draw score
canvas.create_text(30,10, text="Score: {0}".format(score),tag="score", fill="white")

# timer
canvas.after(100, onTimer)

root.mainloop()
