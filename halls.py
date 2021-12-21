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
        print_tab("The walls of this hallway are decorated with commemorative plaques with the names of the employ")
        print_tab("of the year engraved on them. There is a door on the right with the words " + pr_colour("l_blue","Administration Office"))
        print_tab("on it. The corridor also continues " + pr_colour("l_blue","forward") +".")
        var = san_input()
        
       
        # Navigation IF  
        if var  == "forward":
            hall_2(game)
            
        elif var == "adminoffice":
            admin_office(game)
            
        elif var == "back":
            loop = False                # Back value
            
        elif var == game.pc.character_name:
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
    print_tab("You try the Admin Office door and it is locked.")
    pause()
       
def hall_2(game = N_game()):
    
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((2,3),game.game_map.pre)   
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- HALL WAY (2) --") + "\n")
        print_tab("left forward back")
        print_tab("The hallway continues on until another corridor branches off from it to the " + pr_colour("l_blue", "left") + ".  The corridor also ")
        print_tab("continues " + pr_colour("l_blue", "forward") + " with pictures on the wall, of the different logos " + game.courier + " had used in the past.")
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
        
        print_tab(pr_colour("l_blue","-- HALL WAY (5) --") + "\n")
        print_tab("canteen lockerroom door back.")
        print_tab("The corridor ends with 3 doors, the one directly ahead has nothing on it however above it on the ")
        print_tab("brick work, in spray painted stencil font, is the word " + pr_colour("l_blue","Warehouse") + ". The Door to the left has a metal ")
        print_tab("plate screwed to it with the words " + pr_colour("l_blue","Locker Room") + " etched into it. The door on the right has on it a ")
        print_tab("plate that matches the opposing Locker Room door with the one change that it displays the word ")
        print_tab(pr_colour("l_blue","Canteen") + " on it.")
        var = san_input()
        
        if var == "canteen":
            canteen(game)
            
        elif var == "lockerroom":
            locker_room(game)
            
        elif var == "door":
            warehouse(game)
             
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
    # Not Complete
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
    # Not Complete
    clear_screen()
    print_tab(pr_colour("l_blue","-- CLEANING SUPPLY CART --") + "\n")
    print_tab("You walk over to the lift to take a closer look. There is a number pad and")
    print_tab("a card reader next to the door however above them is a seemingly freshly")
    print_tab("printed piece of paper taped to the wall saying “Out of Order”")
    pause()

def hall_4(game = N_game()):
    # Not Complete
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
    # Not Complete
    clear_screen()
    print_tab(pr_colour("l_blue","-- STAIR WELL --") + "\n")
    print_tab("You walk over to the lift to take a closer look. There is a number pad and")
    print_tab("a card reader next to the door however above them is a seemingly freshly")
    print_tab("printed piece of paper taped to the wall saying “Out of Order”")
    pause()

       
def hall_6(game = N_game()):
    # Not Complete
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
    # Not Complete
    clear_screen()
    print_tab(pr_colour("l_blue","-- TOILETS --") + "\n")
    print_tab("You walk over to the lift to take a closer look. There is a number pad and")
    print_tab("a card reader next to the door however above them is a seemingly freshly")
    print_tab("printed piece of paper taped to the wall saying “Out of Order”")
    pause()
    
def fire_exit(game = N_game()):
    # Not Complete
    clear_screen()
    print_tab(pr_colour("l_blue","-- FIRE EXIT --") + "\n")
    print_tab("You walk over to the lift to take a closer look. There is a number pad and")
    print_tab("a card reader next to the door however above them is a seemingly freshly")
    print_tab("printed piece of paper taped to the wall saying “Out of Order”")
    pause()


if __name__ == "__main__":
    game = N_game()
    hall_1(game)

