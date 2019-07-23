import tkinter as tk
from tkinter import ttk
import collections
import files.modules.fileroutes as fileroutes
import files.modules.values as values

def room_configure(a,b,c,d,e,f,g,h,i):
   
    #label, image_label, inventory_label, health_bar, button_top,
        #button_left, button_right, button_bottom,
            #textbox
    
    for z in values.inventory_lower:

        if values.inventory.count(str.capitalize(z))>1:

            values.inventory.append(str.capitalize(z)+' x'+str(values.inventory_lower.count(z)))
            
            while values.inventory.count(str.capitalize(z))>0:

                values.inventory.remove(str.capitalize(z))
    
    health_image=tk.PhotoImage(file=values.health_bar[values.health])
    c.configure(text=values.inventory_func)
    d.configure(image=health_image)
    d.image=health_image

    def button_push(j,k,l):

        values.direction(j,k,l)
        room_configure(a,b,c,d,e,f,g,h,i)

    def room_one(a,b,c,d,e,f,g,h,i):

        if values.door1==[]:
            
            photo=tk.PhotoImage(file=fileroutes.room1_image)

        else:

            photo=tk.PhotoImage(file=fileroutes.open_door)

        a.configure(text='Small Room')
        b.configure(image=photo)
        b.image=photo
        e.configure(text='North', command=lambda: button_push(i,'n',' '))
        f.configure(text='West', command=lambda: button_push(i,'w',' '))
        g.configure(text='East', command=lambda: button_push(i,'e',' '))
        h.configure(text='South', command=lambda: button_push(i,'s',' '))

    def hallway_middle(a,b,c,d,e,f,g,h,i):

        photo=tk.PhotoImage(file=fileroutes.hall_image_middle)
        a.configure(text='Hallway')
        b.configure(image=photo)
        b.image=photo
        e.configure(text='North', command=lambda: button_push(i,'n',' '))
        f.configure(text='Look\nWest', command=lambda: button_push(i,'w',' '))
        g.configure(text='Look\nEast', command=lambda: button_push(i,'e',' '))
        h.configure(text='South', command=lambda: button_push(i,'s',' '))

    def hallway_left(a,b,c,d,e,f,g,h,i):

        photo=tk.PhotoImage(file=fileroutes.hall_image_left)
        b.configure(image=photo)
        b.image=photo
        e.configure(text='West', command=lambda: button_push(i,'w',' '))
        f.configure(text='South', command=lambda: button_push(i,'s',' '))
        g.configure(text='North', command=lambda: button_push(i,'n',' '))
        h.configure(text='Look\nEast', command=lambda: button_push(i,'e',' '))

    def hallway_right(a,b,c,d,e,f,g,h,i):

        photo=tk.PhotoImage(file=fileroutes.hall_image_right)
        b.configure(image=photo)
        b.image=photo
        e.configure(text='East', command=lambda: button_push(i,'e',' '))
        f.configure(text='North', command=lambda: button_push(i,'n',' '))
        g.configure(text='South', command=lambda: button_push(i,'s',' '))
        h.configure(text='Look\nWest', command=lambda: button_push(i,'w',' '))

    def westhall(a,b,c,d,e,f,g,h,i):

        photo=tk.PhotoImage(file=fileroutes.westhall_image)
        a.configure(text='West Hall')
        b.configure(image=photo)
        b.image=photo
        e.configure(text='West', command=lambda: button_push(i,'w',' '))
        f.configure(text='South', command=lambda: button_push(i,'s',' '))
        g.configure(text='North', command=lambda: button_push(i,'n',' '))
        h.configure(text='East', command=lambda: button_push(i,'e',' '))

    def easthallmonster(a,b,c,d,e,f,g,h,i):
        
        photo=tk.PhotoImage(file=fileroutes.easthall_monster_image)
        a.configure(text='East Hall')
        b.configure(image=photo)
        b.image=photo
        e.configure(text='North', command=lambda: button_push(i,'n',' '))
        f.configure(text='West', command=lambda: button_push(i,'w',' '))
        g.configure(text='East', command=lambda: button_push(i,'e',' '))
        h.configure(text='South', command=lambda: button_push(i,'s',' '))

    def easthall(a,b,c,d,e,f,g,h,i):

        photo_dict={'lit':fileroutes.easthall_torch_image, 'unlit':fileroutes.easthall_image, 'taken':fileroutes.easthall_image}
        photo=tk.PhotoImage(file=photo_dict[values.torch[0]])
        a.configure(text='East Hall')
        b.configure(image=photo)
        b.image=photo
        e.configure(text='North', command=lambda: button_push(i,'n',' '))
        f.configure(text='West', command=lambda: button_push(i,'w',' '))
        g.configure(text='East', command=lambda: button_push(i,'e',' '))
        h.configure(text='South', command=lambda: button_push(i,'s',' '))

    def basement(a,b,c,d,e,f,g,h,i):

        photo=tk.PhotoImage(file=fileroutes.basement_image)
        a.configure(text='Basement')
        b.configure(image=photo)
        b.image=photo
        e.configure(text='East', command=lambda: button_push(i,'e',' '))
        f.configure(text='North', command=lambda: button_push(i,'n',' '))
        g.configure(text='South', command=lambda: button_push(i,'s',' '))
        h.configure(text='West', command=lambda: button_push(i,'w',' '))

    room_list={'Basement':basement, 'Easthall':easthall, 'EasthallMonster':easthallmonster, 'Westhall':westhall, 'HallwayRight':hallway_right, 'HallwayLeft':hallway_left, 'Room1':room_one, 'HallwayMiddle':hallway_middle}
    room_list[values.location](a,b,c,d,e,f,g,h,i)

