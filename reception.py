from libraries import *
from mmap import *
from game import N_game
from security_office import *
from halls import hall_1

def recep(game = N_game()):
    loop = True
    while loop:
        if(game.game_over == False):
            if (game.sec_gar == False and game.game_map.pre == (4,2)):
                game.sec_gar = True
                clear_screen()
                print("")
                print_tab(pr_colour("l_blue","-- LEAVING THE SECURITY OFFICE --")+"\n")
                print_tab("As you exit the security office you look through the Glass door down the hallway. You see the Security Guard")
                print_tab("Just rounding the corner into the main corridor on his return journey. That was good timing, another minute")
                print_tab("and he would have caught you. Step into the centre of the reception as he enters and quickly moves past you")
                print_tab("back to the Security Office")
                s_pause()
                game.completed_spec_ob("Search the Office before the Guard Returns")
                s_pause()
                
            game.game_map.pre = game.game_map.player_enter((4,3),game.game_map.pre)   
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- RECEPTION --")+"\n")
            print_tab("The foyer of the building stretches out in a large oval with the narrow ends on the ")
            print_tab("left and right. A semi-circler, tall " + pr_colour("l_blue","Reception Desk") + " is prominently placed against ")
            print_tab("the back wall of the room with a large double " + pr_colour("l_blue","Glass Door") + " to its left which leads ")
            print_tab("further into the building. On the left side of the room there is another door with ")
            print_tab("the name plate on it saying, " + pr_colour("l_blue","Security Office") + ". As you look to the right of the room,")
            print_tab("you see a " + pr_colour("l_blue","Lift") + " door and a " + pr_colour("l_blue","Waiting Area") + " which is nestled back up against the")
            print_tab("glass front windows. ")
            # game.set_new_ob("Get to the Warehouse")
            var = san_input()
            
        
            # Navigation IF  
            if var  == "receptiondesk":
                recep_desk(game)
                
            elif var == "glassdoor":
                glass_door(game)
                
            elif var == "securityoffice":
                sec_office(game)
                
            elif var == "lift":
                lift(game)
                
            elif var == "waitingarea":
                waiting_area(game)
                
            elif var == "exit": ## REMOVE FOMR FULL GAME
                loop = False
                
            
            else:
                hint = "Search for Information you can use to get further int the building"
                game.basic_game_func(var, hint)
        else:
            loop = False

def recep_desk(game = N_game()):
    loop = True
    while loop:
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- RECEPTION DESK --") + "\n")
        print_tab("As you approach the Reception desk you see a brown haired " + pr_colour("l_blue","Receptionist") +" wearing ")
        print_tab("intelligent looking yet elegant round frame glasses. She appears to be engrossed in her ")
        print_tab("work and doesn't notice you immediately. You take the opportunity to glance over the top edge of the desk, down at the")
        print_tab("items on the desk top. There seems to be a number of post-it notes scattered around, normally ")
        print_tab("just out of view. A phone sits on the far side of the desk, where a second receptionist would more ")
        print_tab("easily be able to answer it and a " + pr_colour("l_blue","Notepad") +", with something written on it is placed within easy ")
        print_tab("reaching distance of the receptionist.")
        var = san_input()
        
        if var == "receptionist":
            receptionist(game)
            print("")
            
        elif var == "notepad":
            notepad(game)
            
        
        else:
                hint = "Don't lick icy lamp posts"
                loop = game.basic_game_func(var, hint)


