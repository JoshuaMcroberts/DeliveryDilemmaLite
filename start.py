from libraries import *
from text import *

class character:
    def __init__(self, play_name, char_name, num_plate, gen):
        self.player_name = play_name
        self.character_name = char_name
        self.number_plate = num_plate
        self.inventory = []
        self.gender = gen
         " + pr_colour(2, courier) + " 
        if gen == "male":
            self.pronoun1 = "his"
            self.pronoun2 = "he"
        else:
            self.pronoun1 = "her"
            self.pronoun2 = "she"
            
        con_cat = play_name + char_name + num_plate + gen
        
        cur_op = len(con_cat)%8
        
        # unself this.
        cur_list = [pr_colour(1, "Parcel Force"), pr_colour(4, "FedEx"), pr_colour(2, "Amazon Prime Delivery"), pr_colour(3, "UPS"), 
                         pr_colour(1, "Parcel Force"), pr_colour(4, "FedEx"), pr_colour(2, "Amazon Prime Delivery"), pr_colour(3, "UPS") ]
        
        self.courier = cur_list[cur_op]
        
        
    def set_char_name(self, c_name):
        self.character_name = c_name

    def get_char_name(self):
        return self.character_name

    def set_player_name(self, p_name):
        self.player_name = p_name

    def get_player_name(self):
        return self.player_name

    def set_num_plate(self, num_plate):
        self.number_plate = num_plate

    def get_num_plate(self):
        return self.number_plate
    
    def get_pronouns(self):
        return self.pronoun1, self.pronoun2
    
    def get_courier(self):
        return self.courier
    
    def add_inventory(self, item):
        self.inventory.append(item)
        print_tab("{} has been added to your inventory".format(item))

    def remove_inventory(self, item):
        try:
            ind = self.inventory.index(item)
            use_item = self.inventory.pop(ind)
        except:
            print_tab("(No such item in your Inventory)")
            use_item = False
        finally:
            return use_item

    def display_inventory(self):
        print_tab("INVENTROY")
        if len(self.inventory) > 0:

            for item in self.inventory:
                print_tab(pr_colour(2,item))
            pause()
        else:
            print_tab("Inventory is empty")
            pause()

    def print_all(self):
        clear_screen()
        print_tab("\n\tPlayer Name: {}\n\tCharacter Name: {}\n\tNumber Plate: {}".format(self.player_name, self.character_name, self.number_plate))
        print_tab("Gender: {}\n\tPronoun 1: {}\n\tPronoun 2: {}\n".format(self.gender, self.pronoun1, self.pronoun2))
        self.display_inventory()

def san_text(text):
    text = text.lower()
    text = text.strip()
    return text

def enter_name():
    clear_screen()
    tup_list = [("daniel","PLATE1"),("rebecca","PLATE2"),("andrew","PLATE3"),("joel","PLATE4"),("nathanael","PLATE5")]
    en_name = input("\tPlease enter your "+ pr_colour( 3,"First Name") +": ")
    plate_name = san_text(en_name)
    
    num_plate = 0
    for name, num in tup_list:
        if plate_name == name:
            num_plate = num

    if num_plate == 0:
        num_plate = "REG MISSING"

    return en_name, num_plate
    
def enter_character_name():
    clear_screen()
    character_name = input("\tPlease enter your "+ pr_colour( 3,"Characters name") +": ")
    return character_name

def enter_char_gender():
    
    valid = False
    while not valid:
        clear_screen()
        gen = input("\tIs your Character {} or {}?: ".format(pr_colour(3, "MALE"), pr_colour(3,"FEMALE")))
        gen = san_text(gen)
        
        if gen == "male" or gen == "female":
            valid = True
        else:
            print_tab("\n\tType MALE or FEMALE")
            pause()
    
    return gen
     

def help_text():
    clear_screen()
    print_tab("Help text will go here!")


def about_text():
    clear_screen()
    print_tab("About text will go here!")

def game_intro():
    print_tab("Delviery Dilemma\n")

def game():
    clear_screen()
    # print_tab("Character Set Up\n")
    # pause()
    p_name, num_p = enter_name()
    c_name = enter_character_name()
    c_gen = enter_char_gender()

    pc = character(p_name, c_name, num_p, c_gen)
    # pc.print_all()
    # pause()
    pause()
    
    char_name = pc.get_char_name()
    pro_1, pro_2 = pc.get_pronouns()
    cur = pc.get_courier()
    
    # Game Intro
    act_1_intro(char_name, pro_1, pro_2, cur) " + pr_colour(2, courier) + " 

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
            game()
        elif main_op == 2:
            help_text()
            pause()
        elif main_op == 3:
            about_text()
            pause()
        elif main_op == 4:
            print_tab(pr_colour(4,"Bye Bye"))
           
            ext = True
        else:
            print_tab("Select a Number from 1-4")
            pause()

  
if __name__ == "__main__":
    main()
    # game()
