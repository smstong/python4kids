import tkinter as tk
import random

class Snake:
    def __init__(self, headTag, dotTag, uiScore,
                 upKey, downKey, leftKey, rightKey):
        self.moveX = 10
        self.moveY = 0
        self.score = 0
        self.running = True
        self.headTag = headTag
        self.dotTag = dotTag
        self.uiScore = uiScore
        
        self.upKey = upKey
        self.downKey = downKey
        self.leftKey = leftKey
        self.rightKey = rightKey

        x = random.randint(2,27)*10
        y = random.randint(2,27)*10
        cv.create_image(x,y,image=imgHead, anchor=tk.NW, tag=self.headTag)
        cv.create_image(x-20, y, image=imgDot, anchor=tk.NW, tag=self.dotTag)
        cv.create_image(x-10, y, image=imgDot, anchor=tk.NW, tag=self.dotTag)

        self.bind_keys()

    def go_up(self):
        if self.moveY == 0:
            self.moveX = 0
            self.moveY = -10
            
    def go_down(self):
        if self.moveY == 0:
            self.moveX = 0
            self.moveY = 10

    def go_left(self):
        if self.moveX == 0:
            self.moveX = -10
            self.moveY = 0

    def go_right(self):
        if self.moveX == 0:
            self.moveX = 10
            self.moveY = 0

    def detect_border(self):
        head = cv.find_withtag(self.headTag)[0]
        x, y = cv.coords(head)
        if x<0 or x > 300 or y<0 or y>300:
            self.running = False

    def detect_apple(self):
        apple = cv.find_withtag('apple')[0]
        head = cv.find_withtag(self.headTag)[0]
        x1,y1,x2,y2 = cv.bbox(head)
        objs = cv.find_overlapping(x1,y1,x2,y2)
        if apple in objs:
            x, y = cv.coords(apple)
            cv.create_image(x,y, image=imgDot, anchor=tk.NW, tag=self.dotTag)

            cv.delete(apple)
            locate_apple()

            self.score += 1
            cv.itemconfig(self.uiScore, text="Score: " + str(self.score))
            
    def detect_hitself(self):
        head = cv.find_withtag(self.headTag)[0]
        x1,y1,x2,y2 = cv.bbox(head)
        overlap = cv.find_overlapping(x1,y1,x2,y2)
        dots = cv.find_withtag(self.dotTag)
        for dot in dots:
            if dot in overlap:
                self.running = False
                return

    def bind_keys(self):
        root.bind(self.upKey, lambda event: self.go_up())
        root.bind(self.downKey, lambda event: self.go_down())
        root.bind(self.leftKey, lambda event: self.go_left())
        root.bind(self.rightKey, lambda event: self.go_right())

    def move(self):
        head = cv.find_withtag(self.headTag)[0]
        headX, headY = cv.coords(head)
        cv.move(head, self.moveX, self.moveY)
        dots = cv.find_withtag(self.dotTag)
        for i in range(len(dots)-1):
            x, y = cv.coords(dots[i+1])
            cv.moveto(dots[i], x, y)
        cv.moveto(dots[-1], headX, headY)

    def on_timer(self):
        self.detect_border()
        self.detect_hitself()
        self.detect_apple()
        self.move()
        
######################################################################   
# draw an apple at random pos
def locate_apple():
    x = random.randint(0,27) * 10
    y = random.randint(0,27) * 10
    cv.create_image(x, y, image=imgApple, anchor=tk.NW, tag="apple")

def on_timer():
    snake1.on_timer()
    snake2.on_timer()
    if snake1.running == False and snake2.running == False:
        cv.create_text(150, 150, text="GAME OVER!", fill='yellow', font=('Times', 26, 'bold'))
        return
    root.after(200, on_timer)

root = tk.Tk()
root.geometry("300x300")

cv = tk.Canvas(root, bg='black')
cv.pack(expand=tk.YES, fill=tk.BOTH)

# prepare images
imgApple = tk.PhotoImage(file='apple.png')
imgHead = tk.PhotoImage(file='head.png')
imgDot = tk.PhotoImage(file='dot.png')

# score widget
uiScore1 = cv.create_text(0,0, text="score: 0", fill='white',
               font=('Times', 20, 'bold'), anchor=tk.NW)

uiScore2 = cv.create_text(200,0, text="score: 0", fill='white',
               font=('Times', 20, 'bold'), anchor=tk.NW)

# create two snakes
snake1 = Snake('head1', 'dot1', uiScore1, '<Up>', '<Down>', '<Left>', '<Right>')
snake2 = Snake('head2', 'dot2', uiScore2, '<w>', '<s>', '<a>', '<d>')
locate_apple()

# timer
root.after(200, on_timer)

root.mainloop()
