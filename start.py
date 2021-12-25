from libraries import *
from text import *
from game import *
from reception import recep

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
    clear_screen()
    # ascii_del_dil()
    
    print(pr_colour("l_blue","\n\tWelcome to Delviery Dilemma"))
    s_pause()


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

def menu():
    ext = False
    while not ext:
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- MAIN MENU --") + "\n")
        print_tab("[1] Start\n")
        print_tab("[2] Help\n")
        print_tab("[3] About\n")
        print_tab("[4] Exit\n")

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


# MAIN FUNCTION
def main():

    game_intro()
    
    menu()
  
if __name__ == "__main__":
    main()
    