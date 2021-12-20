from libraries import *
from mmap import *
from game import N_game
from security_office import *

def recep(game = N_game()):
    loop = True
    while loop:
        if(game.game_over == False):
            if (game.sec_gar == False and game.game_map.pre == (4,2)):
                game.sec_gar = True
                clear_screen()
                print_tab(pr_colour("l_blue","-- LEAVING THE SECURITY OFFICE --")+"\n")
                print_tab("As you exit the security office you look through the Glass door down the hallway. You see the Security Guard")
                print_tab("Just rounding the corner into the main corridor on his return journey. That was good timing, another minute")
                print_tab("and he would have caught you. Step into the centre of the reception as he enters and quickly moves past you")
                print_tab("back to the Security Office")
                pause()
                
            game.game_map.pre = game.game_map.player_enter((4,3),game.game_map.pre)   
            clear_screen()
            print_tab(pr_colour("l_blue","-- RECEPTION --")+"\n")
            print_tab("The foyer of the building stretches out in a large oval with the narrow ends on the left and right.")
            print_tab("A semi-circler, tall " + pr_colour("l_blue","Reception Desk") + " is prominently placed against the back wall of the room with a ")
            print_tab("large double " + pr_colour("l_blue","Glass Door") + " to its left which leads further into the building.")
            print_tab("On the left side of the room there is another door with the name plate on it saying, " + pr_colour("l_blue","Security Office") + ". ")
            print_tab("As you look to the right of the room, you see a " + pr_colour("l_blue","Lift") + " door and a " + pr_colour("l_blue","Waiting Area") + " which is ")
            print_tab("nestled back up against the glass front windows. ")
            var = san_input()
            
        
            # Navigation IF  
            if var  == "receptiondesk":
                recep_desk(game)
                
            elif var == "glassdoor":
                glass_door(game)
                
            elif var == "securityoffice":
                sec_office(game)
                
            elif var == "lift":
                lift(game)
                
            elif var == "waitingarea":
                waiting_area(game)
                
            elif var == "exit":
                loop = False
                
            elif var == "map":
                clear_screen()
                game.game_map.print_map()
                pause()
            
            else:
                print("")
                print_tab("Incorrect entry try again")
                pause()
        else:
            loop = False

def recep_desk(game = N_game()):
    loop = True
    while loop:
        clear_screen()
        print_tab(pr_colour("l_blue","-- RECEPTION DESK --") + "\n")
        print_tab("As you approach the Reception desk you see a brown haired " + pr_colour("l_blue","receptionist") +" wearing intelligent")
        print_tab("looking yet elegant round frame glasses. She appears to be engrossed in her work and doesn't notice")
        print_tab("you immediately. You take the opportunity to glance over the top edge of the desk, down at the")
        print_tab("items on the desk top. There seems to be a number of post-it notes scattered around, normally ")
        print_tab("just out of view. A phone sits on the far side of the desk, where a second receptionist would more ")
        print_tab("easily be able to answer it and a " + pr_colour("l_blue","notepad") +", with something written on it is placed within easy ")
        print_tab("reaching distance of the receptionist.")
        var = san_input()
        
        if var == "receptionist":
            # receptionist()
            print("")
            
        elif var == "notepad":
            notepad()
            
            
        elif var == "back":
            loop = False
        
        elif var == "map":
            clear_screen()
            game.game_map.print_map()
            pause()
        
        else:
            print("")
            print_tab("Incorrect entry try again")
            pause()

def notepad(game = N_game()):
    clear_screen()
    print_tab(pr_colour("l_blue","-- Notepad --") + "\n")
    print_tab("Reading the notepad upside down and slightly sideways, you see the words written: “Guest Pass for  new ")
    print_tab("salesman Mr Preston - Expected @14:45”. This gives you an idea! You could call reception and pretend to ")
    print_tab("be 'Mr Preston'. Now all you have to do is find another phone! ")
    print_tab("(New objective)")
    game.preston = True
    pause()
 
def glass_door(game = N_game()):
    loop = True
    while loop:
        clear_screen()
        print_tab(pr_colour("l_blue","-- GLASS DOOR --") + "\n")
        print_tab("You approach the glass door and see next to it on the wall a small electronic pad.")
        print_tab("It looks like a " + pr_colour("l_blue", "Card Reader") + ". You can see the hallway beyond with a few doors ")
        print_tab("leading off to either side.")
        var = san_input()
        
        
        if var == "cardreader":
            card_reader()
        elif var == "back":
            loop = False
        
        elif var == "map":
            clear_screen()
            game.game_map.print_map()
            pause()
        
        else:
            print("")
            print_tab("Incorrect entry try again")
            pause()


