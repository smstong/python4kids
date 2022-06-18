import tkinter as tk
import math
import time

# tk.Frame, tk.Canvas, tk.Tk, tk.Button, tk.Label

class Clock(tk.Canvas):
    def __init__(self, parent, **options):
        tk.Canvas.__init__(self, parent, **options)
        self.configure(bg='lightblue')
        self.radius = 200
        self.secondHand = None
        self.minuteHand = None
        self.hourHand = None

        self.drawFace()
        self.drawHands()

    def drawFace(self):
        for i in range(60):
            angle = i * 6
            x1 = self.radius * math.cos(angle * math.pi / 180)
            y1 = self.radius * math.sin(angle * math.pi / 180)
            x2 = self.radius*0.9 * math.cos(angle * math.pi / 180)
            y2 = self.radius*0.9 * math.sin(angle * math.pi / 180)

            x1,y1 = x1+250, 250-y1
            x2,y2 = x2+250, 250-y2
            self.create_line(x1,y1,x2,y2)
            
    def drawSecondHand(self, showTime):
        sec = showTime.tm_sec
        angle = 90 - sec * 6
        x1, y1 = 0,0
        x2 = self.radius*0.85*math.cos(angle*math.pi/180)
        y2 = self.radius*0.85*math.sin(angle*math.pi/180)
        
        x1,y1 = x1+250, 250-y1
        x2,y2 = x2+250, 250-y2

        if self.secondHand is not None:
            self.delete(self.secondHand)
            
        self.secondHand = self.create_line(x1,y1,x2,y2,fill='red', width=2)
        
    def drawMinuteHand(self, showTime):
        sec = showTime.tm_min
        angle = 90 - sec * 6
        x1, y1 = 0,0
        x2 = self.radius*0.7*math.cos(angle*math.pi/180)
        y2 = self.radius*0.7*math.sin(angle*math.pi/180)
        
        x1,y1 = x1+250, 250-y1
        x2,y2 = x2+250, 250-y2

        if self.minuteHand is not None:
            self.delete(self.minuteHand)
            
        self.minuteHand = self.create_line(x1,y1,x2,y2,fill='yellow', width=5)
        
    def drawHourHand(self, showTime):
        sec = showTime.tm_hour
        angle = 90 - sec * 30
        x1, y1 = 0,0
        x2 = self.radius*0.6*math.cos(angle*math.pi/180)
        y2 = self.radius*0.6*math.sin(angle*math.pi/180)
        
        x1,y1 = x1+250, 250-y1
        x2,y2 = x2+250, 250-y2

        if self.hourHand is not None:
            self.delete(self.hourHand)
            
        self.hourHand = self.create_line(x1,y1,x2,y2,fill='black', width=10)
        
    def drawHands(self):
        curTime = time.localtime()
        
        self.drawSecondHand(curTime)
        self.drawMinuteHand(curTime)
        self.drawHourHand(curTime)
        
        self.after(1000, self.drawHands)

root = tk.Tk()
clk = Clock(root, width=500, height=500)
clk.pack()

root.mainloop()