def receptionist(game = N_game()):
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- RECEPTIONIST --")+"\n")
    print_tab("The receptionist is lost in her work and doesn't seem to notice you standing at the desk. ")
    
    space = "              "
    
    name_len = len(game.pc.char_name) 
    if name_len < 12:
        
        loop = 12 - name_len
        c_name = game.pc.character_name
        
        while loop != 0:
            c_name =  c_name + " "
            loop = loop -1
            
    else:
        c_name = game.pc.character_name
    
    if game.called != True:
        s_pause()
        print("\tThe receptionist looks very busy you should probably not disturb her without a good reason. ")
        s_pause()
        
    else:
        
        if game.time_changed == True:
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- CONVERSATION WITH RECEPTIONIST --")+"\n")
            print_tab(c_name +": Hi there, I'm " + game.pc.title +" Preston…")
            s_pause()
            
            print_tab(game.recep +": Ah yes, Hello " + game.pc.title +" Preston. I'm afraid to tell you that Mr Barber will be in at 14:30 ")
            print_tab(space +"and is unreachable until then. You can wait for him in his office, his PA should be")
            print_tab(space + "there.")
            s_pause()
            
            
            print_tab(c_name +": Oh that's a shame, but yes I'll do that.")
            s_pause()
             
            print_tab(game.recep +": OK, here is your Guest Pass, make sure to return that to me when you are leaving.")
            game.pc.add_inventory("Guest - ID Card")
            s_pause()

            print_tab(c_name +": Will do!")
            s_pause()
            
            print_tab(game.recep +": Do you know where the Mr Barbers office is?")
            s_pause()
            
            print_tab(c_name +": I'm sure I'll manage to find my way")
            s_pause()
             
            print_tab(game.recep +": OK, Have a good meeting.")
            s_pause()

            print_tab(c_name+": Thank you!")
            s_pause()
        
        else:
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- CONVERSATION WITH RECEPTIONIST --")+"\n")
            print_tab(c_name +": Hello there Anna, I do believe we spoken on the phone earlier.")
            s_pause()
            
            print_tab("(The receptionist looks up slightly confused…)")
            s_pause()
            
            print_tab(c_name +": I'm " + game.pc.title + " Preston. We spoke on the phone?")
            s_pause()
             
            print_tab(game.recep +": Oh Yes sorry, everything is crazy with the Christmas rush, our last deliveries are ")
            print_tab(space + "due to go out next week. Are you not a bit earlier than your appointment?")
            s_pause()
            
            print_tab(c_name +": Ah yes, unfortunately my pervious engagement was cancelled so I thought I might come   ")
            print_tab(space + "down here early to see if Mr Barber was available now.")
            s_pause()
            
            
            print_tab(game.recep +": I'm sorry to have to tell you this but Mr Barber won't be in the office until 14:30 ")
            print_tab(space + "at the earliest.")
            s_pause()
            
            print_tab(c_name +": In that case, is it alright if I wait for him in his office?")
            s_pause()
            
            
            print_tab(game.recep +": That shouldn't be a problem. His PA should be there. ")
            s_pause()

            print_tab(c_name+": Thats great, Thank you.")
            s_pause()
            
            print_tab(game.recep +": Ok, here is your Guest ID Card. Make sure to leave that in with me on your way out.")
            game.pc.add_inventory("Guest - ID Card")
            s_pause()

            print_tab(c_name+": OK I'll try not to forget.")
            s_pause()
            
            print_tab(game.recep +": I hope you don't get too bored waiting.")
            s_pause()

            print_tab(c_name+": I'm sure I'll find some way of passing the time.")
            s_pause()
            
            
def notepad(game = N_game()):
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- Notepad --") + "\n")
    print_tab("Reading the notepad upside down and slightly sideways, you see the words written: “Guest Pass for new ")
    print_tab("salesman " + game.pc.title + " Preston - Expected @14:45”. This gives you an idea! You could call reception and pretend to ")
    print_tab("be '" + game.pc.title + " Preston'. Now all you have to do is find another phone! ")
    game.set_new_ob("Find a Phone to call Reception as " + game.pc.title + " Preston")
    game.preston = True
    pause()
 
def glass_door(game = N_game()):
    loop = True
    while loop:
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- GLASS DOOR --") + "\n")
        print_tab("You approach the glass door and see next to it on the wall a small electronic pad.")
        print_tab("It looks like a " + pr_colour("l_blue", "Card Reader") + ". You can see the hallway beyond with a few doors ")
        print_tab("leading off to either side.")
        var = san_input()
        
        
        if var == "cardreader":
            card_reader(game)
            
        else:
            hint = "Don't lick icy lamp posts"
            loop = game.basic_game_func(var, hint)


def card_reader(game = N_game()):
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- CARD READER --") + "\n")
    check = game.pc.check_inventory("Guest - ID Card")
    if check:
        print_tab("You scan the ID Card and the card reader makes a short affirmative *beep*." )
        print_tab("With that the two glass panels glide apart and you pass through into the" )
        print_tab("hallway beyond.")
        pause()      
        hall_1(game)
    else:
        print_tab("You have no card to scan." )
        pause()
        
    

    
def lift(game = N_game()):
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- LIFT --") + "\n")
    print_tab("You walk over to the lift to take a closer look. There is a number pad and")
    print_tab("a card reader next to the door however above them is a seemingly freshly")
    print_tab("printed piece of paper taped to the wall saying “Out of Order - Use stairs”")
    pause()
    
