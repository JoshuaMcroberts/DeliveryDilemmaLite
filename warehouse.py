from libraries import *
from mmap import *
from game import N_game


def warehouse(game = N_game()):
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((2,1),game.game_map.pre)   
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- WAREHOUSE --")+"\n")
        print_tab("shelves damagedparcel loadingbay office")
        print_tab("A semi-circler, tall " + pr_colour("l_blue","Reception Desk") + " is prominently placed against the back wall of the room with a ")
        print_tab("large double " + pr_colour("l_blue","Glass Door") + " to its left which leads further into the building.")
        print_tab("On the left side of the room there is another door with the name plate on it saying, " + pr_colour("l_blue","Security Office") + ". ")
        print_tab("As you look to the right of the room, you see a " + pr_colour("l_blue","Lift") + " door and a " + pr_colour("l_blue","Waiting Area") + " which is ")
        print_tab("nestled back up against the glass front windows.")
        var = san_input()
        
       
        # Navigation IF  
        if var  == "shelves":
            shelves(game)
        
        elif var == "damagedparcels":
            damaged_parcel_area(game)
                
        elif var == "office":
            loading_bay(game)
            
        elif var == "office":
            office(game)
            
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
       
def shelves(game = N_game()):
    
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((2,0),game.game_map.pre)   
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- SHEVLES --") + "\n")
        print_tab("boxes back")
        print_tab("It looks like a " + pr_colour("l_blue", "Card Reader") + ". You can see the hallway beyond with a few doors ")
        print_tab("leading off to either side.")
        var = san_input()
        
        
        if var == "boxes":
            boxes(game)
             
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


def damaged_parcel_area(game = N_game()):
    
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((2,2),game.game_map.pre)   
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- DAMAGED PARCEL STATION --") + "\n")
        print_tab("boxes back.")
        print_tab("It looks like a " + pr_colour("l_blue", "Card Reader") + ". You can see the hallway beyond with a few doors ")
        print_tab("leading off to either side.")
        var = san_input()
        
        if var == "boxes":
            boxes(game)
            
             
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

def loading_bay(game = N_game()):
    
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((1,3),game.game_map.pre)   
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- LOADING BAY --") + "\n")
        print_tab("boxes back.")
        print_tab("It looks like a " + pr_colour("l_blue", "Card Reader") + ". You can see the hallway beyond with a few doors ")
        print_tab("leading off to either side.")
        var = san_input()
        
        
        if var == "boxes":
            boxes(game)
             
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


def office(game = N_game()):
    
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((0,3),game.game_map.pre)   
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- WAREHOUSE OFFICE --") + "\n")
        print_tab("computer worker back.")
        print_tab("It looks like a " + pr_colour("l_blue", "Card Reader") + ". You can see the hallway beyond with a few doors ")
        print_tab("leading off to either side.")
        var = san_input()
        
        
        if var == "computer":
            computer(game)
        
        elif var == "worker":
            worker(game)
            
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
    

def stairs(game = N_game()):
    # 2nd Prioity - gaurd leave office
    clear_screen()
    print_tab(pr_colour("l_blue","-- STAIR WELL --") + "\n")
    print_tab("You walk over to the lift to take a closer look. There is a number pad and")
    print_tab("a card reader next to the door however above them is a seemingly freshly")
    print_tab("printed piece of paper taped to the wall saying “Out of Order”")
    pause()

       
def computer(game = N_game()):
    
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((0,4),game.game_map.pre)   
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- COMPUTER --") + "\n")
        print_tab("search back.")
        print_tab("It looks like a " + pr_colour("l_blue", "Card Reader") + ". You can see the hallway beyond with a few doors ")
        print_tab("leading off to either side.")
        var = san_input()
        
        
        if var == "search":
            search_parcel(game)
        
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
    
def worker(game = N_game()):
    # 2nd Prioity - gaurd leave office
    clear_screen()
    print_tab(pr_colour("l_blue","-- TOILETS --") + "\n")
    print_tab("You walk over to the lift to take a closer look. There is a number pad and")
    print_tab("a card reader next to the door however above them is a seemingly freshly")
    print_tab("printed piece of paper taped to the wall saying “Out of Order”")
    pause()
    
def boxes(game = N_game()):
    
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((0,4),game.game_map.pre)   
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- BOXES --") + "\n")
        print_tab("box<NUMBER> back.")
        print_tab("It looks like a " + pr_colour("l_blue", "Card Reader") + ". You can see the hallway beyond with a few doors ")
        print_tab("leading off to either side.")
        var, num = item_input()

        if var == "box" and num > 0 and num < 31:
        
            if num < 14:
                clear_screen()
                print_tab("below 14")
                pause()
                           
            elif num < 18:
                clear_screen()
                print_tab("below 18")
                pause()
            
            elif num == 21:
                clear_screen()
                print_tab("is 21")
                pause()
                           
            elif num < 31:
                clear_screen()
                print_tab("below 31")
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
            
def search_parcel(game = N_game()):
    
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((0,4),game.game_map.pre)   
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- SEARCH FOR PARCEL --") + "\n")
        print_tab("search back.")
        print_tab("It looks like a " + pr_colour("l_blue", "Card Reader") + ". You can see the hallway beyond with a few doors ")
        print_tab("leading off to either side.")
        var = san_input()
        
        
        if var == "search":
            search_parcel(game)
        
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

if __name__ == "__main__":
    game = N_game()
    warehouse(game)

