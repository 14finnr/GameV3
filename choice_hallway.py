import tkinter as tk
from tkinter import ttk
import files.modules.fileroutes as fileroutes
import files.modules.values as values

#textbox, action, item
def choice_hallway(b,c,d):

    items_hallway=['wall','walls','floor','ceiling']

    if d in items_hallway:

        if c in ('check','examine'):

            b.insert(tk.END, "You "+c+" the "+d+" and find nothing of significance.")

        if c in ('hit','punch','kick'):

            values.health-=1
            b.insert(tk.END, "You "+c+" the "+d+" and hurt yourself. You lose one bar of health.")



