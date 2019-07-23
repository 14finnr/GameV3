import tkinter as tk
from tkinter import ttk
import time
import files.modules.fileroutes as fileroutes
from files.modules.room_config import room_configure
from files.modules.player_choice import choices
import files.modules.values as values
from files.modules.death import death

class room(tk.Frame):

    def __init__(self, parent, controller):

        def look_button(a):

            textbox.configure(state='normal')
            textbox.insert(tk.END, '\n\n')
            a(textbox,'l',' ')
            textbox.see('end')
            textbox.configure(state='disabled')

        def get_input(event):

            if values.health<=0:

                controller.show_frame(death)

            answer=entrybox.get()
            entrybox.delete(0, 'end')
            choices(answer, textbox)
            room_configure(label, image_label, inventory_label, health_bar, button_top, button_left, button_right, button_bottom, textbox)

            if values.question==True:

                values.question=False
                controller.show_frame(question)
            
        tk.Frame.__init__(self, parent)
        self.configure(background='black')
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        label=tk.Label(self, bg='black', fg='white', font=controller.large_font)
        
        textbox=tk.Text(self, bg="black", fg="white", bd=0, width=120, height=10, font=controller.smol_font)
        textbox.insert(tk.END, fileroutes.start_room_text)
        textbox.configure(state='disabled')
        
        scrollbar=tk.Scrollbar(self, command=textbox.yview)
        textbox['yscrollcommand']=scrollbar.set
        prompt=tk.Label(self, text='What would you like to do?: ', bg='black', fg='white')
        entrybox=tk.Entry(self, bg='black', fg='white', width=108)
        entrybox.bind('<Return>', get_input)
        
        button_top=ttk.Button(self, width=7)
        button_left=ttk.Button(self, width=7)
        button_right=ttk.Button(self, width=7)
        button_bottom=ttk.Button(self, width=7)
        button_look=ttk.Button(self, width=7, text='Look', command=lambda: look_button(values.look))
        
        image_label=tk.Label(self, bg='black', bd=0)        
        inventory_label=tk.Label(self, bg='black', fg='white', font=controller.med_font)
        health_bar=tk.Label(self, bg='black', bd=0)

        label.grid(row=0, column=1, pady=10)
        button_top.grid(row=2, column=1)
        health_bar.grid(row=2, column=1, sticky='w')
        button_left.grid(row=3, column=0, padx=20)
        image_label.grid(row=3, column=1, pady=10)
        button_right.grid(row=3, column=2, padx=20)
        button_bottom.grid(row=4, column=1, pady=10)
        button_look.grid(row=5, column=1, pady=10)
        inventory_label.grid(row=6, column=1, sticky='w')
        textbox.grid(row=7, column=1)
        scrollbar.grid(row=7, column=2, sticky='nsw')
        prompt.grid(row=8, column=1, sticky='w', pady=10)
        entrybox.grid(row=8, column=1, sticky='e')
        
        room_configure(label, image_label, inventory_label, health_bar, button_top, button_left, button_right, button_bottom, textbox)

class question(tk.Frame):

    def __init__(self, parent, controller):

        def health_func():

            for i in (yes, no):

                i.destroy()

            values.health+=1
            hw_label.configure(text=fileroutes.get_health)
            hw_label.grid(row=3, column=1, pady=50)
            cont_button.grid(row=4, column=1, pady=50)

        def wealth_func():

            for i in (yes, no):

                i.destroy()
                
            values.jewel_clear()
            values.inventory.append('Jewel')
            values.inventory_lower.append('jewel')
            hw_label.configure(text=fileroutes.get_jewel)
            hw_label.grid(row=3, column=1, pady=50)
            cont_button.grid(row=4, column=1, pady=50)

        def no_func():
            
            values.health-=2
            values.no=True
            response_label.configure(text=fileroutes.shadow_no)
            response_label.grid(row=2, column=1)
            
            for i in (yes, no):

                i.destroy()
  
            cont_button.grid(row=4, column=1, pady=50)

        def yes_func():

            response_label.configure(text=fileroutes.shadow_yes)
            response_label.grid(row=2, column=1, pady=50)
            no.configure(text='Wealth', command=lambda: wealth_func())
            yes.configure(text='Health', command=lambda: health_func())
            
        frame_dict={-2:death, -1:death, 0:death, 1:room, 2:room, 3:room, 4:room, 5:room, 6:room, 7:room}
        tk.Frame.__init__(self, parent)
        self.configure(background='black')
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        title=tk.Label(self, bg='black', fg='white', bd=0, font=controller.large_font, text='A Dark Place')
        image_label=tk.Label(self, bg='black', fg='white', bd=0)
        label=tk.Label(self, bg='black', fg='white', bd=0, font=controller.med_font, text=fileroutes.shadow_response)
        response_label=tk.Label(self, bg='black', fg='white', bd=0, font=controller.med_font)
        hw_label=tk.Label(self, bg='black', fg='white', bd=0, font=controller.med_font)
        
        no=ttk.Button(self, text='No', command=lambda: no_func())
        yes=ttk.Button(self, text='Yes', command=lambda: yes_func())
        cont_button=ttk.Button(self, text='Continue', command=lambda: controller.show_frame(frame_dict[values.health]))

        title.grid(row=0, column=1, pady=10)
        label.grid(row=1, column=1, pady=40, sticky='w')
        yes.grid(row=4, column=1, sticky='w')
        no.grid(row=4, column=1, sticky='e')
        
        
