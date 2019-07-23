import tkinter as tk
from tkinter import ttk
import files.modules.fileroutes as fileroutes
import files.modules.room_basic as room_basic

class startpage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.configure(background='black')
        label=tk.Label(self, text="Welcome to the game. Are you ready to begin?", bg='black', fg='white', font=controller.large_font)
        label.pack(fill='x')
        button1=ttk.Button(self, text="Ready", command=lambda: controller.show_frame(room_basic.room))
        button1.pack(pady=20)
        start_instruc=tk.Label(self, text=(fileroutes.instructions), bg="black", fg="white", font=controller.smol_font)
        start_instruc.pack()
        photo=tk.PhotoImage(file='files\\images\\start_page.png')
        image_label=tk.Label(self, image=photo, bd=0)
        image_label.image=photo
        image_label.pack(expand=True)
