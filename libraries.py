# Defines common routines
import os

# COLORED TEXT
# Example:
# prcolor(1, "prints a red text here")
def pr_colour(colour, text):
    # color:
    # 1 Red
    # 2 Green
    # 3 Yellow / Orange
    # 4 Blue
    # 5 Purple
    # 6 Cyan (Light Blue)
    # 7 Light Gray
    # 8 Black
    return '\033[9' + str(colour) + 'm' + text + '\033[00m'

# CLEAR SCREEN
def clear_screen(lines=100):
    if os.name == 'posix':
        os.system('clear')
    elif os.name in ('nt', 'dos', 'ce'):
        os.system('cls')
    else:
        print('\n' * lines)

# PRINT WITH TAB
def print_tab(text):
    print("\t" + text)

# PAUSE FUNCTION 
def pause():
    input("\n\tHit Enter to Continue...")
    
# Silent PAUSE FUNCTION 
def s_pause():
    input("...")
    

if __name__ == "__main__":
    
    print("\nFORMAT OUTPUTS \n")
    
    # TEST PR_COLOUR
    print("\nTEST pr_colour Examples:")
    print(pr_colour(1,"1 RED"))
    print(pr_colour(2,"2 GREEN"))
    print(pr_colour(3,"3 YELLOW"))
    print(pr_colour(4,"4 BLUE"))
    print(pr_colour(5,"5 PINK"))
    print(pr_colour(6,"6 CYAN"))
    print(pr_colour(7,"7 LIGHT GREY?"))
    print(pr_colour(8,"8 BLACK?"))
    


    # TEST PRINT TAB
    print("\nTEST print_tab Example:")
    print_tab("<Print Tabbed>")