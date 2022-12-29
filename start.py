from libraries import *
from text import *
from game import *
from reception import recep
import TimeLock
import os

# DISPLAY HELP TEXT
def help_text():
    print_tab(pr_colour("l_blue","-- HELP --")+"\n")
    print_tab("You can use the following options anytime you see the '>' character:\n")
    print_tab("back        - This will take you back out of the description you are in.\n")
    print_tab("map         - This will show you the map and where you are on it.\n")
    print_tab("objectives  - This will show a list of current objectives is.\n")    
    print_tab("who am i    - This will show you your characters name.\n")      
    print_tab("inventory   - This will list all the items you have.\n")
    print_tab("hint        - This will give you a hint for the location you are in.\n")  
    pause()
              


# DISPLAY ABOUT TEXT
def cred_text():
    clear_screen()
    print_tab(pr_colour("l_green","-- CREDITS --"))
    print()
    print_tab("Intro Story Reviewers - C. Cadden, J. Harrower, S. Kavuri \n")
    print_tab("Receptionsist Name    - S. Kavuri\n")
    print_tab("Alpha Testers         - R. McRoberts, D. McRoberts, A. McRoberts\n")
    print_tab("Beta Testers          - J. Smyth, N. Smyth\n")
    print_tab("User Testers          - P. Shields, N. Scott-Murphy\n")
    

# DISPLAY ASCII ART
def game_intro():
    clear_screen()
    ascii_del_dil()
    s_pause()

# DISPLAYS GAME OVER ASCII ART
def game_over():
    ascii_game_over()

# GAME FUNCTION
def new_game():
    clear_screen()
    game = N_game()
    game.enter_name()
    game.set_courier()
    game.create_char()
    pc = game.get_character()
    cour = game.get_courier()
    
    pause()
    act_1_intro(cour, pc)
    recep(game)
    game_over()

def menu():
    ext = False
    while not ext:
        clear_screen()
        printNew()
        print_tab(pr_colour("l_blue","-- MAIN MENU --") + "\n")
        print_tab("[1] Start\n")
        print_tab("[2] Help\n")
        print_tab("[3] Credits\n")
        print_tab("[4] Exit\n")

        try:
            main_op = int(input("\t\tEnter Option: "))
        except:
            main_op = 10   

        if main_op == 1:
            new_game()
        elif main_op == 2:
            help_text()
            pause()
        elif main_op == 3:
            cred_text()
            pause()
        elif main_op == 4:
            printNew()
            print_tab(pr_colour("l_orange","Thanks for playing, Bye for Now!\n"))
            ext = True
        else:
            print_tab("Select a Number from 1-4")
            pause()


# MAIN FUNCTION
def main(test):
    
    cmd ="mode con cols=140 lines=40"
    
    os.system(cmd)
    
    TimeLock.timeCheck(test) # Set True for testing
    
    # game_intro()
    
    menu()
  
if __name__ == "__main__":
    main(True)
    
