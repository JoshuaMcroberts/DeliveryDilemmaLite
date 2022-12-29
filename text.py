from libraries import *
from game import Character
import time
from ArtDisplay import *

# def ascii_del_dil():
#     deldil =[
#             FB + "      ____       __ _                         ____  _ __                              ",
#             "     / __ \___  / /_/   _____  _______  __   / __ \/_/ /__  ____ ___  ____ ___  ____ _",
#             "    / / / / _ \/ / / | / / _ \/ ___/ / / /  / / / / / / _ \/ __ `__ \/ __ `__ \/ __ `/",
#             "   / /_/ /  __/ / /| |/ /  __/ /  / /_/ /  / /_/ / / /  __/ / / / / / / / / / / /_/ / ",
#             "  /_____/\___/_/_/ |___/\___/_/   \__, /  /_____/_/_/\___/_/ /_/ /_/_/ /_/ /_/\__,_/  ",
#             "                                 /____/                                               "]
#     cols, lines = screen_size()
#     printArt(deldil, int(cols/2 - (len(deldil[0])/2)), int(lines/2-(len(deldil)/2)))

# def ascii_game_over():
#     row_1 = "\n                   ______                        ____                 \n"
#     row_2 = "                  / ____/___ _____ ___  ___     / __ \_   _____  _____\n"
#     row_3 = "                 / / __/ __ `/ __ `__ \/ _ \   / / / / | / / _ \/ ___/\n"
#     row_4 = "                / /_/ / /_/ / / / / / /  __/  / /_/ /| |/ /  __/ /    \n"
#     row_5 = "                \____/\__,_/_/ /_/ /_/\___/   \____/ |___/\___/_/     \n"
#     row_6 = "\n"
#     game_over = row_1 + row_2 + row_3 + row_4 + row_5 + row_6
    
#     row_1 = "\n   _____ __             __                      ___                __          _          \n"
#     row_2 = "  /_  __/ /  ___ ____  / /__  __ _____  __ __  / _/__  ____  ___  / /__ ___ __/_/__  ___ _\n"
#     row_3 = "   / / / _ \/ _ `/ _ \/  '_/ / // / _ \/ // / / _/ _ \/ __/ / _ \/ / _ `/ // / / _ \/ _ `/\n"
#     row_4 = "  /_/ /_//_/\_,_/_//_/_/\_\  \_, /\___/\_,_/ /_/ \___/_/   / .__/_/\_,_/\_, /_/_//_/\_, / \n"
#     row_5 = "                            /___/                         /_/          /___/       /___/  \n"
#     row_6 = "\n"
#     thanks = row_1 + row_2 + row_3 + row_4 + row_5 + row_6
    
    # clear_screen()
    # print(pr_colour("l_blue_blink",game_over))
    # print(pr_colour("l_blue",thanks))
    # time.sleep(5)
    # clear_screen()
    # print(pr_colour("l_blue",game_over))
    # print(pr_colour("l_blue",thanks))                                              
    # s_pause()
    # print_tab(pr_colour("l_blue","If you did not find the Parcel retry and make smarter choices this time round!"))
    # s_pause()

