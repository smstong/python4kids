import tkinter as tk
import random as rand
import tetris

class Playground(tk.Canvas, tetris.Playground):
    def __init__(self, parent):
        tk.Canvas.__init__(self, parent, bg='black')
        tetris.Playground.__init__(self)
        self.blockSize = 30
        self.config(width=self.cols*self.blockSize, height=self.rows*self.blockSize)
        self.pack()
        self.after(1000, self.on_timer)
        self.colors = ['red', 'blue', 'green', 'yellow']
        self.uiObjs = []
        self.figure = None
        self.bind('<Up>', lambda event: self.ui_rotate_fig())
        self.bind('<Down>', lambda event: self.ui_move_fig_down())
        self.bind('<Left>', lambda event: self.ui_move_fig_left())
        self.bind('<Right>', lambda event: self.ui_move_fig_right())
        self.focus_set()
        self.gameOver = False

    def new_figure(self):
        self.figure = tetris.Figure(x=self.cols//2, y=-2)
        self.figColor = self.rand_color()
        for stateBlocks in self.figure.allBlocks:
            for blk in stateBlocks:
                blk.color = self.figColor

    def rand_color(self):
        return rand.choice(self.colors)

    def on_timer(self):
        if self.gameOver:
            return

        if self.figure is None:
            self.new_figure()

        self.ui_move_fig_down()
        self.after(1000, self.on_timer)

    def ui_rotate_fig(self):
        if tetris.Playground.rotate_fig(self, self.figure):
            self.update_ui()

    def ui_move_fig_down(self):
        if tetris.Playground.move_fig_down(self, self.figure):
            self.update_ui()
        else:
            self.ui_freeze_fig()
            self.ui_delete_full_rows()
            self.new_figure()

    def ui_delete_full_rows(self):
        tetris.Playground.delete_full_rows(self)
        self.update_ui()
        self.ui_update_score()

    def ui_update_score(self):
        lblScore.config(text=f'Score: {self.score}')
    
    def ui_freeze_fig(self):
        tetris.Playground.freeze_fig(self, self.figure)
        if self.figure.y <= 0:
            self.game_over()
    
    def game_over(self):
        self.gameOver = True
        self.create_text(self.winfo_width()/2, 
                self.winfo_height()/2, 
                text="GAME OVER!", 
                fill='white',
                font=('Times', 30,'bold'))
        
    def ui_move_fig_left(self):
        tetris.Playground.move_fig_left(self, self.figure)
        self.update_ui()

    def ui_move_fig_right(self):
        tetris.Playground.move_fig_right(self, self.figure)
        self.update_ui()

    def logic_to_pixel(self, x, y):
        return (x*self.blockSize, y*self.blockSize)

    def clear_ui(self):
        for obj in self.uiObjs:
            self.delete(obj)

        self.uiObjs.clear()

    def update_ui(self):
        self.clear_ui()

        blocks = (self.blocks + self.figure.cur_blocks())
        for blk in blocks:
            x1,y1 = self.logic_to_pixel(blk.x, blk.y)
            x2,y2 = self.logic_to_pixel(blk.x+1, blk.y+1)
            uiObj = self.create_rectangle(x1,y1,x2,y2,width=0,fill=blk.color)
            self.uiObjs.append(uiObj)
        
root = tk.Tk()
root.title("Teris Demo")
pg = Playground(root)
lblScore = tk.Label(root, text="Score: 0", font=('Times', 20, 'bold'))
lblScore.pack()
tk.mainloop()
