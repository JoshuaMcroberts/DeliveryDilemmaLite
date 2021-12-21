from libraries import *
from mmap import *
from game import N_game

def canteen(game = N_game()):
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((1,2),game.game_map.pre)   
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- CANTEEN --")+"\n")
        print_tab("The Canteen is a small room with a " + pr_colour("l_blue","Bench") + " that starts against the right-hand wall and wraps around ")
        print_tab("the edge of the room to the back wall. A " + pr_colour("l_blue","Fridge") + " stands up-right against the back wall, pushed into ")
        print_tab("the left corner of the room. A " + pr_colour("l_blue","Coat Rack") + " seems to have been haphazardly attached to the wall on ")
        print_tab("the left of the door as you enter the room. Two workers sit in the at one of the two tables in the ")
        print_tab("room staring at their phones. ")
        var = san_input()
        
       
        # Navigation IF  
        if var  == "worker1":
            worker_1(game)
            
        elif var == "worker2":
            worker_2(game)
        
        elif var == "fridge":
            fridge(game)
            
        elif var == "bench":
            bench(game)
            
        elif var == "coatrack":
            coat_rack_canteen(game)
        
        elif var == "back":
            loop = False                # Back value
            
        elif var == "<playername>":
            print("inventory")
            # placeholder function
            
        elif var == "map":
            clear_screen()
            game.game_map.print_map()
            pause()
            
        elif var == "hint":
            clear_screen()
            # custom help text for room
        
        else:
            print("")
            print_tab("Incorrect entry try again")
            pause()
            

def worker_1(game = N_game()):
    loop = True
    while loop:
        
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- Worker 1 --")+"\n")
        print_tab("worker1 worker2 fridge coatrack bench ")
        print_tab("")
        print_tab("")
        var = san_input()
        
       
        # Navigation IF  
        if var  == "talk":
            print("Convo Tree")
            pause()
        
        elif var == "back":
            loop = False                # Back value
            
        elif var == "<playername>":
            print("inventory")
            # placeholder function
            
        elif var == "map":
            clear_screen()
            game.game_map.print_map()
            pause()
            
        elif var == "hint":
            clear_screen()
            # custom help text for room
        
        else:
            print("")
            print_tab("Incorrect entry try again")
            pause()

def worker_2(game = N_game()):
    clear_screen()
    print_tab("Worker 2")
    pause()

def fridge(game = N_game()):
    loop = True
    while loop:
        
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- FRIDGE --")+"\n")
        print_tab("egg lunchbox back ")
        print_tab("")
        print_tab("")
        var = san_input()
        
       
        # Navigation IF  
        if var  == "egg":
            egg(game)
            
        elif var == "lunchbox":
            lunch_box(game)

        elif var == "back":
            loop = False                # Back value
            
        elif var == "<playername>":
            print("inventory")
            # placeholder function
            
        elif var == "map":
            clear_screen()
            game.game_map.print_map()
            pause()
            
        elif var == "hint":
            clear_screen()
            # custom help text for room
        
        else:
            print("")
            print_tab("Incorrect entry try again")
            pause()
            



def egg(game = N_game()):
    clear_screen()
    # need to be able to take
    print_tab(pr_colour("l_blue","-- EGG --") + "\n")
    print_tab("")
    pause()

def lunch_box(game = N_game()):
    clear_screen()
    print_tab(pr_colour("l_blue","-- LUNCH BOX --") + "\n")
    print_tab("")
    pause()


def bench(game = N_game()):
    
    loop = True
    while loop:
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- Bench --") + "\n")
        print_tab("microwave toaster back")
        print_tab("")
        print_tab("")
        var = san_input()
        
        
        if var == "microwave":
            microwave(game)
            
        elif var == "toaster":
            toaster(game)
             
        elif var == "back":
            loop = False
            # loop break value
        
        elif var == "<playername>":
            print("inventory")
        
        elif var == "map":
            clear_screen()
            game.game_map.print_map()
            pause()
        
        elif var == "hint":
            clear_screen()
            # custom help text for room
        
        else:
            print("")
            print_tab("Incorrect entry try again")
            pause()

