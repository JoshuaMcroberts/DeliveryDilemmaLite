from libraries import *
from game import N_game       
import time
             
def sec_office(game = N_game()):
    
    
        loop = True
        while loop:
            if(game.game_over == False):
                game.game_map.pre = game.game_map.player_enter((4,2),game.game_map.pre)
                clear_screen()
                print("")
                print_tab(pr_colour("l_blue","-- SECURITY OFFICE --")+"\n")
                print_tab("An imposing array of monitors looms large over you on the right wall of the room as you ")
                print("\tenter, bathing everything in a pale blue light. " ,end="")
                if(game.sec_gar == True):
                    print("Lazily seated at a " + pr_colour("l_blue","Desk") + " below the wall of ")
                    print("\tscreens is a lone " + pr_colour("l_blue","Security Guard") + " snacking on a chocolate bar and looking at his phone. ")
                    print("\tDirectly opposite ",end="")
                else:
                    print("Below the wall of screens sits a fairly")
                    print("\tunassuming " + pr_colour("l_blue","Desk")+ " with a collection of different objects on it. The room seems too quiet. ")
                    print("\tDirectly opposite ", end="")
                print("the door a " + pr_colour("l_blue","Coat Rack")+" bears few garments and along the back wall stands a ")
                print_tab("bank of four " +pr_colour("l_blue","Lockers") + ". The door behind you leads you " + pr_colour("l_blue","Back") + " the way you came.")
                
                var = san_input()
            
                # Navigation IF  
                if var  == "desk":
                    loop = sec_desk(game)
            
                elif var == "securityguard":
                    loop = sec_guard(game)
                    
                    
                elif var == "coatrack":
                    loop = coat_rack(game)
                    
                    
                elif var == "lockers":
                    loop = sec_lockers(game)
                    
                elif var == "nosec":
                    # REMOVE FROM FULL GAME
                    game.sec_gar = False
                
                else:
                    hint = "You might have to go outside the Security Office and WAIT for the guard to leave. "
                    loop = game.basic_game_func(var, hint)           
            else: 
                loop = False


def sec_desk(game = N_game()):
    
    if (game.sec_gar == False):
        loop = True
        while loop:
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- DESK --")+"\n")
            
            if game.full_bin == False:
                print_tab("A closer look at the desk reveals a scattering of chocolate bar wrappers and empty drinks cans. ")
            else:
                print_tab("An inspection of the desk shows a tidy construction made from the finest wood IKEA could find. ")
            
            print_tab("There is a desk mounted " + pr_colour("l_blue","Monitor") + " that sits in front of a keyboard. It seems to have been recently")
            
            if game.full_bin:
                print_tab("used. A " + pr_colour("l_blue","Bin") + " sits just to the right of the desk and is completely full. A " + pr_colour("l_blue","Phone") + " sits in the ")
            else:
                print_tab("used. A " + pr_colour("l_blue","Bin") + " sits just to the right of the desk and is completely empty. A " + pr_colour("l_blue","Phone") + " sits in the ")
            
            print_tab("centre of the desk on the left of the monitor and keyboard.")
            var = san_input()
        
            # Navigation IF  
            if var  == "monitor":
                monitor(game)

                
            elif var == "bin":
                bin_can(game)
                
            elif var == "phone":
                phone(game)
            
            else:
                hint = "Don't lick icy lamp posts"
                loop = game.basic_game_func(var, hint)
        return True
    else:
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- DESK --")+"\n")
        print_tab("As soon as you step up to the desk the Security guard sees you!\n")
        angry_guard(game)
        pause()
        return False

def bin_can(game = N_game()):
    contin = False
    first = True
    while not contin :
        if game.full_bin == False:
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- BIN --")+"\n")
            print_tab("You have a choice:")
            if first :
                s_pause()
            else:
                print("")
            print_tab("[1] Tidy the desk")
            print_tab("[2] Leave it as it is\n")
            print_tab("Pick an option.")
            var = san_input()
            first = False
            
            if var == "1" or var == "2":
                contin = True
            else:
                clear_screen()
                print("")
                print_tab("Incorrect entry. Type 1 or 2")
                pause() 
        else:
            var = "1"
            contin = True
    
    if var == "1":
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- BIN --")+"\n")
        print_tab("The desk, which was a mess, has been tidied by " + game.pc.character_name + " and now the bin is full.")
        pause()
        game.full_bin = True
    else:
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- BIN --")+"\n")
        print_tab("You do nothing with the bin and leave the desk in a mess")
        pause()

