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
        if(game.game_over == False):
            game.game_map.pre = game.game_map.player_enter((3,3),game.game_map.pre)   
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- HALL WAY (1) --")+"\n")
            print_tab("The walls of the hallway are decorated with commemorative plaques with the names of the ")
            print_tab("employee of the year engraved on them. There is a door on the right with the words " )
            print_tab(pr_colour("l_blue","Admin Office") +" on it. The corridor also continues " + pr_colour("l_blue","Forward") +".")
            var = san_input()
            
            
            # Navigation IF  
            if var  == "forward":
                hall_2(game)
                
            elif var == "adminoffice":
                admin_office(game)
            
            else:
                hint = "Don't lick icy lamp posts"
                loop = game.basic_game_func(var, hint)
        else:
            loop = False
            
def admin_office(game = N_game()):
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- ADMIN OFFICE --") + "\n")
    print_tab("You try the Admin Office door and it is locked.")
    pause()
       
def hall_2(game = N_game()):
    
    loop = True
    while loop:
        if(game.game_over == False):
            game.game_map.pre = game.game_map.player_enter((2,3),game.game_map.pre)   
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- HALL WAY (2) --") + "\n")
            print_tab("The hallway continues on until another corridor branches off from it to the " + pr_colour("l_blue", "Left") + ". The  ")
            print_tab("corridor also continues " + pr_colour("l_blue", "Forward") + " with pictures on the wall, of the different logos " + game.courier )
            print_tab("had used in the past.")
            var = san_input()
            
            
            if var == "left":
                hall_5(game)
                
            elif var == "forward":
                hall_3(game)
            
            else:
                hint = "Don't lick icy lamp posts"
                loop = game.basic_game_func(var, hint)
        else:
            loop = False

def hall_5(game = N_game()):
    
    loop = True
    while loop:
        if(game.game_over == False):
            game.game_map.pre = game.game_map.player_enter((2,2),game.game_map.pre)   
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- HALL WAY (5) --") + "\n")
            print_tab("The corridor ends with 3 doors, the one directly ahead has nothing on it however above it on ")
            print_tab("the brick work, in spray painted stencil font, is the word " + pr_colour("l_blue","Warehouse") + ". The Door to the left ")
            print_tab("has a metal plate screwed to it with the words " + pr_colour("l_blue","Locker Room") + " etched into it. The door on the ")
            print_tab("right has on it a plate that matches the opposing Locker Room door with the one change that ")
            print_tab("it displays the word " + pr_colour("l_blue","Canteen") + " on it.")
            var = san_input()
            
            if var == "canteen":
                canteen(game)
                
            elif var == "lockerroom":
                locker_room(game)
                
            elif var == "warehouse":
                warehouse_door(game)
            
            else:
                hint = "Make a good search of the locker room"
                loop = game.basic_game_func(var, hint)
        else:
            loop = False
            
def warehouse_door(game = N_game()):
    loop = True
    while loop:
        if(game.game_over == False):
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- WAREHOUSE DOOR --") + "\n")
            print_tab("As you stand in front of the warehouse you see an all too familiar " + pr_colour("l_blue", "Card Reader") + " placed on ")
            print_tab("the wall on the left of the door. ")
            var = san_input()
                    
            if var == "cardreader":
                card_reader(game)
            
            else:
                hint = "Don't lick icy lamp posts"
                loop = game.basic_game_func(var, hint)
        else:
            loop = False

def card_reader(game = N_game()):
    if(game.game_over == False):
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- CARD READER --") + "\n")
        check = game.pc.check_inventory("Warehouse - ID Card")
        if check:
            print_tab("You scan the Warehouse ID Card and an affirmative *beep* comes from the Card Reader." )
            print_tab("Pushing the door open, you enter the Warehouse.")
            pause()
            warehouse(game)
        else:
            print_tab("You can try using your Guest ID Card however a down beat *boop* sound tells you that" )
            print_tab("it doesn't have an access level high enough to enter the Warehouse." )
            # s_pause()
            # game.set_new_ob("Search Nearby for a Warehouse ID")      
            pause()  
        
          
def hall_3(game = N_game()):
    # Not Complete
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((1,3),game.game_map.pre)   
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- HALL WAY (3) --") + "\n")
        print_tab("The corridor continues on " + pr_colour("l_blue","Forward") + " with the odd light overhead having blown its bulb. A few ")
        print_tab("paces ahead of you a janitors " + pr_colour("l_blue","Supply Cart") + " sits unattended. Apart of it this section of the ")
        print_tab("hallway is bare.")
        var = san_input()
        
        
        if var == "supplycart":
            supply_cart(game)
        
        elif var == "forward":
            hall_4(game)
        
        else:
            hint = "Don't lick icy lamp posts"
            loop = game.basic_game_func(var, hint)


    
def supply_cart(game = N_game()):
    # Not Complete
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- CLEANING SUPPLY CART --") + "\n")
    print_tab("The supply cart has a number of different items used to resupply toilets, A few toilet rolls, ")
    print_tab("some liquid soap refills and a three packs of paper towel refills. ")
    pause()

def hall_4(game = N_game()):
    # Not Complete
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((0,3),game.game_map.pre)   
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- HALL WAY (4) --") + "\n")
        print_tab("At this point the long straight main corridor comes to a stop in its forward direction. It ")
        print_tab("carries on to the " + pr_colour("l_blue","Right") + " a bit further. On the left there is a door marked as " + pr_colour("l_blue","Stairs") + ".")
        var = san_input()
        
        
        if var == "stairs":
            stairs(game)
        
        elif var == "right":
            hall_6(game)
        
        else:
            hint = "Don't lick icy lamp posts"
            loop = game.basic_game_func(var, hint)
    

def stairs(game = N_game()):
    # Not Complete
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- DOOR TO STAIRS --") + "\n")
    print_tab("On closer inspection the door to the stairs appears to have a notice posted on it. The ")
    print_tab("notice reads: 'Stairs out of use due to construction. Please use Lift.'")
    pause()

       
def hall_6(game = N_game()):
    # Not Complete
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((0,4),game.game_map.pre)   
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- HALL WAY (6) --") + "\n")
        print_tab("This section of the corridor is a bit colder than the others and a draft makes the hairs on ")
        print_tab("the back of you're neck stand on end. You look ahead and see a " + pr_colour("l_blue","Fire Exit") + ". You assume this is ")
        print_tab("what is creating the draft. On your left are a set of doors marked as " + pr_colour("l_blue","Toilets") + " one for men and  ")
        print_tab("one for women.")
        var = san_input()
        
        
        if var == "toilets":
            toilets(game)
        
        elif var == "fireexit":
            fire_exit(game)
        
        else:
            hint = "Don't lick icy lamp posts"
            loop = game.basic_game_func(var, hint)
    
def toilets(game = N_game()):
    # Not Complete
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- TOILETS --") + "\n")
    print_tab("The door of the male toilets looks more used with the paint around the bottom chipping from")
    print_tab("impacts with work boots. You don’t feel any need to use the toilets so you move on.")
    pause()
    
def fire_exit(game = N_game()):
    # Not Complete
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- FIRE EXIT --") + "\n")
    print_tab("Stepping up to the Fire Exit you see that a strip of foam that had been excluding the draft ")
    print_tab("has come away from the bottom of the door. A sticker on the door reads: ‘Warning: This door ")
    print_tab("is Alarmed’. Not knowing what you did to alarm the door, you step back into the corridor. ")
    pause()
    


if __name__ == "__main__":
    game = N_game()
    hall_1(game)

