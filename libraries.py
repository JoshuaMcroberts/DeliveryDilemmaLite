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