#CURRENT: work on hall choice
import tkinter as tk
from tkinter import ttk
from files.modules.start import startpage
from files.modules.room_basic import room, question
from files.modules.death import death

#add end page(s) to the list of possible Fs when you make them

class window(tk.Tk):

    large_font=("Verdana", 12)
    med_font=("Verdana", 10)
    smol_font=("Verdana", 8)
    
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default='files\\images\\icon.ico')
        tk.Tk.wm_title(self, 'Dungeon-Crawler #80079')
        self.state('zoomed')
        container=tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames={}

        for F in (startpage, room, death, question):

            frame=F(container,self)
            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(startpage)

    def show_frame(self, cont):

        frame=self.frames[cont]
        frame.tkraise()

game=window()
game.mainloop()