def waiting_area(game = N_game()):
    # 2nd Prioity - gaurd leave office
    wait = game.wait
    loop = True
    while loop:
        if(game.game_over == False):
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- WAITING AREA --") + "\n")
            print_tab("The waiting area consists of three tan leather sofas set in a U shape, with the open")
            print_tab("end facing the main entrance. This gives each sofa a varying view, from the reception")
            print_tab("to the those entering through the main door and the final facing out the window to ")
            print_tab("the carpark area outside. There are a few magazines laid out on a short coffee table")
            print_tab("in the middle of the U shape to help pass the " + pr_colour("l_blue","Wait") + ".")
            var = san_input()
            char_name = game.pc.character_name
            if var == "wait":
                if wait < 1:
                    clear_screen()
                    print("")
                    print_tab(pr_colour("l_blue","-- WAIT " + str(wait+1) +" --") + "\n")
                    print_tab(char_name + " rests in the waiting area for half an hour. Nothing happens.")
                    wait += 1
                    pause()
                    
                elif wait < 2:
                    clear_screen()
                    print("")
                    print_tab(pr_colour("l_blue","-- WAIT " + str(wait+1) +" --") + "\n")
                    print_tab(char_name + " rests in the waiting area for half an hour. As you are about to get up the Security")
                    print_tab("Guard leaves his office, scans his card at the glass door and passes through.") 
                    print_tab("Best take your chance to check out the Security office!")
                    game.set_new_ob("Search the Office before the Guard Returns")
                    wait += 1
                    game.sec_gar = False
                    pause()
                
                elif wait < 3:
                    clear_screen()
                    print("")
                    print_tab(pr_colour("l_blue","-- WAIT " + str(wait+1) +" --") + "\n")
                    print_tab(char_name + " rests in the waiting area for half an hour. Nothing happens.")
                    wait += 1
                    pause()
                
                    # notepad option change wait < 4 to 3
                elif wait < 5:
                    clear_screen()
                    print("")
                    print_tab(pr_colour("l_blue","-- WAIT " + str(wait+1) +" --") + "\n")
                    print_tab(char_name + " rests in the waiting area for half an hour. The Receptionist gets up, scans")
                    print_tab("her pass and leaves through the glass door, only to return 5 mins later with a cup")
                    print_tab("of coffee and a small piece of fruit.")
                    wait += 1
                    pause()
                    
                elif wait < 6:
                    clear_screen()
                    print("")
                    print_tab(pr_colour("l_blue","-- WAIT " + str(wait+1) +" --") + "\n")
                    print_tab(char_name + " rests in the waiting area for half an hour. A delivery man enters the reception and drags a")
                    print_tab("sack truck across the floor which appears to have one flat wheeintelligentl. The security guard emerges from")
                    print_tab("his office and escorts the delivery man through the glass door and then back out again after another")
                    print_tab("10 minutes has passed.")
                    wait += 1
                    pause()
                    
                elif wait < 8:
                    clear_screen()
                    print("")
                    print_tab(pr_colour("l_blue","-- WAIT " + str(wait+1) +" --") + "\n")
                    print_tab(char_name + " grows tired of waiting. Another half hour passes.")
                    wait += 1
                    pause()
                    
                elif wait < 9:
                    clear_screen()
                    print("")
                    print_tab(pr_colour("l_blue","-- WAIT " + str(wait+1) +" --") + "\n")
                    print_tab(char_name + " rests in the waiting area for half an hour. Closing time approaches.")
                    wait += 1
                    pause()
                    
                else:
                    clear_screen()
                    print("")
                    print_tab(pr_colour("l_blue","-- WAIT " + str(wait+1) +" --") + "\n")
                    print_tab(char_name + " rests in the waiting area. The Security Guard emerges from his office and escorts <character>")
                    print_tab("out of the building as it is closing time. ")
                    print_tab("Game Over")
                    game.game_over = True
                    pause()
                
                game.wait = wait    

            else:
                hint = "Don't lick icy lamp posts"
                loop = game.basic_game_func(var, hint)
        else:
            loop = False
    

if __name__ == "__main__":
    game = N_game()
    game.pc.add_inventory("Guest - ID Card")
    game.pc.add_inventory("Warehouse - ID Card")
    game.pc.set_pronouns("male")
    # game.called = True
    # game.time_changed =True
    recep(game)
    # receptionist(game)

