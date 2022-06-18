import tkinter as tk
import math
import time

# tk.Frame, tk.Canvas, tk.Tk, tk.Button, tk.Label

class Clock(tk.Canvas):
    def __init__(self, parent, **options):
        tk.Canvas.__init__(self, parent, **options)
        self.pack(expand=tk.YES, fill=tk.BOTH, padx=0, pady=0)
        
        self.configure(bg='white')
        self.radius = 0
        self.secondHand = None
        self.minuteHand = None
        self.hourHand = None
        self.tickSize = 10
        self.fontSize = 20
        self.bind('<Configure>', lambda event: self.onSize(event.width, event.height))
        
    # transform from model coords(math) to canvas page coords
    def model2page(self, x, y):
         return x+self.centerX, self.centerY-y
         
    def onSize(self, width, height):
        self.centerX = width/2
        self.centerY = height/2
        self.radius = min(width,height)/2 - 40
        self.drawFace()
        self.drawHands()

    def drawFace(self):
        self.delete('face')
        self.create_oval(self.centerX-self.radius-20, self.centerY-self.radius-20,
                         self.centerX+self.radius+20, self.centerY+self.radius+20,
                         fill='lightblue', width=20, outline='black',
                         tag='face')
        
        for i in range(60):
            angle = 90 - i * 6
            x1 = self.radius * math.cos(angle * math.pi / 180)
            y1 = self.radius * math.sin(angle * math.pi / 180)
            x2 = (self.radius-self.tickSize) * math.cos(angle * math.pi / 180)
            y2 = (self.radius-self.tickSize) * math.sin(angle * math.pi / 180)

            x1,y1 = self.model2page(x1,y1)
            x2,y2 = self.model2page(x2,y2)

            if i % 5 == 0:
                self.create_line(x1,y1,x2,y2,width=3, tag="face")
                x = (self.radius-self.fontSize-10) * math.cos(angle * math.pi / 180)
                y = (self.radius-self.fontSize-10) * math.sin(angle * math.pi / 180)
                x,y = self.model2page(x,y)
                
                self.create_text(x, y, text='%d' % (12 if i==0 else i//5),
                                 font=("Times", self.fontSize, 'bold'),
                                 anchor=tk.CENTER, tag="face")
            else:
                self.create_line(x1,y1,x2,y2,width=1, tag="face")

            
    def drawSecondHand(self, showTime):
        sec = showTime.tm_sec
        angle = 90 - sec * 6
        x1 = (self.radius)*0.1*math.cos((180+angle)*math.pi/180)
        y1 = (self.radius)*0.1*math.sin((180+angle)*math.pi/180)
        x2 = (self.radius-self.tickSize)*math.cos(angle*math.pi/180)
        y2 = (self.radius-self.tickSize)*math.sin(angle*math.pi/180)
        
        x1,y1 = self.model2page(x1,y1)
        x2,y2 = self.model2page(x2,y2)
            
        self.secondHand = self.create_line(x1,y1,x2,y2,fill='red', width=2, tag='hand')
        
    def drawMinuteHand(self, showTime):
        minute = showTime.tm_min
        angle = 90 - (minute + showTime.tm_sec/60) * 6
        x1 = (self.radius)*0.1*math.cos((180+angle)*math.pi/180)
        y1 = (self.radius)*0.1*math.sin((180+angle)*math.pi/180)
        x2 = (self.radius-self.tickSize)*0.9*math.cos(angle*math.pi/180)
        y2 = (self.radius-self.tickSize)*0.9*math.sin(angle*math.pi/180)
        
        x1,y1 = self.model2page(x1,y1)
        x2,y2 = self.model2page(x2,y2)
            
        self.minuteHand = self.create_line(x1,y1,x2,y2,fill='yellow', width=5, arrow=tk.LAST,
                                           arrowshape=(12,15,5), tag='hand')
        
    def drawHourHand(self, showTime):
        hour = showTime.tm_hour
        angle = 90 - (hour+showTime.tm_min/60+showTime.tm_sec/3600) * 30
        
        x1 = (self.radius)*0.1*math.cos((180+angle)*math.pi/180)
        y1 = (self.radius)*0.1*math.sin((180+angle)*math.pi/180)
        x2 = (self.radius-self.tickSize)*0.8*math.cos(angle*math.pi/180)
        y2 = (self.radius-self.tickSize)*0.8*math.sin(angle*math.pi/180)
        
        x1,y1 = self.model2page(x1,y1)
        x2,y2 = self.model2page(x2,y2)
            
        self.hourHand = self.create_line(x1,y1,x2,y2,fill='black', width=10, arrow=tk.LAST,
                                         arrowshape=(16,20,6),tag='hand')
    def drawScrew(self):
        self.create_oval(self.centerX-10, self.centerY-10,
                         self.centerX+10, self.centerY+10,
                         fill='black',
                         tag='hand')
        
    def drawHands(self):
        curTime = time.localtime()
        self.delete('hand')
        self.drawSecondHand(curTime)
        self.drawMinuteHand(curTime)
        self.drawHourHand(curTime)
        self.drawScrew()
        
        self.after(1000, self.drawHands)

root = tk.Tk()
clk = Clock(root, width=500, height=500)

root.mainloop()
