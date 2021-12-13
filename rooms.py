from libraries import *

def recep():
    loop = True
    while loop:
        clear_screen()
        print_tab(pr_colour("l_blue","-- RECEPTION --")+"\n")
        print_tab("The foyer of the building stretches out in a large oval with the narrow ends on the left and right.")
        print_tab("A semi-circler, tall " + pr_colour("l_blue","Reception Desk") + " is prominently placed against the back wall of the room with a ")
        print_tab("large double " + pr_colour("l_blue","Glass Door") + " to its left which leads further into the building.")
        print_tab("On the left side of the room there is another door with the name plate on it saying, " + pr_colour("l_blue","Security Office") + ". ")
        print_tab("As you look to the right of the room, you see a " + pr_colour("l_blue","Lift") + " door and a " + pr_colour("l_blue","Waiting Area") + " which is ")
        print_tab("nestled to back up against the glass front windows. ")
        var = san_input()
        
        # print_tab(var)
        
        if var  == "receptiondesk":
            recep_desk()
            
        elif var == "glassdoor":
            glass_door()
            
        elif var == "securityoffice":
            sec_office()
            
        elif var == "lift":
            lift()
            
        elif var == "waitingarea":
            waiting_area()
            
        elif var == "exit":
            loop = False
            
        else:
            print_tab("Incorrect entry try again")
            pause()

def recep_desk():
    clear_screen()
    print_tab("RD")
    pause()
    
def glass_door():
    clear_screen()
    print_tab(pr_colour("l_blue","-- GLASS DOOR --") + "\n")
    print_tab("You approach the glass door and see next to it on the wall a small electronic pad.")
    print_tab("It looks like a " + pr_colour("l_blue", "Card Reader")+". You can see the hallway beyond with a few doors ")
    print_tab("leading off to either side.")
    var = san_input()
    
     
    
    

    
def sec_office():
    clear_screen()
    print_tab("SO")
    pause()
    
def lift():
    clear_screen()
    print_tab(pr_colour("l_blue","-- LIFT --") + "\n")
    print_tab("You walk over to the lift to take a closer look. There is a number pad and")
    print_tab("a card reader next to the door however above them is a seemingly freshly")
    print_tab("printed piece of paper taped to the wall saying “Out of Order”")
    pause()
    
def waiting_area():
    
    wait = 0
    loop1 = True
    while loop1:
        clear_screen()
        print_tab(pr_colour("l_blue","-- WAITING AREA --") + "\n")
        print_tab("The waiting area consists of three tan leather sofas set in a U shape, with the open")
        print_tab("end facing the main entrance. This gives each sofa a varying view, from the reception")
        print_tab("to the those entering through the main door and the final facing out the window to ")
        print_tab("the carpark area outside. There are a few magazines laid out on a short coffee table")
        print_tab("in the middle of the U shape to help pass the " + pr_colour("l_blue","Wait") + ".")
        var = san_input()

        if var == "wait":
            if wait < 4:
                clear_screen()
                print_tab("<character> rests in the waiting area for half an hour. Nothing happens.")
                wait += 1
                pause()
                # notepad option change wait < 4 to 3
            elif wait < 5:
                clear_screen()
                print_tab("<character> rests in the waiting area for half an hour. The Receptionist gets up, scans")
                print_tab("her pass and leaves through the glass door, only to return 5 mins later with a cup")
                print_tab("of coffee and a small piece of fruit.")
                wait += 1
                pause()
                
            elif wait < 6:
                clear_screen()
                print_tab("<character> rests in the waiting area for half an hour. A delivery man enters the reception and drags a")
                print_tab("sack truck across the floor which appears to have one flat wheel. The security guard emerges from")
                print_tab("his office and escorts the delivery man through the glass door and then back out again after another")
                print_tab("10 minutes has passed.")
                wait += 1
                pause()
                
            elif wait < 8:
                clear_screen()
                print_tab("<character> grows tired of waiting. Another half hour passes.")
                wait += 1
                pause()
                
            elif wait < 9:
                clear_screen()
                print_tab("<character> rests in the waiting area for half an hour. Closing time approaches.")
                wait += 1
                pause()
                
            else:
                clear_screen()
                print_tab("<character> rests in the waiting area. The Security Guard emerges from his office and escorts <character>")
                print_tab("out of the building as it is closing time. ")
                print_tab("Game Over")
                pause()
                
        elif var == "back":
            # not wait
            print_tab("")    
            loop1 = False
        else:
            clear_screen()
            print_tab("Try typing 'Back'")
            pause()
            
             
             
            


if __name__ == "__main__":
    recep()

