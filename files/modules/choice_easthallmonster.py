import tkinter as tk
from tkinter import ttk
import files.modules.fileroutes as fileroutes
import files.modules.values as values

items_easthallmonster=['monster', 'fred', 'torch']

#textbox, action, item
def choice_easthallmonster(b,c,d):

    def check_monster(b):

        values.health-=2
        values.location='Easthall'
        values.monster=False
        b.insert(tk.END, fileroutes.check_monster)
        b.insert(tk.END, '\n\nYou lose two bars of health.')

    def check_torch(b):

        b.insert(tk.END, 'It is an unlit torch.')

    check_dict={'fred':check_monster, 'monster':check_monster, 'torch':check_torch}

    if d in items_easthallmonster+values.inventory_lower:

        if c in ('check','examine'):

            try:
                check_dict[d](b)
                
            except KeyError:
                
                b.insert(tk.END, "You don't have time to "+c+" things right now!")

        if c in ('use','light'):

            if d=='torch':
                
                b.insert(tk.END, "You will have to take the torch if you wish to "+c+" it.")

        if c in ('take','grab','get') and d=='torch':

            items_easthallmonster.remove('torch')
            values.torch.remove('unlit')
            values.torch.append('taken')
            values.inventory_lower.append('torch(unlit)')
            values.inventory.append('Torch(unlit)')
            b.insert(tk.END, "Taken.")

        if c in ('hit', 'punch', 'attack', 'kill', 'kick'):

            for i in ('attack','kill'):

                if c==i:

                    c='hit'
                    
            values.location='Easthall'
            values.monster=False
            values.health-=2
            b.insert(tk.END, "You "+c+" the beast right in the snout. ")
            b.insert(tk.END, fileroutes.sad_hit)
            b.insert(tk.END, "\n\nYou lose two bars of health.")

        if c=='hug' and d in ('fred','monster'):

            values.monster=False
            values.location='Easthall'
            b.insert(tk.END, fileroutes.hug_monster)
