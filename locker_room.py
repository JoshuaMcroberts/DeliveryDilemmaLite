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
        print_tab("Ten full size " + pr_colour("l_blue","Lockers") + " are against the right-hand wall with a matching Ten opposite ")
        print_tab("them against the left-hand wall. The wall towards the back of the room is roughly ")
        print_tab("half the size of the other two walls and therefore has two rows of five half-sized ")
        print_tab("lockers which had been stacked to give in total an additional Ten lockers. ")
        print_tab("Each locker is sequentially numbered.")
        var = san_input()
        
       
        # Navigation IF  
        if var  == "lockers":
            print("")
            lockers(game)
        
        else:
            hint = "Don't lick icy lamp posts"
            loop = game.basic_game_func(var, hint)


       
def lockers(game = N_game()):
    
    loop = True
    while loop:  
        clear_screen()
        # update text
        print_tab(pr_colour("l_blue","-- LOCKERS --") + "\n")
        print_tab("Enter the locker number you wish to search:" )
        var, num = item_input()
              
        if var == "locker" and num > 0 and num < 31:
        
            if num < 14:
                clear_screen()
                print_tab(pr_colour("l_blue","-- LOCKER " + str(num) + " --") + "\n")
                print_tab("You open " + pr_colour("l_blue","Locker " + str(num)) + " and find that it is empty.")
                pause()
                           
            elif num < 21:
                clear_screen()
                print_tab(pr_colour("l_blue","-- LOCKER " + str(num) + " --") + "\n")
                print_tab("You go to open " + pr_colour("l_blue","Locker " + str(num)) + " but it appears to be locked.")
                pause()
            
            elif num == 21:
                locker_21(game)
                
            elif num < 26:
                clear_screen()
                print_tab(pr_colour("l_blue","-- LOCKER " + str(num) + " --") + "\n")
                
                if game.get_key == False:
                    print_tab("As you open " + pr_colour("l_blue","Locker " + str(num)) + " you hear someone else enter the room. You pretend to be retrieving ")
                    print_tab("something from your non-existent bag in the empty locker. The person passes behind you and goes ")
                    print_tab("further down your row. Out of the corner of your eye you see them take their pass from around ")
                    print_tab("their neck and put it inside the locker. They then take out a lunch box and locking their locker behind ")
                    print_tab("them. As they exit the room they slip their locker key into the pocket of their worn work coat. ")
                    game.get_key = True
                else:
                    print_tab("You open " + pr_colour("l_blue","Locker " + str(num)) + " and find that it is empty.")
                pause()     
                
            elif num < 31:
                clear_screen()
                print_tab(pr_colour("l_blue","-- LOCKER " + str(num) + " --") + "\n")
                print_tab("You go to open " + pr_colour("l_blue","Locker " + str(num)) + " but it appears to be locked.")
                pause()
            
        else:
            hint = "Don't lick icy lamp posts"
            loop = game.basic_game_func(var, hint)

def locker_21(game = N_game()):
    
    clear_screen()
    print_tab(pr_colour("l_blue","-- LOCKER 21 --") + "\n")
    bol = game.pc.check_inventory("Locker 21 - Key")
    
    if bol and game.locker_21_empty == False:
        print_tab("You slide the key for locker 21 into the lock and open it. Inside the locker is a black backpack which is ")
        print_tab("open and a security pass with the words 'Marvin Bleak - Warehouse Opts' on it. You take the pass ")
        print_tab("and relock the locker. ")
        game.locker_21_empty = True
        game.pc.add_inventory("Warehouse - ID Card")
        
   
    elif bol and game.locker_21_empty:
        print_tab("You slide the key for locker 21 into the lock and open it. Inside the locker is a black backpack which is ")
        print_tab("open and seems to have had a box removed from it. Nothing useful here, you close and relock the locker.")
    
    else:
        print_tab("You go to open " + pr_colour("l_blue","Locker 21") + " but it appears to be locked.")
    ## Locked
    
    pause()
    


if __name__ == "__main__":
    game = N_game()
    game.pc.inventory = ["Locker 21 - Key"]
    locker_room(game)

