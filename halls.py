from libraries import *
from mmap import *
from game import N_game
from security_office import *
from warehouse import *
from locker_room import *
from canteen import *

def hall_1(game = N_game()):
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((3,3),game.game_map.pre)   
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- HALL WAY (1) --")+"\n")
        print_tab("forward adminoffice back")
        print_tab("A semi-circler, tall " + pr_colour("l_blue","Reception Desk") + " is prominently placed against the back wall of the room with a ")
        print_tab("large double " + pr_colour("l_blue","Glass Door") + " to its left which leads further into the building.")
        print_tab("On the left side of the room there is another door with the name plate on it saying, " + pr_colour("l_blue","Security Office") + ". ")
        print_tab("As you look to the right of the room, you see a " + pr_colour("l_blue","Lift") + " door and a " + pr_colour("l_blue","Waiting Area") + " which is ")
        print_tab("nestled back up against the glass front windows.")
        var = san_input()
        
       
        # Navigation IF  
        if var  == "forward":
            hall_2(game)
            
        elif var == "adminoffice":
            admin_office(game)
            
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
            
def admin_office(game = N_game()):
    clear_screen()
    print_tab(pr_colour("l_blue","-- ADMIN OFFICE --") + "\n")
    print_tab("You walk over to the lift to take a closer look. There is a number pad and")
    print_tab("a card reader next to the door however above them is a seemingly freshly")
    print_tab("printed piece of paper taped to the wall saying “Out of Order”")
    pause()
       
def hall_2(game = N_game()):
    
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((2,3),game.game_map.pre)   
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- HALL WAY (2) --") + "\n")
        print_tab("left forward back")
        print_tab("It looks like a " + pr_colour("l_blue", "Card Reader") + ". You can see the hallway beyond with a few doors ")
        print_tab("leading off to either side.")
        var = san_input()
        
        
        if var == "left":
            hall_5(game)
            
        elif var == "forward":
            hall_3(game)
             
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


def hall_5(game = N_game()):
    
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((2,2),game.game_map.pre)   
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- HALL WAY (5) --") + "\n")
        print_tab("canteen lockerroom door back.")
        print_tab("It looks like a " + pr_colour("l_blue", "Card Reader") + ". You can see the hallway beyond with a few doors ")
        print_tab("leading off to either side.")
        var = san_input()
        
        
        if var == "canteen":
            # canteen(game)
            print("canteen")
            pause()
            
        elif var == "lockerroom":
            # locker_room(game)
            print("locker room")
            pause()
            
        elif var == "door":
            # warehouse(game)
            print("warehouse")
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

def hall_3(game = N_game()):
    
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((1,3),game.game_map.pre)   
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- HALL WAY (3) --") + "\n")
        print_tab("supplycart forward back.")
        print_tab("It looks like a " + pr_colour("l_blue", "Card Reader") + ". You can see the hallway beyond with a few doors ")
        print_tab("leading off to either side.")
        var = san_input()
        
        
        if var == "supplycart":
            supply_cart(game)
        
        elif var == "forward":
            hall_4(game)
             
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


    
def supply_cart(game = N_game()):
    clear_screen()
    print_tab(pr_colour("l_blue","-- CLEANING SUPPLY CART --") + "\n")
    print_tab("You walk over to the lift to take a closer look. There is a number pad and")
    print_tab("a card reader next to the door however above them is a seemingly freshly")
    print_tab("printed piece of paper taped to the wall saying “Out of Order”")
    pause()

def hall_4(game = N_game()):
    
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((0,3),game.game_map.pre)   
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- HALL WAY (4) --") + "\n")
        print_tab("stairs right back.")
        print_tab("It looks like a " + pr_colour("l_blue", "Card Reader") + ". You can see the hallway beyond with a few doors ")
        print_tab("leading off to either side.")
        var = san_input()
        
        
        if var == "stairs":
            stairs(game)
        
        elif var == "right":
            hall_6(game)
             
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

       
def hall_6(game = N_game()):
    
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((0,4),game.game_map.pre)   
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- HALL WAY (6) --") + "\n")
        print_tab("toilets fireexit back.")
        print_tab("It looks like a " + pr_colour("l_blue", "Card Reader") + ". You can see the hallway beyond with a few doors ")
        print_tab("leading off to either side.")
        var = san_input()
        
        
        if var == "toilets":
            toilets(game)
        
        elif var == "fireexit":
            fire_exit(game)
             
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
    
def toilets(game = N_game()):
    # 2nd Prioity - gaurd leave office
    clear_screen()
    print_tab(pr_colour("l_blue","-- TOILETS --") + "\n")
    print_tab("You walk over to the lift to take a closer look. There is a number pad and")
    print_tab("a card reader next to the door however above them is a seemingly freshly")
    print_tab("printed piece of paper taped to the wall saying “Out of Order”")
    pause()
    
def fire_exit(game = N_game()):
    # 2nd Prioity - gaurd leave office
    clear_screen()
    print_tab(pr_colour("l_blue","-- FIRE EXIT --") + "\n")
    print_tab("You walk over to the lift to take a closer look. There is a number pad and")
    print_tab("a card reader next to the door however above them is a seemingly freshly")
    print_tab("printed piece of paper taped to the wall saying “Out of Order”")
    pause()


if __name__ == "__main__":
    game = N_game()
    hall_1(game)

