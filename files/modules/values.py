import tkinter as tk
from tkinter import ttk
import collections
import files.modules.fileroutes as fileroutes
from files.modules.death import death

location='Room1'
health=5
inventory_lower=[]
inventory=[]
inventory_func='Inventory:',inventory
door1=[]
sound='present'
monster='present'
question=False
no=False
monster=True
torch=['unlit']
door_easthall=True

health_bar={-2: fileroutes.health_bar_0, -1: fileroutes.health_bar_0, 0: fileroutes.health_bar_0, 1: fileroutes.health_bar_1, 2: fileroutes.health_bar_2, 3: fileroutes.health_bar_3, 4: fileroutes.health_bar_4, 5: fileroutes.health_bar_5, 6: fileroutes.health_bar_6}

def coin_clear():

    for i in inventory:

        if 'Coin x' in i:

            inventory.remove(i)

def jewel_clear():

    for i in inventory:

        if 'Jewel x' in i:

            inventory.remove(i)

#textbox, action, item
def instructions(b,c,d):

    if 'instructions' in (c,d) or 'i' in (c,d):

        b.insert(tk.END, fileroutes.instructions)

#textbox, action, item
def look(b,c,d):

    directions=['n','s','w','e','north','south','east','west']

    if len(str(c))==1 and d==' ':

        b.insert(tk.END, "look\n\n")

    if c in ('l','look') and d not in directions:

        def room1(b):

            b.insert(tk.END, fileroutes.start_look_around_text)

            if door1==[]:

                b.insert(tk.END, "The door is currently closed.")

            if door1!=[]:

                b.insert(tk.END, "The door is currently open.")

        def hallwayM(b):

            b.insert(tk.END, fileroutes.hallway)

        def hallwayL(b):

            b.insert(tk.END, fileroutes.hallwayL)

        def hallwayR(b):

            b.insert(tk.END, fileroutes.hallwayR)

        def westhall(b):

            def wsound(b):

                b.insert(tk.END, fileroutes.left_hall_look)

            def nosound(b):

                b.insert(tk.END, fileroutes.left_hall_look_nosound)

            sound_dict={'present':wsound, 'gone':nosound}
            sound_dict[sound](b)

        def easthallmonster(b):

            b.insert(tk.END, fileroutes.monster_encounter[29:])

        def easthall(b):

            if torch==['unlit']:

                b.insert(tk.END, fileroutes.empty_6_turned)

            elif torch!=['unlit']:

                b.insert(tk.END, fileroutes.empty_hall_notorch)
                
        look_dict={'Easthall':easthall, 'EasthallMonster':easthallmonster, 'Westhall':westhall, 'HallwayRight':hallwayR, 'HallwayLeft':hallwayL, 'Room1':room1, 'HallwayMiddle':hallwayM}
        look_dict[location](b)

