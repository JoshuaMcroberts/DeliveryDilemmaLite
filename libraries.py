import os
import sys

# COLORED TEXT
# Example:
# prcolor(1, "prints a red text here")
def pr_colour(colour, text):
    test = 0
    colours = [("l_orange", '\033[38;5;209m'),
               ("orange", '\033[38;5;208m'),
               ("d_orange", '\033[38;5;202m'),
               ("l_blue", '\033[38;5;74m'),
               ("blue", '\033[38;5;26m'),
               ("d_blue", '\033[38;5;18m'),
               ("l_green", '\033[38;5;2m'),
               ("green", '\033[38;5;28m'),
               ("d_green", '\033[38;5;22m'),
               ("l_yellow", '\033[38;5;227m'),
               ("yellow", '\033[38;5;11m'),
               ("d_yellow", '\033[38;5;178m'),
               ("l_pink", '\033[38;5;177m'),
               ("pink", '\033[38;5;163m'),
               ("d_pink", '\033[38;5;161m'),
               ("l_purple", '\033[38;5;91m'),
               ("purple", '\033[38;5;54m'),
               ("d_purple", '\033[38;5;53m'),
               ("l_red", '\033[38;5;203m'),
               ("red", '\033[38;5;9m'),
               ("d_red", '\033[38;5;88m'),
               ("brown", '\033[38;5;94m'),
               ("olive", '\033[38;5;58m'),
               ("black", '\033[38;5;232m'),
               ("grey", '\033[38;5;241m'),
               ("white", '\033[38;5;15m'),
               ("cyan", '\033[38;5;6m'),
               ("num_p", '\033[38;5;232m\033[48;5;184m\033[1m'),
               ("us_num_p", '\033[7;5;44m\033[1m'),
               ("amazon", '\033[38;5;166m\033[1m'),
               ("prime", '\033[0m\033[38;5;166m\033[1m\033[4m'),
               ("del", '\033[38;5;232m\033[48;5;153m\033[1m'),
               ("p_force", '\033[38;5;195m\033[48;5;160m\033[1m'),
               ("ups", '\033[38;5;11m\033[48;5;52m'),
               ("fed", '\033[38;5;18m\033[48;5;153m\033[1m'),
               ("ex", '\033[38;5;166m\033[48;5;153m\033[1m'),
               ("l_blue_blink",'\033[5m\033[38;5;74m' )
               ]
    
    for col in colours:
        
        if test == 1:
            col_def = col[1]
            print(col_def + "All of the Colours\033[0m")
            # print("Col(0): {} Col(1): {} Colour: {}".format(col(0), col(1), colour))
            
            
        else:
            if col[0] == colour:
                col_out = col[1]
                # print("Col(0): {} Col(1): {} Colour: {}".format(col[0], col_out, colour))
                break
            else:
                col_out = '\033[00m'
    # print(col_out + " " + text + '\033[00m')
    if test == 1:
        return "end \033[00m"
    else:
        return col_out + text + '\033[00m'

# CLEANS TEXT TO SIMPLE FORM
def san_text(text):
    text = text.lower()
    text = text.replace(" ", "")
    return text

# TAKES IN INPUT ANS SIMPLIFIES IT
def san_input():
    var = input("\n\t> ")
    var = san_text(var)
    return var
    
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
    input("\n\tPress Enter to Continue...")
    
# Silent PAUSE FUNCTION 
def s_pause():
    print("\n\tPress Enter to Continue...",end="\r")
    input()
    sys.stdout.write("\033[F\033[K")


# READ IN AND PARSE STRING TO STR AND INT
def item_input():
    text = input("\n\t> ")
    text = text.lower()
    var = text.split(" ")
    if len(var) == 2:
        locker = var[0]
        try:
            number = int(var[1])
        except:
            locker = var[0]
            number = int("0")
    else:
        locker = var[0]
        number = int("0")
    return locker, number


if __name__ == "__main__":
    
    print("\nFORMAT OUTPUTS \n")
    
    # TEST PR_COLOUR
    print("\nTEST pr_colour Examples:")
    print("________")
    print(pr_colour("us_num_p"," JKZ" + u'\xB7'+ "8620 "))

    for i in range(10):
        print("\033[7;5;"+str(i)+"mWords"+str(i)+"\033[0m")
    


    # TEST PRINT TAB
    print("\nTEST print_tab Example:")
    print_tab("<Print Tabbed>")