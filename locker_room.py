from libraries import *
from mmap import *
from game import N_game


def locker_room(game = N_game()):
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((3,2),game.game_map.pre)   
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- LOCKER ROOM --")+"\n")
        print_tab("The room is narrow and bordering three walls are a collection of storage lockers. ")
        print_tab("Ten full size " + pr_colour("l_blue","Lockers") + " are against the right-hand wall with a matching Ten opposite ")
        print_tab("them against the left-hand wall. The wall towards the back of the room is roughly ")
        print_tab("half the size of the other two walls and therefore has two rows of five half-sized ")
        print_tab("lockers which had been stacked to give in total an additional Ten lockers, 30 in total.")
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
        print("")
        print_tab(pr_colour("l_blue","-- LOCKERS --") + "\n")
        print_tab("Enter the locker number you wish to search:" )
        print_tab("You may need a " + pr_colour("l_blue","Hint") + " to start your search.")
        var, num = item_input()
        
        if str(type(num)) != "<class 'int'>":
            
            var = san_text(var + str(num))
        
        if var == "locker" and num > 0 and num < 31:
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- LOCKER " + str(num) + " --") + "\n")
            
            if num < 14:
                
                print_tab("You open " + pr_colour("l_blue","Locker " + str(num)) + " and find that it is empty.")
               
                           
            elif num < 21:
                
                print_tab("You go to open " + pr_colour("l_blue","Locker " + str(num)) + " but it appears to be locked.")
            
            
            elif num == 21:
                locker_21(game)
            
            elif num < 24:
                
                print_tab("You go to open " + pr_colour("l_blue","Locker " + str(num)) + " but it appears to be locked.")
                
            elif num < 28:
                
                if game.get_key == False:
                    print_tab("As you open " + pr_colour("l_blue","Locker " + str(num)) + " you hear someone else enter the room. You pretend to be retrieving ")
                    print_tab("something from your non-existent bag in the empty locker. The person passes behind you and goes ")
                    print_tab("further down your row. Out of the corner of your eye you see them take their pass from around ")
                    print_tab("their neck and put it inside the locker. They then take out a lunch box and lock their locker behind ")
                    print_tab("them. As they exit the room they slip their locker key into the pocket of their worn work coat. ")
                    game.get_key = True
                    game.set_new_ob("Follow the worker and find a way to get their locker key")
                    
                else:
                    print_tab("You open " + pr_colour("l_blue","Locker " + str(num)) + " and find that it is empty.")
               
                
            elif num < 31:
                print_tab("You go to open " + pr_colour("l_blue","Locker " + str(num)) + " but it appears to be locked.")
            pause()
            
        else:
            hint = "Type: Locker 1"
            loop = game.basic_game_func(var, hint)

def locker_21(game = N_game()):
    
    bol = game.pc.check_inventory("Locker 21 - Key")
    
    if bol and game.locker_21_empty == False:
        print_tab("You slide the key for locker 21 into the lock and open it. Inside the locker is a black ")
        print_tab("backpack which is open and a security pass with the words 'Marvin Bleak - Warehouse Opts' ")
        print_tab("on it. You take the pass and relock the locker. ")
        game.locker_21_empty = True
        s_pause()
        game.completed_spec_ob("Open Locker 21")
        s_pause()
        game.set_new_ob("Enter the Warehouse")
        s_pause()
        game.pc.add_inventory("Warehouse - ID Card")
        
        
   
    elif bol and game.locker_21_empty:
        print_tab("You slide the key for locker 21 into the lock and open it. Inside the locker is a black  ")
        print_tab("backpack which is open and seems to have had a box removed from it. Nothing useful here, ")
        print_tab("you close and relock the locker.")
    else:
        print_tab("You go to open " + pr_colour("l_blue","Locker 21") + " but it appears to be locked.")
    
    


if __name__ == "__main__":
    game = N_game()
    game.pc.inventory = ["Locker 21 - Key"]
    locker_room(game)