def angry_guard(game = N_game()):
    game.sec_gar_level += 1
    anger_level = game.sec_gar_level
    
    if(anger_level < 2):
        
        print_tab(pr_colour("red","Security Guard") + ': Hey who are you and what are you doing in here?')
    
    elif(anger_level < 3):
        
        print_tab(pr_colour("red","Security Guard") + ': You shouldn\'t be in here get out!')
        
    elif(anger_level < 4):
        
        print_tab(pr_colour("red","Security Guard") + ': What are you doing snooping around in here?!')
        
    elif(anger_level < 5):
        
        print_tab(pr_colour("red","Security Guard") + ': Stop coming back in here! Get out!')
        
    elif(anger_level < 6):
        print_tab(pr_colour("red","Security Guard") + ": This is your last chance! If you come in here again I'll kick you out!")
        
    else:
        game.game_over = True
        print_tab("The Security Guard escorts you off the premises, you got off easy this time, he could have ")
        print_tab("called the Police!")

    
def sec_guard(game = N_game()):
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- SECURITY GUARD --")+"\n")
    print_tab("You take a few steps toward the Security Guard and clear your throat. He jumps from his seat!\n")
    angry_guard(game)
    pause()
    return False

def coat_rack(game = N_game()):
    if (game.sec_gar == False):
        loop = True
        while loop:  
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- COAT RACK --") + "\n")
            print_tab("Looking at the coat rack you see one heavy " + pr_colour("l_blue","Winter Coat") + " hanging up on it. There is also a scarf")
            print_tab("that has been draped on a peg with a flat cap then put on top of it.")
            var = san_input()
            
            
            if var == "wintercoat":
                coat(game)

            else:
                hint = "Don't lick icy lamp posts"
                loop = game.basic_game_func(var, hint)
                
        return True 
            
    else:
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- COAT RACK --")+"\n")
        print_tab("You move over to the coat rack but your movement disturbs the guard!\n")
        angry_guard(game)
        pause()
        return False

def coat(game = N_game()):
    
    loop = True
    while loop:
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- WINTER COAT --") + "\n")
        print_tab("The coat looks like it is fairly new. It has a slight tear on one of the cuffs, no doubt caused by  ")
        print_tab("a trip and fall. It has two large exterior pockets both " + pr_colour("l_blue","Left") + " and " + pr_colour("l_blue","Right") + ".")
        var = san_input()
        
        
        if var == "left":
            left_pocket(game)
        
        elif var == "right":
            right_pocket(game)
        
        else:
            hint = "Don't lick icy lamp posts"
            loop = game.basic_game_func(var, hint)


    
def left_pocket(game = N_game()):
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- LEFT POCKET --") + "\n")
    print_tab("You feel the left pocket from the outside and note that something makes a crinkling noise. You put")
    print_tab("your hand inside and pull it out with a packet of Wine Gums held in its grasp. You think better of")
    print_tab("the unhealthy snack and stash it back where it came from. ") 
    pause()

def right_pocket(game = N_game()):
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- RIGHT POCKET --") + "\n")
    print_tab("The right pocket brings forth a number of items when shaken including, a set of car keys, a packet ")
    print_tab("of extra minty chewing gum and a used tissue. All of which are deemed not useful and swiftly returned.")
    pause()    
    
