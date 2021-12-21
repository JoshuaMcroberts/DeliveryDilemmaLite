from libraries import *
from mmap import Plan

class N_game:
    def __init__(self):
        self.player_name = ""
        self.number_plate = ""
        self.pc = Character()
        self.game_map = Plan()
        self.game_over = False
        self.sec_gar = True
        self.sec_gar_level = 0
        self.wait = 0
        self.preston = False
        self.courier = pr_colour("orange","Amazon")
        
    def set_player_name(self, p_name):
        self.player_name = pr_colour( "l_blue",p_name)
    
    def get_player_name(self):
        return self.player_name

    def set_num_plate(self, num_plate):
        self.number_plate = pr_colour("num_p", num_plate)
        
    def get_num_plate(self):
        return self.number_plate    
    
    def get_character(self):
        return self.pc
    
    def set_courier(self):
        # Courier Picker
        con_cat = len(self.player_name)*3
        cur_op = con_cat%4
        
        amazon = pr_colour("amazon", " A") + pr_colour("prime","maz")+ pr_colour("amazon","on Prime Delivery ") 
        fedex = pr_colour("fed", " Fed") + pr_colour("ex","Ex ")
        p_force = pr_colour("p_force", " Parcel Force ")
        ups = pr_colour("ups", " UPS ")
        
        cur_list = [amazon, fedex, ups, p_force]
        self.courier = cur_list[cur_op]
        # End Courier Picker
        
    def get_courier(self):
        return self.courier
       
    # ENTER PLAYER NAME - CHECK FOR NUMBER PLATE PLAYER
    def enter_name(self):
        
        tup_list = [("daniel"," PLATE1 "),("rebecca"," PLATE2 "),("andrew"," PLATE3 "),("joel"," PLATE4 "),("nathanael"," PLATE5 ")]
        
        correct = False
        while not correct:
            clear_screen()
            en_name = input("\tPlease enter your "+ pr_colour( "l_yellow","First Name") +": ")
            en_name = pr_colour("l_blue", en_name)
            
            
            val2 = False
            while not val2:
                clear_screen()
                print_tab("You have entered: " + en_name)
                val = input("\tIs this correct? (Y/N): ")
                
                if val == "Y":
                    correct = True
                    val2 = True
                elif val == "N":
                    correct = False
                    val2 = True
                else:
                    print()
                    print_tab("Enter Y for Yes or N for No")
                    pause()
        
        
        plate_name = san_text(en_name)
        
        num_plate = 0
        for name, num in tup_list:
            if plate_name == name:
                num_plate = num

        if num_plate == 0:
            num_plate = " REG MISSING "

        self.set_player_name(en_name)
        self.set_num_plate(num_plate)
    
    
    def create_char(self):
        name = self.enter_character_name()
        gen = self.enter_char_gender()
        self.pc = Character()
        self.pc.set_char_name(name)
        self.pc.set_pronouns(gen)
        
        
    # ENTER CHARACTER NAME    
    def enter_character_name(self):
        
        correct = False
        while not correct:
            clear_screen()
            character_name = input("\tPlease enter your "+ pr_colour( "l_yellow","Characters name") +": ")
            character_name = pr_colour("l_blue", character_name)
            
            
            val2 = False
            while not val2:
                clear_screen()
                print_tab("You have entered: " + character_name)
                val = input("\tIs this correct? (Y/N): ")
                
                if val == "Y":
                    correct = True
                    val2 = True
                elif val == "N":
                    correct = False
                    val2 = True
                else:
                    print()
                    print_tab("Enter Y for Yes or N for No")
                    pause()
        
        
        return character_name


    # ENTER CHARACTER GENDER
    def enter_char_gender(self):
        
        valid = False
        while not valid:
            clear_screen()
            gen = input("\tIs your Character {} or {}?: ".format(pr_colour("l_yellow", "male"), pr_colour("l_yellow","female")))
            gen = san_text(gen)
            
            if gen == "male" or gen == "female":
                valid = True
            else:
                print_tab("\n\tType MALE or FEMALE")
                pause()
        return gen
    
# CHARACTER CLASS
class Character:
    def __init__(self):
        self.inventory = ["Correct Parcel", ]
        self.gender = "Male"
        self.character_name = pr_colour("l_blue","Timmy")
        
        
    def set_char_name(self, c_name):
        self.character_name = pr_colour( "l_blue" , c_name )

    def get_char_name(self):
        return self.character_name
    
    def set_pronouns(self, gen):
        self.gender = gen
        
        if gen == "male":
            self.pronoun1 = "his"
            self.pronoun2 = "he"
            self.pronoun3 = "him"
        else:
            self.pronoun1 = "her"
            self.pronoun2 = "she"
            self.pronoun3 = "her"
    
    def get_pronouns(self):
        return self.pronoun1, self.pronoun2, self.pronoun3
    
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
        print_tab("\n\tCharacter Name: {}".format(self.character_name))
        print_tab("Gender: {}\n\tPronoun 1: {}\n\tPronoun 2: {}\n".format(self.gender, self.pronoun1, self.pronoun2))
        self.display_inventory()