#textbox, action, item
def direction(b,c,d):

    directions=['n','s','w','e','north','south','east','west']
    b.configure(state='normal')
    button_press=False

    if len(str(c))==1 and d==' ':

        b.insert(tk.END, '\n\n')
        button_press=True

    def north(b):

        def room_one(b):

            if door1==[]:

                b.insert(tk.END, "The closed door blocks your way.")

            else:

                global location
                location='HallwayMiddle'
                b.insert(tk.END, fileroutes.hallway)

        def hallwayM(b):

            b.insert(tk.END, "There is only a hard wall to the north.")

        def westhall(b):

            if sound=='present':

                b.insert(tk.END, "When you try to move, the whispers become more intense and seem to surround you, as if trying to tell you something.")

        def easthallmonster(b):

            b.insert(tk.END, "The monster blocks your path!")

        room={'EasthallMonster':easthallmonster, 'Westhall':westhall, 'HallwayRight':hallwayM, 'HallwayLeft':hallwayM, 'Room1':room_one, 'HallwayMiddle':hallwayM}

        if button_press==True:

            b.insert(tk.END, "north\n\n")
        
        room[location](b)
        
    def south(b):

        def room_one(b):

            b.insert(tk.END, "There is only a hard wall to the south.")

        def hallwayM(b):
            
            global location
            location='Room1'
            b.insert(tk.END, "You step back into the small room.")

        def westhall(b):

            if sound=='present':

                b.insert(tk.END, "When you try to move, the whispers become more intense and seem to surround you, as if trying to tell you something.")

            elif sound!='present':

                global location
                location='Basement'
                b.insert(tk.END, fileroutes.sewer_go)

        room={'EasthallMonster':room_one, 'Easthall':room_one, 'Westhall':westhall, 'HallwayRight':hallwayM, 'HallwayLeft':hallwayM, 'Room1':room_one, 'HallwayMiddle':hallwayM}

        if button_press==True:

            b.insert(tk.END, "south\n\n")
        
        room[location](b)

    def west(b):

        def room_one(b):

            b.insert(tk.END, "There is only a hard wall to the west.")

        def hallwayM(b):

            global location
            location='HallwayLeft'
            b.insert(tk.END, fileroutes.hallwayL)

        def hallwayL(b):

            global location
            location='Westhall'
            
            def wsound(b):

                b.insert(tk.END, fileroutes.left_hall)

            def nosound(b):

                b.insert(tk.END, fileroutes.left_hall_nosound)
                
            sound_dict={'present':wsound, 'gone':nosound}
            sound_dict[sound](b)

        def easthallmonster(b):

            b.insert(tk.END, "You can't run now. You have to act!")

        def easthall(b):

            if 'Torch(lit)' in inventory:

                inventory.remove('Torch(lit)')
                inventory_lower.remove('torch(lit)')
                torch.clear()
                torch.append('taken')
                b.insert(tk.END, "What little fuel your torch had to offer runs out.\n")

            global location
            location='HallwayMiddle'
            b.insert(tk.END, "You step back into the hallway.")

        room={'Easthall':easthall, 'EasthallMonster':easthallmonster, 'Westhall':room_one, 'HallwayLeft':hallwayL, 'HallwayRight':hallwayM, 'Room1':room_one, 'HallwayMiddle':hallwayM}

        if button_press==True:

            b.insert(tk.END, "west\n\n")
        
        room[location](b)

    def east(b):

        def room_one(b):

            b.insert(tk.END, "There is only a hard wall to the east.")

        def hallwayM(b):

            global location
            location='HallwayRight'
            b.insert(tk.END, fileroutes.hallwayR)

        def hallwayR(b):
            
            monster_dict={True:'EasthallMonster', False:'Easthall'}
            text_dict={True:fileroutes.right_hall+'\n'+fileroutes.monster_encounter, False:"You go east."}
            global location
            location=monster_dict[monster]
            b.insert(tk.END, text_dict[monster])

        def westhall(b):

            if sound=='present':

                b.insert(tk.END, "When you try to move, the whispers become more intense and seem to surround you, as if trying to tell you something.")

            if sound!='present':

                global location
                location='HallwayMiddle'
                b.insert(tk.END, fileroutes.hallway)

        def easthallmonster(b):

            global health
            global location
            location='Easthall'
            health-=1
            b.insert(tk.END, fileroutes.run_alcove)

        def easthall(b):

            global health
            global location
            location='Basement'

            if 'torch(lit)' in inventory_lower:
                
                inventory_lower.remove('torch(lit)')
                inventory.remove('Torch(lit)')
                torch.clear()
                torch.append('taken')
                b.insert(tk.END, fileroutes.go_alcove_torch)

            else:

                health-=1
                b.insert(tk.END, fileroutes.go_alcove_notorch)

            b.insert(tk.END, fileroutes.sewer_go)

        room={'Easthall':easthall, 'EasthallMonster':easthallmonster, 'Westhall':westhall, 'HallwayRight':hallwayR, 'HallwayMiddle':hallwayM, 'HallwayLeft':hallwayM, 'Room1':room_one}

        if button_press==True:

            b.insert(tk.END, "east\n\n")
        
        room[location](b)

    direction_dict={'n':north, 'north':north, 's':south, 'south':south, 'w':west, 'west':west, 'e':east, 'east':east}
    dir_check=0

    for i in (c,d):

        if i in directions:

            if dir_check==0:

                dir_check+=1
                direction_dict[i](b)

    b.see('end')
    