def sec_lockers(game = N_game()):
    if (game.sec_gar == False):
        loop = True
        while loop:  
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- Lockers --") + "\n")
            print_tab("You walk over to the lockers and take a cursory glance at them. The " + pr_colour("l_blue","Locker 1") + " and " + pr_colour("l_blue","Locker 4"))
            print_tab("both their doors slightly open. " + pr_colour("l_blue","Locker 2") + " and " + pr_colour("l_blue","Locker 3") + " appear to be closed and locked. There is")
            print_tab("a thin coat of dust on the lockers and an open cardboard box sits on top of them.")
            var = san_input()
            
            
            if var == "locker1":
                clear_screen()
                print("")
                print_tab(pr_colour("l_blue","-- Locker 1 --") + "\n")
                print_tab("Locker 1 has a couple of stickers stuck to its door, one of which reads 'Come visit West Orange ")
                print_tab("Pavilion Mall'. Inside the locker there are only a few discarded items, a clip-on tie, a couple ")
                print_tab("of pixie sticks and a name badge that reads 'Name: P Blart'. You move on.")
                pause()
            
            elif var == "locker2":
                clear_screen()
                print("")
                print_tab(pr_colour("l_blue","-- Locker 2 --") + "\n")
                print_tab("As assumed Locker 2 is locked. No point in wasting anymore time with it.")
                pause()
            
            
            elif var == "locker3":
                clear_screen()
                print("")
                print_tab(pr_colour("l_blue","-- Locker 3 --") + "\n")
                print_tab("The latch on Locker 3 turns but the mechanism seems to be jammed. You guess that this locker hasn't.")
                print_tab("been used in a long time.")
                pause()
            
            
            elif var == "locker4":
                clear_screen()
                print("")
                print_tab(pr_colour("l_blue","-- Locker 3 --") + "\n")
                print_tab("Locker 4 seems to have some old newspapers in it. The door opened easily however there appears to be.")
                print_tab("some form of mold growing in the top left corner inside the locker. You shut the door and move on.")
                pause()
                
            else:
                hint = "Not many hints to be had"
                loop = game.basic_game_func(var, hint)
        return True
    
    else:
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- LOCKERS --")+"\n")
        print_tab("When opening the locker it makes a *clunk* noise. The Guard immediately swivels round in his ")
        print_tab("chair and stands. \n")
        angry_guard(game)
        pause()
        return False
    



def monitor(game = N_game()):
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- MONITER --")+"\n")
    print_tab(game.pc.character_name + " looks at the monitor and sees a Word Document is opened with the title of")
    print_tab("'How Can Planes Fly Upside Down?'. There doesn't seem to have been much progress made.")
    print_tab("A couple of tabs in the browser show some signs of the pursuit of the thesis however ")
    print_tab("the user seems to have been distracted by cat videos on YouTube. Not much of value here.")
    pause()
    
def dialling():
    for i in range(2):
        ast = 0 
        p_ast = ""
        sys.stdout.write("\033[K")
        while ast < 6:
           
            p_ast = p_ast + "∗ "
            print("\tPhone Dialling " + p_ast , end="\r")
            time.sleep(0.4)
            ast += 1
    time.sleep(0.5)
       
