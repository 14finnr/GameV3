import tkinter as tk
from tkinter import ttk
import files.modules.fileroutes as fileroutes
import files.modules.values as values
from files.modules.choice_room1 import choice_room1
from files.modules.choice_hallway import choice_hallway
from files.modules.choice_westhall import choice_westhall
from files.modules.choice_easthallmonster import choice_easthallmonster
from files.modules.choice_easthall import choice_easthall
from files.modules.choice_basement import choice_basement
from files.modules.death import death

#answer, textbox
def choices(a,b):

    interactions=['look','look around','examine','use','pray','play','eat','drink','open','check','say','speak','talk','listen','hit','break','punch','attack','fight','kill','hug','fuck','bang','light','go','move','walk','unlock','knock','swim','take','grab','get','west','east','north','south','e','w','s','n','l','i','instructions']
    room_choose={'Basement':choice_basement, 'Easthall':choice_easthall, 'EasthallMonster':choice_easthallmonster, 'Westhall':choice_westhall, 'HallwayRight':choice_hallway, 'HallwayLeft':choice_hallway, 'HallwayMiddle':choice_hallway, 'Room1':choice_room1}
    
    b.configure(state='normal')
    b.insert(tk.END,'\n\n'+a+'\n\n')

    if len(a.split())==1:

        action=str.lower(a)
        item=''

        values.basic_functions(b, action, item)
        room_choose[values.location](b, action, item)

    if len(a.split())==2:

        action=str.lower(a.split()[0])
        item=str.lower(a.split()[1])

        values.basic_functions(b, action, item)
        room_choose[values.location](b, action, item)

    if len(a.split())>2:

        articles=0

        for i in ('to','the','at'):

            if i in a.split():
                             
                articles+=1
                b.insert(tk.END, "I don't understand articles, such as '"+i+"'.")

        if articles==0:
            
            b.insert(tk.END, "That command was a bit too complicated. Try shortening it to one or two words.")

    if len(a.split())<=2 and action not in interactions:

        b.insert(tk.END, "I don't understand '"+action+"' as a verb.")

    if values.health<=0:

        b.insert(tk.END, "\n\n(Press Enter to continue)")

    b.see('end')
    b.configure(state='disabled')

    #return button_push or None
    
