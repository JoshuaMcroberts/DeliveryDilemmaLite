from libraries import *
from mmap import *
from game import N_game


def locker_room(game = N_game()):
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((3,2),game.game_map.pre)   
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- LOCKER ROOM --")+"\n")
        print_tab("lockers")
        print_tab("The room is narrow and bordering three walls are a collection of storage lockers. ")
        print_tab("Ten full size lockers are against the right-hand wall with a matching Ten opposite ")
        print_tab("them against the left-hand wall. The wall towards the back of the room is roughly ")
        print_tab("half the size of the other two walls and therefore has two rows of five half-sized ")
        print_tab("lockers which had been stacked to give in total an additional Ten lockers. ")
        print_tab("Each locker is sequentially numbered.")
        var = san_input()
        
       
        # Navigation IF  
        if var  == "lockers":
            print("")
            # enter locker number you would like to search
            lockers(game)
            
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


       
def lockers(game = N_game()):
    
    loop = True
    while loop:  
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- LOCKERS --") + "\n")
        print_tab("locker 1 - locker 30")
        print_tab("Enter the locker number you wish to search by typing: 'Locker <NUMBER>'.")
        var, num = item_input()
        
        if var == "locker" and num > 0 and num < 31:
        
            if num < 14:
                clear_screen()
                print_tab(pr_colour("l_blue","-- LOCKER " + str(num) + " --") + "\n")
                print_tab("You open " + pr_colour("l_blue","locker " + str(num)) + " and find that it is empty.")
                pause()
                           
            elif num < 21:
                clear_screen()
                print_tab(pr_colour("l_blue","-- LOCKER " + str(num) + " --") + "\n")
                print_tab("You go to open " + pr_colour("l_blue","'locker ' + num") + " but it appears to be locked.")
                pause()
            
            elif num == 21:
                locker_21(game)
                
            elif num < 26:
                clear_screen()
                print_tab(pr_colour("l_blue","-- LOCKER " + str(num) + " --") + "\n")
                print_tab("As you open " + pr_colour("l_blue","'locker ' + num") + " you hear someone else enter the room. You pretend to be retrieving ")
                print_tab("something from your non-existent bag in the empty locker. The person passes behind you and goes ")
                print_tab("further down your row. Out of the corner of your eye you see them take their pass from around ")
                print_tab("their neck and put it inside the locker. They then take out a lunch box and locking their locker behind ")
                print_tab("them. As they exit the room they slip their locker key into the pocket of their worn work coat. ")
                # Progression
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

def locker_21(game = N_game()):
    
    clear_screen()
    print_tab(pr_colour("l_blue","-- LOCKER 21 --") + "\n")
    
    if 1 == 2 and 3 == 3:
        print_tab("You slide the key for locker 21 into the lock and open it. Inside the locker is a black backpack which is ")
        print_tab("open and a security pass with the words ‘ Marvin Bleak – Warehouse Opts ’ on it. You take the pass ")
        print_tab("and relock the locker. ")
        inventory # add ware house id pass to inventory
   
    elif 1 == 2 and 3 == 4:
        print_tab("You slide the key for locker 21 into the lock and open it. Inside the locker is a black backpack which is ")
        print_tab("open and seems to have had a box removed from it. Nothing useful here, you close and relock the locker.")
    
    else:
        print_tab("You go to open " + pr_colour("l_blue","'locker ' + num") + " but it appears to be locked.")
    ## Locked
    
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
    locker_room(game)

