import tkinter as tk
from tkinter import ttk
import files.modules.fileroutes as fileroutes

class death(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.configure(background='black')
        photo=tk.PhotoImage(file=fileroutes.death_image)
        
        label=tk.Label(self, bg='black', fg='white', text='The Void', font=controller.large_font)
        image_label=tk.Label(self, bg='black', bd=0, image=photo)
        image_label.image=photo
        epitaph=tk.Label(self, bg='black', fg='white', bd=0)
        blurb=tk.Label(self, bg='black', fg='white', font=controller.med_font, text="After your many trials, you finally succumb to your wounds. Your adventure is over.")

        label.pack(side='top', fill='x')        
        image_label.pack()
        epitaph.pack()
        blurb.pack(fill='both')
