import tkinter as tk
from tkinter import ttk
import files.modules.fileroutes as fileroutes
import files.modules.values as values
from files.modules.death import death

items_1=['bed','window','floor','wall','walls','ceiling','door','lock','pants','pocket','pockets','shirt']

def check_bed(b):

    if 'note' not in values.inventory_lower and 'box' not in values.inventory_lower:

        if 'box' not in items_1:

            items_1.append('box')

        b.insert(tk.END,(fileroutes.check_bed_text))

    else:

        b.insert(tk.END, "There is nothing left under the bed.")

def check_window(b):

    b.insert(tk.END, fileroutes.check_window)

def check_floor(b):

    items_1.remove('floor')
    items_1.append('jewel')
    values.health-=1
    b.insert(tk.END, fileroutes.check_floor)
    b.insert(tk.END, "\n\n You lose one bar of health.")

def check_wall(b):

    b.insert(tk.END, "You run your hands along the cold wall and find nothing.")

def check_ceiling(b):

    b.insert(tk.END, "You can see nothing special about the ceiling.")

def check_door(b):

    if values.door1==[]:

        b.insert(tk.END, fileroutes.check_door)

    if values.door1!=[]:

        b.insert(tk.END, "The door opens to the north, revealing a dimly lit hallway")

def check_shirt(b):

    b.insert(tk.END, "Unlike your pants, your shirt contains nothing of value.")

def check_box(b):

    b.insert(tk.END, "You need to take the box if you wish to examine it.")

def check_jewel(b):

    b.insert(tk.END, "You need to take the jewel if you wish to examine it.")

def check_pants(b):

    for i in ('pants','pocket','pockets'):

        items_1.remove(i)

    for i in ('Key','Lighter','Paperclip'):

        values.inventory.append(i)
        values.inventory_lower.append(str.lower(i))

    b.insert(tk.END, fileroutes.check_pants_text)

check_dict={'ceiling':check_ceiling, 'jewel':check_jewel, 'box':check_box, 'bed':check_bed, 'window':check_window, 'floor':check_floor, 'wall':check_wall, 'walls':check_wall, 'door':check_door, 'shirt':check_shirt, 'pants':check_pants, 'pocket':check_pants, 'pockets':check_pants}

def open_door(b):
    
    values.inventory_lower.remove('paperclip')
    values.inventory.remove('Paperclip')
    values.door1.append('open')
    b.insert(tk.END, fileroutes.open_door1)
    
#textbox, action, item
def choice_room1(b,c,d):

    if d in items_1+['paperclip']:

        if c in ('check','examine'):

            check_dict[d](b)

        if c in ('hit','punch','kick','break','destroy'):

            if c in ('break','destroy'):

                c='hit'
            
            values.health-=1
            b.insert(tk.END, "You "+c+" the "+d+" and hurt yourself. You lose one bar of health.")
            
        if c in ('take','grab','get'):

            if d in ('jewel','box'):

                if d=='jewel':

                    values.jewel_clear()

                values.inventory.append(str.capitalize(d))
                values.inventory_lower.append(items_1.pop(items_1.index(d)))
                b.insert(tk.END, 'Taken.')

        if d in ('door','lock'):

            if c in ('open','unlock'):

                if 'key' in values.inventory_lower:

                    b.insert(tk.END, "The key doesn't fit the door's lock.")

                else:

                    b.insert(tk.END, "The door is locked and you have no key.")

            if c=='pick':

                if 'paperclip' not in values.inventory_lower:

                    b.insert(tk.END, "You have nothing with which to pick the lock.")

                if 'paperclip' in values.inventory_lower:

                    open_door(b)

        if c=='use' and d=='paperclip':

            if 'paperclip' in values.inventory_lower:

                open_door(b)
