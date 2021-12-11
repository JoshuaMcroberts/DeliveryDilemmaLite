from libraries import *
from start import character

def act_1_intro(chac_name, pronoun1, pronoun2, courier):
      
    clear_screen()
    print_tab("It was the night before the delivery deadline before Christmas and all through the house,")
    print_tab("was heard the soft clicking and whirring of printer and mouse.")
    print_tab("Parcels lay strewn in every which way,")
    print_tab("with wrapping paper and packaging all on display.")
    pause()

    clear_screen()
    print_tab("The rush was on for the Christmas deadline you see")
    print_tab("and " + pr_colour( 4, chac_name) + " had left the parcel packing until after " + pronoun1 + " tea.")
    print_tab("Each box for a friend would be stacked by the stair,")
    print_tab("In hopes that in the morning " + courier + " would be there.")
    pause()
    
    clear_screen()
    print_tab("In the midst of the chaos the doorbell did ring, ")
    print_tab("“Who could that be?” " + pr_colour( 4, chac_name) + " thought as " + pronoun2 + " tied up a string.")
    print_tab("It was a late-night delivery of something unknown,")
    print_tab("Could be a book or a beagle or an old-style gramophone?")
    pause()

    clear_screen()
    print_tab("With the parcel signed for, and courier on his way,")
    print_tab("" + pr_colour( 4, chac_name)+ " went back to " + pronoun1 + " busy wrapping day.")
    print_tab("With the new delivery almost opened another distraction was at hand,")
    print_tab("From the living room a phone rang, completely unplanned. ")
    pause()


    clear_screen()
    print_tab("A call from an Auntie that put time off track, ")
    print_tab("Left our protagonist trying to pick up the slack.")
    print_tab("With last labels printed and hurriedly stuck on,")
    print_tab("It was time to go to bed and dream through until dawn.")
    pause()

    clear_screen()
    print_tab("Wrenched from a dream as a good bit drew near,")
    print_tab("By a rap on a door? Ah the Courier is here! ")
    print_tab("A swift hustle and bustle of parcels to van,")
    print_tab("and a thank you mince pie for the " + courier + ", delivery man.")
    pause()

    clear_screen()
    print_tab("Now time to relax with a good job well done. ")
    print_tab("Every last parcel away! But wait, what’s this one?")
    print_tab("With shock and surprise after slightest delay, ")
    print_tab("remembered was the unopened gift from yesterday.")
    pause()


    clear_screen()
    print_tab("With unwrapping the gift came confusion and shock,")
    print_tab("“This is the tea cosy and puzzle book for Great Uncle Jock?!”")
    print_tab("At once the error was clear as can be,")
    print_tab("“I’ve sent a parcel to him, that was meant for me!”")
    pause()


if __name__ == "__main__":
    act_1_intro("Bob", "his", "he")