from libraries import *
from text import *
from game import *
from rooms import recep

# DISPLAY HELP TEXT
def help_text():
    clear_screen()
    print_tab("Help text will go here!")


# DISPLAY ABOUT TEXT
def about_text():
    clear_screen()
    print_tab("About text will go here!")


# DISPLAY ASCII ART
def game_intro():
    print_tab("Delviery Dilemma\n")


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
    # Game ACT 1
    act_1_intro(cour, pc)
    game.game_map.print_map()
    recep(game)
    # Game ACT 2
    # - Getting in  
    # - Sec Office
    # - Reception 
    # - Outside main enterence
    # - Outside Firedoor
    # - Outside loading bay enterence
    
    # Game ACT 3 
    # - Hall 1
    # -- Admin Offices
    # - Hall 2
    # -- Hall 5
    # - Hall 3
    # -- Unknown Room
    # - Hall 4 
    # -- Stairs
    # -- Fire door
    # -- Toilets
    # - Hall 5
    # -- Locker Room
    # -- Canteen/Lounge


# MAIN FUNCTION
def main():

    game_intro()
    ext = False
    while not ext:
        clear_screen()
        print_tab("Main Menu")
        print_tab("[1] Start")
        print_tab("[2] Help")
        print_tab("[3] About")
        print_tab("[4] Exit")

        try:
            main_op = int(input("\tEnter Option: "))
        except:
            main_op = 10   

        if main_op == 1:
            new_game()
        elif main_op == 2:
            help_text()
            pause()
        elif main_op == 3:
            about_text()
            pause()
        elif main_op == 4:
            print_tab(pr_colour("purple","Bye Bye"))
           
            ext = True
        else:
            print_tab("Select a Number from 1-4")
            pause()

  
if __name__ == "__main__":
    main()
    