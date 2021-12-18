from libraries import *
from mmap import *
from game import N_game       
             
def sec_office(game = N_game()):
    
    
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((4,2),game.game_map.pre)
        clear_screen()
        print_tab(pr_colour("l_blue","-- SECURITY OFFICE --")+"\n")
        print_tab("An imposing array of monitors looms large over you on the right wall of the room as you enter.")
        print_tab("Bathing everything in a pale blue light. Lazily seated at a " + pr_colour("l_blue","Desk") + " below the wall of screens is a")
        print_tab("lone " + pr_colour("l_blue","Security Guard") + " snacking on a chocolate bar and looking at his phone. Directly opposite ")
        print_tab("the door a " + pr_colour("l_blue","Coat Rack")+" bears few garments and along the back wall stands a bank of four" +pr_colour("l_blue","Lockers") + ".")
        print_tab("The door behind you leads you " + pr_colour("l_blue","Back") + " the way you came.")
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
                        
        elif var == "back":
            loop = False
            
        elif var == "map":
            clear_screen()
            game.game_map.print_map()
            pause()
        
        else:
            print_tab("Incorrect entry try again")
            pause()             


# Guard must leave room
def sec_desk(game = N_game()):
    game.game_map.pre = game.game_map.player_enter((4,2),game.game_map.pre)
    
    loop = True
    while loop:
        clear_screen()
        print_tab(pr_colour("l_blue","-- DESK --")+"\n")
        
        var = san_input()
       
        # # Navigation IF  
        # if var  == "desk":
        #     sec_desk(game)
       
        # elif var == "securityguard":
        #     sec_guard(game)
            
        # elif var == "coatrack":
        #     coat_rack(game)
            
        # elif var == "lockers":
        #     sec_lockers(game)
                        
        # elif var == "back":
        #     loop = False
            
        # elif var == "map":
        #     clear_screen()
        #     game.game_map.print_map()
        #     pause()
        
        # else:
        #     print_tab("Incorrect entry try again")
        #     pause()  
    
def sec_guard(game = N_game()):
    print("sg")

def coat_rack(game = N_game()):
    print("cr")
    
def sec_lockers(game = N_game()):
    print("sl")
    



# def sec_desk():
#     print("")
    
# def sec_desk():
#     print("")
    

if __name__ == "__main__":
    sec_office()