def act_1_intro(courier, pc = Character()):
    
    char_name = pc.get_char_name()
    pronoun1, pronoun2, pronoun3 = pc.get_pronouns()
      
    clear_screen()
    printNew()
    print_tab(pr_colour("l_blue","-- INTRO STORY --") + "\n")
    print_tab("It was the night before the delivery deadline before Christmas and all through the house,")
    print_tab("was heard the soft clicking and whirring of printer and mouse.")
    print_tab("Parcels lay strewn in every which way,")
    print_tab("with wrapping paper and packaging all on display.")
    pause()

    clear_screen()
    printNew()
    print_tab(pr_colour("l_blue","-- INTRO STORY --") + "\n")
    print_tab("The rush was on for the Christmas deadline, you see")
    print_tab("and " + char_name + " had left the parcel packing until after " + pronoun1 + " tea.")
    print_tab("Each box for a friend would be stacked by the stair,")
    print_tab("In hopes that in the morning " + courier + " would be there.")
    pause()
    
    clear_screen()
    printNew()
    print_tab(pr_colour("l_blue","-- INTRO STORY --") + "\n")
    print_tab("In the midst of the chaos the doorbell did ring, ")
    print_tab("“Who could that be?” " + char_name + " thought as " + pronoun2 + " tied up a string.")
    print_tab("It was a late-night delivery of something unknown,")
    print_tab("Could be a book or a beagle or an old-style gramophone?")
    pause()

    clear_screen()
    printNew()
    print_tab(pr_colour("l_blue","-- INTRO STORY --") + "\n")
    print_tab("With the parcel signed for, and Courier on his way,")
    print_tab(char_name + " went back to " + pronoun1 + " very busy wrapping day.")
    print_tab("With the new delivery almost opened another distraction was at hand,")
    print_tab("From the living room a phone rang, completely unplanned. ")
    pause()

    clear_screen()
    printNew()
    print_tab(pr_colour("l_blue","-- INTRO STORY --") + "\n")
    print_tab("A call from an Auntie that put time off track, ")
    print_tab("Left our protagonist trying to pick up the slack.")
    print_tab("With last labels printed and hurriedly stuck on,")
    print_tab("It was time to go to bed and dream through until dawn.")
    pause()

    clear_screen()
    printNew()
    print_tab(pr_colour("l_blue","-- INTRO STORY --") + "\n")
    print_tab("Wrenched from a dream as a good bit drew near,")
    print_tab("By a rap on a door? Ah the Courier is here! ")
    print_tab("A swift hustle and bustle of parcels to van,")
    print_tab("and a thank you mince pie for the " + courier + ", delivery man.")
    pause()

    clear_screen()
    printNew()
    print_tab(pr_colour("l_blue","-- INTRO STORY --") + "\n")
    print_tab("Now time to relax with a good job well done. ")
    print_tab("Every last parcel away! But wait, what’s this one?")
    print_tab("With shock and surprise after slightest delay, ")
    print_tab("remembered was the unopened gift from yesterday.")
    pause()


    clear_screen()
    printNew()
    print_tab(pr_colour("l_blue","-- INTRO STORY --") + "\n")
    print_tab("With unwrapping the gift came confusion and shock,")
    print_tab("“This is the tea cosy and puzzle book for Great Uncle Jock?!”")
    print_tab("At once the error was clear as can be,")
    print_tab("“I’ve sent a parcel to him, that was meant for me!”")
    pause()

    clear_screen()
    printNew()
    print_tab(pr_colour("l_blue","-- INTRO STORY --") + "\n")
    print_tab("“That’s Christmas Ruined! I must get it on track!")
    print_tab("I must find a way to get that parcel back!”")
    print_tab("With fleetest of fingers and no time for delay,")
    print_tab("On to the " + courier + " website to try save the day!")
    pause()

    clear_screen()
    printNew()
    print_tab(pr_colour("l_blue","-- INTRO STORY --") + "\n")
    print_tab("A scuffle of papers on desk had unveiled,")
    print_tab("the tracking information of the gift wrongly mailed.")
    print_tab("On the " + courier + " website there was a pop-up you see,")
    print_tab("and with a click of ‘reject all cookies’ " + char_name + " thought “They’re not tracking me!”")
    pause()

    clear_screen()
    printNew()
    print_tab(pr_colour("l_blue","-- INTRO STORY --") + "\n")
    print_tab("With a quick search in the parcel tracking bar,")
    print_tab("an HTTP request was sent over the wire.")
    print_tab("Through to server, and thence a database,")
    print_tab("with information retrieved, the path was retraced. ")
    pause()

    clear_screen()
    printNew()
    print_tab(pr_colour("l_blue","-- INTRO STORY --") + "\n")
    print_tab("It popped up on the screen, the information was clear,")
    print_tab("The delivery van was headed to West Devonshire.")
    print_tab("As a local of sunny Weston-on-Trent, ")
    print_tab(char_name + " thought it was a strange place for the parcel to be sent.")
    pause()

    clear_screen()
    printNew()
    print_tab(pr_colour("l_blue","-- INTRO STORY --") + "\n")
    print_tab("With no time left for a return and resend,")
    print_tab(char_name + " found " + pronoun3 + "self at " + pronoun1 + " wits end!")
    print_tab("And then in a split second, an idea did appear,")
    print_tab("“I’ll go there, switch the parcel, then be in the clear!”")
    pause()

    clear_screen()
    printNew()
    print_tab(pr_colour("l_blue","-- INTRO STORY --") + "\n")
    print_tab("A Delivery Dilemma so hard to compound, ")
    print_tab("would require " + pronoun3 + " to put " + pronoun1 + " boots on the ground.")
    print_tab("With the solution to the problem not an easy one,")
    print_tab(char_name + "’s Christmas Adventure had just begun!")
    pause()

    clear_screen()
    printNew()
    ascii_del_dil()
    pause()
    
    clear_screen()
    printNew()
    print_tab(pr_colour("l_blue","-- THE BEGINNING --") + "\n")
    print_tab(char_name + " takes a long drive to the " + courier + " distribution centre in West Devonshire.")
    print_tab("There is a slight nip in the air as "+ pronoun2 +" parks on the street in front of ")
    print_tab("the building which is set a bit off the road. Briskly, "+ pronoun2 +" walks towards the entrance.")
    print_tab("Passing through the front door and entering the reception area. ")
    pause()

    contin = False
    while contin == False:
        clear_screen()
        printNew()
        print_tab(pr_colour("l_blue","-- INSTRUCTIONS --") + "\n")
        print_tab("- Your goal is to find Uncle Jock's Parcel. To do this you must gain access to and search different")
        print_tab("  parts of the building. \n")
        print_tab("- As you move from room to room you will see objects highlighted like " + pr_colour("l_blue","This") + ".")
        print_tab("  You can type these words to interact with the room or object highlighted.\n")
        print_tab("- Type " + pr_colour("l_blue","Help") + " anytime you see '>' for information on basic commands.\n\n")
        print_tab("Type " + pr_colour("l_blue","Ready") + " to continue.")
        var = san_input()
        
        
        if var == "ready":
            contin = True
            
        elif var == "help":
            
            clear_screen()
            printNew()
            print_tab(pr_colour("l_blue","-- HELP --")+"\n")
            print_tab("You can use the following options anytime you see the '>' character:\n")
            print_tab("back        - This will take you back out of the description you are in.\n")
            print_tab("map         - This will show you the map and where you are on it.\n")
            print_tab("objectives  - This will show a list of current objectives is.\n")    
            print_tab("who am i    - This will show you your characters name.\n")      
            print_tab("inventory   - This will list all the items you have.\n")
            print_tab("hint        - This will give you a hint for the location you are in.\n")  
            pause()
              
            
        else:
            print("")
            print_tab("Incorrect entry. Type 'Ready'")
            pause()
    
     
    
if __name__ == "__main__":
    #act_1_intro("Bob", "his", "he", "him", " UPS ")
    ascii_game_over()