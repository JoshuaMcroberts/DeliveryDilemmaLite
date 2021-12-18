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
        print_tab("worker1 worker2 fridge coatrack bench ")
        print_tab("A semi-circler, tall " + pr_colour("l_blue","Reception Desk") + " is prominently placed against the back wall of the room with a ")
        print_tab("large double " + pr_colour("l_blue","Glass Door") + " to its left which leads further into the building.")
        print_tab("On the left side of the room there is another door with the name plate on it saying, " + pr_colour("l_blue","Security Office") + ". ")
        print_tab("As you look to the right of the room, you see a " + pr_colour("l_blue","Lift") + " door and a " + pr_colour("l_blue","Waiting Area") + " which is ")
        print_tab("nestled back up against the glass front windows.")
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
        print_tab("A semi-circler, tall " + pr_colour("l_blue","Reception Desk") + " is prominently placed against the back wall of the room with a ")
        print_tab("large double " + pr_colour("l_blue","Glass Door") + " to its left which leads further into the building.")
        print_tab("On the left side of the room there is another door with the name plate on it saying, " + pr_colour("l_blue","Security Office") + ". ")
        print_tab("As you look to the right of the room, you see a " + pr_colour("l_blue","Lift") + " door and a " + pr_colour("l_blue","Waiting Area") + " which is ")
        print_tab("nestled back up against the glass front windows.")
        var = san_input()
        
       
        # Navigation IF  
        if var  == "talk":
            print("Convo Tree")
            pause()
            
        # elif var == "worker2":
        #     worker_2(game)
        
        # elif var == "fridge":
        #     fridge(game)
            
        # elif var == "bench":
        #     bench(game)
            
        # elif var == "coatrack":
        #     coat_rack(game)
        
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
        print_tab("A semi-circler, tall " + pr_colour("l_blue","Reception Desk") + " is prominently placed against the back wall of the room with a ")
        print_tab("large double " + pr_colour("l_blue","Glass Door") + " to its left which leads further into the building.")
        print_tab("On the left side of the room there is another door with the name plate on it saying, " + pr_colour("l_blue","Security Office") + ". ")
        print_tab("As you look to the right of the room, you see a " + pr_colour("l_blue","Lift") + " door and a " + pr_colour("l_blue","Waiting Area") + " which is ")
        print_tab("nestled back up against the glass front windows.")
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
    print_tab("You walk over to the lift to take a closer look. There is a number pad and")
    print_tab("a card reader next to the door however above them is a seemingly freshly")
    print_tab("printed piece of paper taped to the wall saying “Out of Order”")
    pause()

def lunch_box(game = N_game()):
    clear_screen()
    print_tab(pr_colour("l_blue","-- LUNCH BOX --") + "\n")
    print_tab("You walk over to the lift to take a closer look. There is a number pad and")
    print_tab("a card reader next to the door however above them is a seemingly freshly")
    print_tab("printed piece of paper taped to the wall saying “Out of Order”")
    pause()


def bench(game = N_game()):
    
    loop = True
    while loop:
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- Bench --") + "\n")
        print_tab("microwave toaster back")
        print_tab("It looks like a " + pr_colour("l_blue", "Card Reader") + ". You can see the hallway beyond with a few doors ")
        print_tab("leading off to either side.")
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
        print_tab("coat back")
        print_tab("It looks like a " + pr_colour("l_blue", "Card Reader") + ". You can see the hallway beyond with a few doors ")
        print_tab("leading off to either side.")
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
        print_tab("leftpocket rightpocket")
        print_tab("It looks like a " + pr_colour("l_blue", "Card Reader") + ". You can see the hallway beyond with a few doors ")
        print_tab("leading off to either side.")
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
    print_tab("You walk over to the lift to take a closer look. There is a number pad and")
    print_tab("a card reader next to the door however above them is a seemingly freshly")
    print_tab("printed piece of paper taped to the wall saying “Out of Order”")
    pause()

def right_pocket(game = N_game()):
    
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((0,3),game.game_map.pre)   
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- RIGHT POCKET --") + "\n")
        print_tab("keys tissue back")
        print_tab("It looks like a " + pr_colour("l_blue", "Card Reader") + ". You can see the hallway beyond with a few doors ")
        print_tab("leading off to either side.")
        var = san_input()
        
        
        if var == "keys":
            keys(game)
        
        elif var == "tissue":
            tissue(game)
             
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
    

def keys(game = N_game()):
    # 2nd Prioity - gaurd leave office
    clear_screen()
    print_tab(pr_colour("l_blue","-- Keys --") + "\n")
    print_tab("You walk over to the lift to take a closer look. There is a number pad and")
    print_tab("a card reader next to the door however above them is a seemingly freshly")
    print_tab("printed piece of paper taped to the wall saying “Out of Order”")
    pause()

    
def tissue(game = N_game()):
    clear_screen()
    print_tab(pr_colour("l_blue","-- TISSUE --") + "\n")
    print_tab("You walk over to the lift to take a closer look. There is a number pad and")
    print_tab("a card reader next to the door however above them is a seemingly freshly")
    print_tab("printed piece of paper taped to the wall saying “Out of Order”")
    pause()


if __name__ == "__main__":
    game = N_game()
    canteen(game)

