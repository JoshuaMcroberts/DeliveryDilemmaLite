from libraries import *
from mmap import *
from game import N_game

def canteen(game = N_game()):
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((1,2),game.game_map.pre)   
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- CANTEEN --")+"\n")
        print_tab("The Canteen is a small room with a " + pr_colour("l_blue","Bench") + " that starts against the right-hand wall and wraps ")
        print_tab("around the edge of the room to the back wall. A " + pr_colour("l_blue","Fridge") + " stands up-right against the back wall, ")
        print_tab("pushed into the left corner of the room. A " + pr_colour("l_blue","Coat Rack") + " seems to have been haphazardly attached  ")
        print_tab("to the wall on the left of the door as you enter the room. Two workers sit at one of the two ")
        print_tab("tables in the room staring at their phones. ")
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
        
        else:
            hint = "Don't lick icy lamp posts"
            loop = game.basic_game_func(var, hint)
            

def worker_1(game = N_game()):
    loop = True
    while loop:
        
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- WORKER 1 --")+"\n")
        print_tab("worker1 worker2 fridge coatrack bench ")
        print_tab("")
        print_tab("")
        var = san_input()
        
        # Navigation IF  
        if var  == "talk":
            print("Convo Tree")
            pause()
        
        else:
            hint = "Don't lick icy lamp posts"
            loop = game.basic_game_func(var, hint)

def worker_2(game = N_game()):
    clear_screen()
    print_tab("Worker 2")
    pause()

def fridge(game = N_game()):
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- FRIDGE --")+"\n")
    print_tab("You move over to the fridge and notice that the exterior hasn’t been wiped down in a long ")
    print_tab("while. You open the door and take note that there is a plastic case of eggs and a single ")
    print_tab("loaf of bread. In contrast with the exterior, the interior of the fridge looks like it is ")
    print_tab("cleaned out regularly. Not much of use in here.")
    pause()



def egg(game = N_game()):
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- EGG --") + "\n")
    print_tab("")
    pause()

def lunch_box(game = N_game()):
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- LUNCH BOX --") + "\n")
    print_tab("")
    pause()


def bench(game = N_game()):
    
    loop = True
    while loop:
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- BENCH --") + "\n")
        print_tab("Wrapping the back wall and round to the right hand side of the room, the bench creates a ")
        print_tab("convenient area for people to stand around for a coffee break or an adequate work top for ")
        print_tab("food preparation. Setting on the bench are two electrical appliances. One being a " + pr_colour("l_blue","Toaster"))
        print_tab("and the other being a " + pr_colour("l_blue","Microwave")+ ". Both look a little worse for ware.  ")
        var = san_input()
        
        if var == "microwave":
            microwave(game)
            
        elif var == "toaster":
            toaster(game)
        
        else:
            hint = "Don't lick icy lamp posts"
            loop = game.basic_game_func(var, hint)

def toaster(game = N_game()):
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- TOASTER --") + "\n")
    print_tab("You look into the toaster and see a lifetimes accumulation of bread crumbs gathered at the ")
    print_tab("bottom of it bread toasting wells. You think to yourself that it is a fire just waiting to ")
    print_tab("happen. Looking at the power cable also makes you bristle as you see the cable has been cut ")
    print_tab("and spliced onto a different plug and some electrical tape has been crudely employed as to")
    print_tab("cover up the poor workmanship. You stop inspecting the toaster and step back tot he centre ")
    print_tab("of the room.")
    pause()

def microwave(game = N_game()):
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- MICROWAVE --") + "\n")
    print_tab("You open the microwave to take a look and find it is by far the most well used appliance in ")
    print_tab("the canteen. You draw this conclusion from the numerous different colours of stains on its ")
    print_tab("interior that mark each time a new food stuff has been heated or over heated inside it. You ")
    print_tab("quickly shut the microwave door and step back just in time as a stale heated smell starts to")
    print_tab("rise to your nose. You probably shouldn’t open that again.")
    pause()



def coat_rack_canteen(game = N_game()):
    
    loop = True
    while loop:  
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- COAT RACK --") + "\n")
        print_tab("A brief glace at the coat rack informs you that there are two items of clothing hanging")
        print_tab("there. The first of which being an old tattered high-vis vest and the second of which being" )
        print_tab("a work " + pr_colour("l_blue","Coat") + ".")
        var = san_input()
        
        
        if var == "coat":
            coat(game)

        else:
            hint = "Don't lick icy lamp posts"
            loop = game.basic_game_func(var, hint)

def coat(game = N_game()):
    
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((1,3),game.game_map.pre)   
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- Coat --") + "\n")
        print_tab("The coat looks like it has been in use for some time. It has high-vis strips strategically ")
        print_tab("sown onto it. It seems to be a straight-forward design with a " + pr_colour("l_blue","Left Pocket") + " and " + pr_colour("l_blue","Right Pocket"))
        print_tab("the only two places ")
        var = san_input()
        
        
        if var == "leftpocket":
            left_pocket(game)
        
        elif var == "rightpocket":
            right_pocket(game)
        
        else:
            hint = "Don't lick icy lamp posts"
            loop = game.basic_game_func(var, hint)


    
def left_pocket(game = N_game()):
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- LEFT POCKET --") + "\n")
    if game.got_key == False:
        print_tab("When you slip your hand into the left pocket of the coat it immediately comes into contact ")
        print_tab("with something cold and metallic. You withdraw your hand to find clutched in it a locker key ")
        print_tab("with the number 21 written on a tag attached to it. ") 
        game.pc.add_inventory("Locker 21 - Key")
        game.got_key = True
        s_pause()
        game.completed_spec_ob("Follow the worker and find a way to get their locker key")
        s_pause()
        game.set_new_ob("Open Locker 21")
        pause()
    else:
        print_tab("The left pocket is empty.")
        pause()

def right_pocket(game = N_game()):
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- RIGHT POCKET --") + "\n")
    print_tab("You put your hand quickly into the right pocket and bring it out to find it contains only a ")
    print_tab("sticky old boiled sweet and some pocket lint which has now become stuck to your fingers.")
    pause()

if __name__ == "__main__":
    game = N_game()
    canteen(game)

