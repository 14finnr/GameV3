import tkinter as tk
from tkinter import ttk
import files.modules.fileroutes as fileroutes
import files.modules.values as values

items_westhall=['water','stairs','wall','walls','floor','ceiling','sound','sounds','whisper','whispers','whispering','voice','voices']
sound_words=('sound','sounds','whisper','whispers','whispering','voice','voices')

#textbox, action, item
def choice_westhall(b,c,d):

    if d in items_westhall+['']:

        if c in ('check','examine'):

            if d in ('floor','ceiling'):

                b.insert(tk.END, "You "+c+" the "+d+" and find nothing of significance.")

            if d in ('wall','walls'):

                for i in ('wall','walls'):

                    items_westhall.remove(i)

                values.coin_clear()

                for i in range(1,4):

                    values.inventory.append('Coin')
                    values.inventory_lower.append('coin')

                values.inventory.append('Dagger')
                values.inventory_lower.append('dagger')
                b.insert(tk.END, fileroutes.westhall_check_wall)

            if d in sound_words:

                b.insert(tk.END, fileroutes.check_sound)

            if d=='water':

                b.insert(tk.END, "There is a cold, rapid underground stream flowing northward.")

            if d=='stairs':

                b.insert(tk.END, "The stairs are slick and covered in moss. They descend southward into the darkness.")

        if c in ('speak','talk','listen','say'):

            for i in sound_words:

                items_westhall.remove(i)

            values.question=True
            values.sound='gone'