#textbox, action, item
def inv_check(b,c,d):

    def box_check(b):
        
        inventory.remove('Box')
        inventory.append('Note')
        inventory_lower.remove('box')
        inventory_lower.append('note')
        coin_clear()

        for i in range(1,6):

            inventory.append('Coin')
            inventory_lower.append('coin')

        #money='Coins x'+str(dollars)
        #inventory.pop(0)
        #inventory.insert(0, money)
        b.insert(tk.END, fileroutes.check_box)
        
    def jewel_check(b):

        b.insert(tk.END, "It's shiny.")

    def paperclip_check(b):

        b.insert(tk.END, "It's a normal-looking paperclip.")

    def lighter_check(b):

        b.insert(tk.END, "It's an old, beat-up bic lighter. Wait... what time period does this game take place in?")

    def key_check(b):

        b.insert(tk.END, "It's a rusty key.")

    def note_check(b):

        b.insert(tk.END, fileroutes.check_note)

    def coin_check(b):

        b.insert(tk.END, "They are old-looking gold coins.")

    def dagger_check(b):

        b.insert(tk.END, "The dagger is old and dull, but better than nothing.")

    inv_dict={'dagger':dagger_check, 'note':note_check, 'coin':coin_check, 'coins':coin_check, 'box':box_check, 'jewel':jewel_check, 'paperclip':paperclip_check, 'lighter':lighter_check, 'key':key_check}

    try:
        
        if c in ('check','examine','open','read'):

            if d in inventory_lower+['coins','key']:

                if d in inventory_lower:

                    inv_dict[d](b)

                if d=='coins':

                    if 'coin' in inventory_lower:

                        inv_dict[d](b)

    except KeyError:

        pass

#textbox, action, item
def inv_use(b,c,d):

    def use_lighter(b):

        if 'torch(unlit)' in inventory_lower:

            global monster
            global location
            global health
            inventory.remove('Torch(unlit)')
            inventory_lower.remove('torch(unlit)')
            inventory.append('Torch(lit)')
            inventory_lower.append('torch(lit)')
            torch.remove('taken')
            torch.append('lit')
            b.insert(tk.END, "You light your torch")

            if location=='EasthallMonster':
                
                location='Easthall'
                monster=False
                health-=1
                b.insert(tk.END, " and swing it in the beast's face.")
                b.insert(tk.END, fileroutes.sad_hit)
                b.insert(tk.END, '\n\nYou lose one bar of health.')

            if location=='Easthall':

                b.insert(tk.END, ". ")

            else:

                inventory.remove('Torch(lit)')
                inventory_lower.remove('torch(lit)')
                b.insert(tk.END, ", but it's old and rotten. It flares up quickly and then falls apart. ")

        if location=='Westhall':

            b.insert(tk.END, "You strike your lighter, but the darkness seems to swallow what little light it produces. It does little to help you see.")
                
        else:
            
            b.insert(tk.END, "You strike your lighter. The room is a bit brighter. ")

    def use_torch(b):

        global health
        global location
        global monster

        if location=='EasthallMonster' and 'torch(unlit)' in inventory_lower:

            health-=2
            location='Easthall'
            monster=False
            b.insert(tk.END, "You wave it in the beast's face, but it isn't very intimidating without fire. ")
            b.insert(tk.END, fileroutes.normal_hit)
            b.insert(tk.END, '\n\nYou lose two bars of health.')

        else:

            use_lighter(b)

    def use_key(b):

        if 'lockbox' in inventory_lower:

            pass
            #add lockbox function here

        else:
            
            if location in ('Room1','Easthall'):

                b.insert(tk.END, "The key doesn't fit the door's lock.")

            else:

                b.insert(tk.END, "There is nothing here to use a key on.")

    def use_coin(b):

        b.insert(tk.END, "There isn't anything to use a coin on.")

    def use_jewel(b):

        if location!='Statue':

            b.insert(tk.END, "There is nothing here to use a jewel on.")

    use_dict={'torch':use_torch, 'jewel':use_jewel, 'coin':use_coin, 'coins':use_coin, 'lighter':use_lighter, 'key':use_key}

    try:

        if c in ('use','light','drink') and d in inventory_lower+['coins','torch']:

            if d in inventory_lower:
                
                use_dict[d](b)

            if d=='coins' and 'coin' in inventory_lower:

                use_dict[d](b)

            if d=='torch':

                if c!='light':
                    
                    if 'torch(unlit)' in inventory_lower or 'torch(lit)' in inventory_lower:

                        use_dict[d](b)

                if c=='light':

                    use_lighter(b)

    except KeyError:

        pass

def basic_functions(a,b,c):

    inv_check(a,b,c)
    inv_use(a,b,c)
    look(a,b,c)
    instructions(a,b,c)
    direction(a,b,c)

            
