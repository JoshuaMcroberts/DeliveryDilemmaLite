from libraries import *
from mmap import *
from game import N_game       
import time
             
def sec_office(game = N_game()):
    
    
        loop = True
        while loop:
            if(game.game_over == False):
                game.game_map.pre = game.game_map.player_enter((4,2),game.game_map.pre)
                clear_screen()
                print_tab(pr_colour("l_blue","-- SECURITY OFFICE --")+"\n")
                print_tab("An imposing array of monitors looms large over you on the right wall of the room as you enter.")
                print("\tBathing everything in a pale blue light. " ,end="")
                if(game.sec_gar == True):
                    print("Lazily seated at a " + pr_colour("l_blue","Desk") + " below the wall of screens is a ")
                    print("\tlone " + pr_colour("l_blue","Security Guard") + " snacking on a chocolate bar and looking at his phone. Directly opposite\n\t",end="")
                else:
                    print("Below the wall of screens sits a fairly unassuming " + pr_colour("l_blue","Desk")+ ".\n\tDirectly opposite ", end="")
                print("the door a " + pr_colour("l_blue","Coat Rack")+" bears few garments and along the back wall stands a bank of ")
                print_tab("four " +pr_colour("l_blue","Lockers") + ". The door behind you leads you " + pr_colour("l_blue","Back") + " the way you came.")
                
                var = san_input()
            
                # Navigation IF  
                if var  == "desk":
                    sec_desk(game)
            
                elif var == "securityguard":
                    sec_guard(game)
                    
                    
                elif var == "coatrack":
                    coat_rack(game)
                    
                    
                elif var == "lockers":
                    sec_lockers(game)
                    
                elif var == "nosec":
                    # REMOVE FROM FULL GAME
                    game.sec_gar = False
                
                else:
                    hint = "Don't lick icy lamp posts"
                    loop = game.basic_game_func(var, hint)           
            else: 
                loop = False

# Guard must leave room
def sec_desk(game = N_game()):
    
    if (game.sec_gar == False):
        loop = True
        while loop:
            clear_screen()
            print_tab(pr_colour("l_blue","-- DESK --")+"\n")
            print_tab("A closer look at the desk reveals a scattering of chocolate bar wrappers and empty drinks cans. ")
            print_tab("There is a desk mounted " + pr_colour("l_blue","monitor") + " that sit in front of a keyboard. It seems to have been recently")
            print_tab("used. A " + pr_colour("l_blue","bin") + " sits just to the right of the desk and is completely empty.  A " + pr_colour("l_blue","phone") + " sits in the ")
            print_tab("centre of the desk on the left of the monitor and keyboard.")
            var = san_input()
        
            # Navigation IF  
            if var  == "monitor":
                monitor(game)
                pause()
                
            elif var == "bin":
                print("bin_can(game)")
                pause()
                
            elif var == "phone":
                print("phone(game)")
                pause() 
            
            else:
                hint = "Don't lick icy lamp posts"
                loop = game.basic_game_func(var, hint)
    else:
        clear_screen()
        print_tab(pr_colour("l_blue","-- DESK --")+"\n")
        print_tab("As soon as you step up to the desk the Security guard sees you!\n")
        angry_guard(game)
        pause()

def angry_guard(game = N_game()):
    game.sec_gar_level += 1
    anger_level = game.sec_gar_level
    
    if(anger_level < 2):
        
        print_tab('Guard: "Hey who are you and what are you doing in here?"')
    
    elif(anger_level < 3):
        
        print_tab('Guard: "You shouldn\'t be in here get out!"')
        
    elif(anger_level < 4):
        
        print_tab('Guard: "What are you doing snooping around in here?!')
        
    elif(anger_level < 5):
        
        print_tab('Guard: "Stop coming back in here! Get out!"')
        
    elif(anger_level < 6):
        print_tab('Guard: "This is your last chance! If you come in here again I\'ll kick you out!"')
        
    else:
        game.game_over = True
        print_tab("The Security Guard escorts you off the premises, you got off easy this time, he could have called the Police!")

    
def sec_guard(game = N_game()):
    clear_screen()
    print_tab(pr_colour("l_blue","-- SECURITY GUARD --")+"\n")
    print_tab("You take a few steps toward the Security Guard and clear your throat. He jumps from his seat!\n")
    angry_guard(game)
    pause()

def coat_rack(game = N_game()):
    if (game.sec_gar == False):
        print("cr")
    else:
        clear_screen()
        print_tab(pr_colour("l_blue","-- COAT RACK --")+"\n")
        print_tab("You move over to the coat rack but your movement disturbs the guard!\n")
        angry_guard(game)
        pause()
    
def sec_lockers(game = N_game()):
    if (game.sec_gar == False):
            print("sl")
    else:
        clear_screen()
        print_tab(pr_colour("l_blue","-- LOCKERS --")+"\n")
        print_tab("When opening the locker it makes a *clunk* noise. The Guard immediately swivels round in his chair and stands. \n")
        angry_guard(game)
        pause()
    



def monitor(game = N_game()):
    loop = True
    while loop:
        clear_screen()
        print_tab(pr_colour("l_blue","-- MONITER --")+"\n")
        print_tab("A closer look at the desk reveals a scattering of chocolate bar wrappers and empty drinks cans. ")
        print_tab("There is a desk mounted " + pr_colour("l_blue","monitor") + " that sit in front of a keyboard. It seems to have been recently")
        print_tab("used. A " + pr_colour("l_blue","bin") + " sits just to the right of the desk and is completely empty. A " + pr_colour("l_blue","phone") + " sits in the ")
        print_tab("centre of the desk on the left of the monitor and keyboard.")
        var = san_input()
    
        # Navigation IF  
        if var  == "monitor":
            monitor()
            pause()
            
        elif var == "bin":
            print("bin_can(game)")
            pause()
            
        elif var == "phone":
            print("phone(game)")
            pause() 
        
        else:
            hint = "Don't lick icy lamp posts"
            loop = game.basic_game_func(var, hint)
    
def dialling():
    for i in range(2):
        ast = 0
        p_ast = ""
        p_ast = p_ast + "∗ "
        time.sleep(0.4)
        clear_screen()
        print("Phone Dialling " + p_ast)
        ast += 1
        time.sleep(0.5)
        clear_screen()
    print("Answered")  
    time.sleep(2) 
       
def phone(game = N_game()):
    loop = True
    while loop:
        clear_screen()
        print_tab(pr_colour("l_blue","-- Phone --")+"\n")
        print_tab("A closer look at the desk reveals a scattering of chocolate bar wrappers and empty drinks cans. ")
        print_tab("There is a desk mounted " + pr_colour("l_blue","monitor") + " that sit in front of a keyboard. It seems to have been recently")
        print_tab("used. A " + pr_colour("l_blue","bin") + " sits just to the right of the desk and is completely empty. A " + pr_colour("l_blue","phone") + " sits in the ")
        print_tab("centre of the desk on the left of the monitor and keyboard.")
        var = san_input()
    

if __name__ == "__main__":
    game = N_game()
    sec_office(game)

