import tkinter as tk
from tkinter import ttk
import files.modules.values as values
import files.modules.fileroutes as fileroutes
import files.modules.choice_easthallmonster as monster

items_easthall=['door','alcove','ceiling','wall','walls','floor']

def check_door(b):

    b.insert(tk.END, "It is a sturdy wooden door that is ")

    if values.door_easthall==True:

        b.insert(tk.END, "currently closed.")

    elif values.door_easthall==False:

        b.insert(tk.END, "currently open.")

def check_torch(b):

    b.insert(tk.END, "It is an unlit torch.")

def check_alcove(b):

    if 'torch(lit)' in values.inventory_lower:

        items_easthall.remove('alcove')
        items_easthall.append('dagger')
        items_easthall.append('skeleton')
        b.insert(tk.END, fileroutes.check_alcove_torch)

    else:

        b.insert(tk.END, fileroutes.check_alcove_notorch)

def check_skeleton(b):

    items_easthall.remove('skeleton')
    items_easthall.append('jewel')
    b.insert(tk.END, fileroutes.check_skeleton)

def take_jewel():

    items_easthall.remove('jewel')
    values.jewel_clear()
    values.inventory.append('Jewel')
    values.inventory_lower.append('jewel')

def take_dagger():

    items_easthall.remove('dagger')
    values.inventory.append('Dagger')
    values.inventory_lower.append('dagger')

def take_torch():

    values.torch.remove('unlit')
    values.torch.append('taken')
    items_easthall.remove('torch')
    values.inventory.append('Torch(unlit)')
    values.inventory_lower.append('torch(unlit)')

check_dict={'skeleton':check_skeleton, 'alcove':check_alcove, 'door':check_door, 'torch':check_torch}
take_dict={'jewel':take_jewel, 'dagger':take_dagger, 'torch':take_torch}
        
def choice_easthall(b,c,d):

    if 'torch' in monster.items_easthallmonster:

        monster.items_easthallmonster.remove('torch')
        items_easthall.append('torch')

    if d in items_easthall:

        if c in ('check','examine'):

            if d in ('ceiling','wall','walls','floor'):

                b.insert(tk.END, "You "+c+" the "+d+" and find nothing of significance.")

            else:

                check_dict[d](b)

        if c in ('use','light'):

            if d=='torch':

                b.insert(tk.END, "You will have to take the torch if you wish to "+c+" it.")
        
        if c in ('take','grab','get'):

            take_dict[d]()
            b.insert(tk.END, "Taken.")