def phone(game = N_game()):
    
    space = "              "
    gap = ""
    name_len = len(game.pc.char_name) 
    # print_tab(str(name_len))
    # s_pause()
    if name_len < 12:
        
        loop = 12 - name_len
        c_name = game.pc.character_name
        
        while loop != 0:
            gap = gap + " "
            loop = loop -1
        
            
    else:
        c_name = game.pc.character_name
    
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- PHONE --")+"\n")
    print_tab("You pick up the phone and dial the number for reception.")
    pause()
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- PHONE CONVERSATION WITH RECEPTION --")+"\n")
    dialling()
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- PHONE CONVERSATION WITH RECEPTION --")+"\n")
    print_tab(game.recep +": Hello, " + game.courier + " West Devonshire distribution centre, Anna speaking,")
    print_tab(space + "How can I help you?")
    if game.preston != True:
        s_pause()
        print("\tYou quickly realise you have not thought of a reason for your call. You quickly hang up the phone.")
        s_pause()
        print_tab("*Call Disconnects*")
        s_pause()
    
    elif game.preston == True:
        con_1 = False
        contin = False
        first = True
        game.called = True
        while not contin :
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- PHONE CONVERSATION WITH RECEPTION --")+"\n")
            print_tab(game.recep +": Hello, " + game.courier + " West Devonshire distribution centre, Anna speaking, ")
            print_tab(space + "How can I help you?")
            if first :
                s_pause()
            else:
                print("")
            print_tab("[1] Ask after a made-up person")
            print_tab("[2] Impersonate " + game.pc.title + " Preston\n")
            print_tab("Pick an option.")
            var = san_input()
            first = False
            
            if var == "1" or var == "2":
                contin = True
            else:
                clear_screen()
                print("")
                print_tab("Incorrect entry. Type 1 or 2")
                pause() 
        

                
        if var == "1":
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- PHONE CONVERSATION WITH RECEPTION --")+"\n")
            print_tab(c_name + gap + ": Hello Anna, I was wondering if you could help me with a quick query? ")
            print_tab(space + "I'm wondering  if Joe Smyth is in the office today? ")
            s_pause()
            
            print_tab(game.recep +": I'm not sure I know him, I can check for you if you would like?")
            s_pause()
            
            print_tab(c_name + gap + ": That's alright, I'll see if I can get him directly on his office phone.")
            s_pause()
            
            first = True
            var = "0"
            while var != "2":
                clear_screen()
                print("")
                print_tab(pr_colour("l_blue","-- PHONE CONVERSATION WITH RECEPTION --")+"\n")
                print_tab("(Continue the conversation...)")
                print("")
                print_tab("[2] Impersonate " + game.pc.title + " Preston\n")
                print_tab("Pick an option")
                var = san_input()
                first = False
                
                if var !="2":
                    print_tab("Incorrect entry. Type 2")
                    pause()  
            con_1 = True                  

            
        if var == "2":
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- PHONE CONVERSATION WITH RECEPTION --")+"\n")
            if con_1:
                convo = c_name + gap + ": Oh by the way,"
            else:
                convo = c_name + gap + ": Yes, I'm hoping you can."
            print_tab( convo + " My name is " + game.pc.p_name + " Preston, I'm supposed to be attending  ")
            print_tab(space + "a meeting later on…")
            s_pause()
            
            first = True
            contin = False
            while not contin:
                if not first:
                    print("") 
                    print_tab(pr_colour("l_blue","-- PHONE CONVERSATION WITH RECEPTION --")+"\n")
                print_tab(game.recep +": Ah yes, with Mr Barber, I believe the meeting it schedule for 14:45, is that")
                print_tab(space + "correct?")
                if first :
                    s_pause()
                else:
                    print("")
                print_tab("[3] Confirm the original meeting time")
                print_tab("[4] Change the meeting to before the real " + game.pc.title + " Preston shows up.\n")
                print_tab("Pick an option")
                var = san_input()
                first = False
                if var == "3" or var == "4":
                    contin= True
                else:
                    clear_screen()
                    print("")
                    print_tab("Incorrect entry. Type 3 or 4")
                    pause()
                    clear_screen() 
                    
            if var == "3":
                clear_screen()
                print("")
                print_tab(pr_colour("l_blue","-- PHONE CONVERSATION WITH RECEPTION --")+"\n")
                print_tab(c_name + gap + ": Yes that is correct. I have another engagement elsewhere beforehand.")
                s_pause()
                
                print_tab(game.recep +": Ok excellent, Is there anything else I can help you with?")
                s_pause()
                
                print_tab(c_name + gap + ": Nope, that is everything")
                s_pause()

                print_tab(game.recep +": Ok, see you later on then.")
                s_pause()
                
                print_tab(c_name + gap + ": Right, Bye")
                s_pause()
                
                print_tab("             *Call Disconnects*")
                s_pause()
            
            elif var == "4":
                clear_screen()
                print("")
                print_tab(pr_colour("l_blue","-- PHONE CONVERSATION WITH RECEPTION --")+"\n")
                print_tab(c_name + gap + ": No Actually, I was scheduled to have a meeting before the one with Mr Barber  ")
                print_tab(space + "but it has been cancelled. So, I'm planning on coming in earlier. I haven't  ")
                print_tab(space + "had a chance to speak to his PA yet.")
                s_pause()
                
                print_tab(game.recep +": That should be fine, I can double check with his PA if you want?")
                s_pause()
                
                print_tab(c_name + gap + ": Its fine, I don't mind waiting it if comes to it. ")
                s_pause()

                print_tab(game.recep +": Ok then I'll see you when you get here. Bye for now. ")
                s_pause()
                
                print_tab(c_name + gap + ": See you then, Bye")
                s_pause()
                
                print_tab("             *Call Disconnects*")
                s_pause()
                game.time_changed = True
            
        game.completed_spec_ob("Find a Phone to call Reception as " + game.pc.title + " Preston")        
        s_pause()
        
        game.set_new_ob("Talk to the Receptionist to get ID Card")        

        s_pause()

if __name__ == "__main__":
    game = N_game()
    game.pc.set_pronouns("male")
    game.preston = True
    sec_office(game)
    # phone(game)