def card_reader(game = N_game()):
    clear_screen()
    print_tab(pr_colour("l_blue","-- CARD READER --") + "\n")
    
    if():
        print()
    print_tab("You approach the glass door and see next to it on the wall a small electronic pad.")
    print_tab("It looks like a " + pr_colour("l_blue", "Card Reader") + ". You can see the hallway beyond with a few doors ")
    print_tab("leading off to either side.")
    var = san_input()

    

    
def lift(game = N_game()):
    clear_screen()
    print_tab(pr_colour("l_blue","-- LIFT --") + "\n")
    print_tab("You walk over to the lift to take a closer look. There is a number pad and")
    print_tab("a card reader next to the door however above them is a seemingly freshly")
    print_tab("printed piece of paper taped to the wall saying “Out of Order”")
    pause()
    
def waiting_area(game = N_game()):
    # 2nd Prioity - gaurd leave office
    wait = game.wait
    loop = True
    while loop:
        if(game.game_over == False):
            clear_screen()
            print_tab(pr_colour("l_blue","-- WAITING AREA --") + "\n")
            print_tab("The waiting area consists of three tan leather sofas set in a U shape, with the open")
            print_tab("end facing the main entrance. This gives each sofa a varying view, from the reception")
            print_tab("to the those entering through the main door and the final facing out the window to ")
            print_tab("the carpark area outside. There are a few magazines laid out on a short coffee table")
            print_tab("in the middle of the U shape to help pass the " + pr_colour("l_blue","Wait") + ".")
            var = san_input()
            char_name = game.pc.character_name
            if var == "wait":
                if wait < 1:
                    clear_screen()
                    print_tab(char_name + " rests in the waiting area for half an hour. Nothing happens.")
                    wait += 1
                    pause()
                    
                elif wait < 2:
                    clear_screen()
                    print_tab(char_name + " rests in the waiting area for half an hour. As you are about to get up the Security")
                    print_tab("Guard leaves his office, scans his card at the glass door and passes through.") 
                    print_tab("Best take your chance to check out the Security office!")
                    wait += 1
                    game.sec_gar = False
                    pause()
                
                elif wait < 3:
                    clear_screen()
                    print_tab(char_name + " rests in the waiting area for half an hour. Nothing happens.")
                    wait += 1
                    pause()
                
                    # notepad option change wait < 4 to 3
                elif wait < 5:
                    clear_screen()
                    print_tab(char_name + " rests in the waiting area for half an hour. The Receptionist gets up, scans")
                    print_tab("her pass and leaves through the glass door, only to return 5 mins later with a cup")
                    print_tab("of coffee and a small piece of fruit.")
                    wait += 1
                    pause()
                    
                elif wait < 6:
                    clear_screen()
                    print_tab(char_name + " rests in the waiting area for half an hour. A delivery man enters the reception and drags a")
                    print_tab("sack truck across the floor which appears to have one flat wheel. The security guard emerges from")
                    print_tab("his office and escorts the delivery man through the glass door and then back out again after another")
                    print_tab("10 minutes has passed.")
                    wait += 1
                    pause()
                    
                elif wait < 8:
                    clear_screen()
                    print_tab(char_name + " grows tired of waiting. Another half hour passes.")
                    wait += 1
                    pause()
                    
                elif wait < 9:
                    clear_screen()
                    print_tab(char_name + " rests in the waiting area for half an hour. Closing time approaches.")
                    wait += 1
                    pause()
                    
                else:
                    clear_screen()
                    print_tab(char_name + " rests in the waiting area. The Security Guard emerges from his office and escorts <character>")
                    print_tab("out of the building as it is closing time. ")
                    print_tab("Game Over")
                    game.game_over = True
                    pause()
                
                game.wait = wait    
                
            elif var == "back":
                # not wait
                print_tab("")    
                loop = False
                
            elif var == "map":
                clear_screen()
                game.game_map.print_map()
                pause()    
                
            else:
                clear_screen()
                print_tab("Try typing 'Back'")
                pause()
        else:
            loop = False
    

if __name__ == "__main__":
    recep()

