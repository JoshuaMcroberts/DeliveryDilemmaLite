from libraries import *
from text import *
from game import *
from reception import recep

# DISPLAY HELP TEXT
def help_text():
    clear_screen()
    print_tab("Help text will go here!")


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
    # ascii_del_dil()
    
    print(pr_colour("l_blue","\n\tWelcome to Delviery Dilemma"))
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
        print("")
        print_tab(pr_colour("l_blue","-- MAIN MENU --") + "\n")
        print_tab("[1] Start\n")
        print_tab("[2] Help\n")
        print_tab("[3] Credits\n")
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
            cred_text()
            pause()
        elif main_op == 4:
            print("")
            print_tab(pr_colour("l_orange","Thanks for playing, Bye for Now!\n"))
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
    