def toaster(game = N_game()):
    clear_screen()
    print_tab(pr_colour("l_blue","-- TOASTER --") + "\n")
    print_tab("You walk over to the lift to take a closer look. There is a number pad and")
    print_tab("a card reader next to the door however above them is a seemingly freshly")
    print_tab("printed piece of paper taped to the wall saying “Out of Order”")
    pause()

def microwave(game = N_game()):
    
    loop = True
    while loop:  
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- MICROWAVE --") + "\n")
        print_tab("heat back")
        print_tab("It looks like a " + pr_colour("l_blue", "Card Reader") + ". You can see the hallway beyond with a few doors ")
        print_tab("leading off to either side.")
        var = san_input()
        
        
        if var == "heat":
            # coat(game)
            print_tab("heat")
            pause()
            
             
        elif var == "back":
            loop = False
            # loop break value
        
        elif var == "<playername>":
            print("inventory")
        
        elif var == "map":
            clear_screen()
            game.game_map.print_map()
            pause()
        
        elif var == "hint":
            clear_screen()
            # custom help text for room
        
        else:
            print("")
            print_tab("Incorrect entry try again")
            pause()



def coat_rack_canteen(game = N_game()):
    
    loop = True
    while loop:  
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- COAT RACK --") + "\n")
        print_tab("A brief glace at the coat rack informs you that there are two items of clothing hanging there. The ")
        print_tab("first of which being an old tattered high-vis vest and the second of which being a work " + pr_colour("l_blue","Coat") + ".")
        var = san_input()
        
        
        if var == "coat":
            coat(game)
            
        elif var == "back":
            loop = False
            # loop break value
        
        elif var == "<playername>":
            print("inventory")
        
        elif var == "map":
            clear_screen()
            game.game_map.print_map()
            pause()
        
        elif var == "hint":
            clear_screen()
            # custom help text for room
        
        else:
            print("")
            print_tab("Incorrect entry try again")
            pause()

def coat(game = N_game()):
    
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((1,3),game.game_map.pre)   
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- Coat --") + "\n")
        print_tab("The coat looks like it has been in use for some time. It has high-vis strips strategically sown onto it. It ")
        print_tab("seems to be a straight-forward design with a " + pr_colour("l_blue","Left Pocket") + " and " + pr_colour("l_blue","Right Pocket") + " the only two places ")
        var = san_input()
        
        
        if var == "leftpocket":
            left_pocket(game)
        
        elif var == "rightpocket":
            right_pocket(game)
             
        elif var == "back":
            loop = False
            # loop break value
        
        elif var == "<playername>":
            print("inventory")
        
        elif var == "map":
            clear_screen()
            game.game_map.print_map()
            pause()
        
        elif var == "hint":
            clear_screen()
            # custom help text for room
        
        else:
            print("")
            print_tab("Incorrect entry try again")
            pause()


    
def left_pocket(game = N_game()):
    clear_screen()
    print_tab(pr_colour("l_blue","-- LEFT POCKET --") + "\n")
    print_tab("When you slip your hand into the left pocket of the coat it immediately comes into contact with ")
    print_tab("something cold and metallic. You withdraw your hand to find clutched in it a locker key with the ")
    print_tab("number 21 written on a tag attached to it. ") 
    game.pc.add_inventory("Locker 21 - Key")
    pause()

def right_pocket(game = N_game()):
    clear_screen()
    print_tab(pr_colour("l_blue","-- RIGHT POCKET --") + "\n")
    print_tab("You put your hand quickly into the right pocket and bring it out to find it contains only a sticky old ")
    print_tab("boiled sweet and some pocket lint which has now become stuck to your fingers.")
    pause()

if __name__ == "__main__":
    game = N_game()
    canteen(game)

