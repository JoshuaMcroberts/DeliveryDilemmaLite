from libraries import *
from m_map import Plan

class N_game:
    def __init__(self):
        self.player_name = ""
        self.number_plate = ""
        self.unformated_plate = ""
        self.pc = Character()
        self.game_map = Plan()
        self.game_over = False
        self.sec_gar = True
        self.sec_gar_level = 0
        self.wait = 0
        self.preston = False
        self.courier = pr_colour("orange","Amazon")
        self.locker_21_empty = False
        self.got_key = False
        self.get_key = False
        self.objectives = []
        self.boxes=[False, False, False, False, False, False, False, False, False]
        self.time_changed = False
        self.called = False 
        self.worker = True
        self.recep = pr_colour("pink","Receptionist")
        self.full_bin = False
        
    
    def set_boxes(self,box):
        box = box - 1
        self.boxes[box] = True
    
    def check_boxes(self):
        count = 0
        for box in self.boxes:
            if box == True:
                count = count + 1
        
        if count > 6 :
            return True
        else:
            return False
        
    def basic_game_func(self, var, hint):
        
        if var == "back":
            return False

        elif var == "map":
            clear_screen()
            self.game_map.print_map()
            pause()
            return True  
            
        elif var == "objectives":
            clear_screen()
            printNew()
            print_tab("-- CURRENT OBJECTIVES --\n")
            self.display_ob_list()
            pause()
            return True  
            
        elif var == "whoami":
            print("")
            print_tab("You are " + self.pc.character_name)
            pause()
            return True  
        
        elif var == "inventory":
            clear_screen()
            self.pc.display_inventory()
            pause()
            return True  
        
        elif var == "state":
            clear_screen()
            self.display_game_state()
            pause()
            return True  
            
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
            return True  
        
        elif var == "hint":
            print("")
            print("\t\tHint -", end="")                                                                         
            print_tab(hint)
            pause()
            return True 
        
        else:
            print("")
            print_tab("Incorrect entry try again")
            pause()
            return True  
    
    def set_new_ob(self, objective):
        self.objectives.append(objective)
        print("")
        print(pr_colour("l_green","\t\tNew Objective Added: \t" + objective))
        
    def display_cur_ob(self):
        ob = self.objectives[-1]
        print_tab(ob)
        
    def display_ob_list(self):

        for ob in reversed(self.objectives):
           print_tab(pr_colour("l_green", "- " + ob + "\n")) 
    
    def check_ob(self, objective):
        check = False
        for ob in self.objectives:
            if ob == objective:
                check = True
        
        return check
    
    def completed_cur_ob(self):
        objective = self.objectives.pop()
        print("")
        print(pr_colour("l_green","\t\tObjective Completed: \t" + objective))
        
    def completed_spec_ob(self, objective):
        for ob in self.objectives:
            if ob == objective:
                ind = self.objectives.index(objective)
                self.objectives.pop(ind)
        print("")
        print(pr_colour("l_green","\t\tObjective Completed: \t" + objective))
                
    def set_player_name(self, p_name):
        self.player_name = pr_colour( "l_blue",p_name)
    
    def get_player_name(self):
        return self.player_name

    def set_num_plate(self, num_plate, nationality):
         
        if nationality == "us":
            self.number_plate = pr_colour("us_num_p", num_plate)
        else:
            self.number_plate = pr_colour("num_p", num_plate)
              
        self.unformated_plate = num_plate
        
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
        
        tup_list = [("daniel"," R44 REP ", "uk"),("rebecca"," FX05 YAJ ", "uk"),("andrew"," KLZ 9890 ", "uk"),("joel"," T229 RGP ", "uk"),("nathanael"," PLZ 8101 ", "uk"),("caroline"," JKZ" + u'\xB7'+ "8620 ", "us")]
        
        correct = False
        while not correct:
            clear_screen()
            printNew()
            print_tab(pr_colour("l_blue","-- GAME SETUP--") + "\n")
            en_name = input("\tPlease enter your "+ pr_colour( "l_yellow","First Name") +": ")
            plate_name = san_text(en_name)
            en_name = pr_colour("l_blue", en_name)
            
            
            val2 = False
            while not val2:
                clear_screen()
                printNew()
                print_tab(pr_colour("l_blue","-- GAME SETUP--") + "\n")
                print_tab("You have entered: " + en_name)
                val = input("\tIs this correct? (Y/N): ")
                
                val = san_text(val)
                
                if val == "y":
                    correct = True
                    val2 = True
                elif val == "n":
                    correct = False
                    val2 = True
                else:
                    print()
                    print_tab("Enter Y for Yes or N for No")
                    pause()
                
        num_plate = 0
        for name, num, nationality in tup_list:
            if plate_name == name:
                num_plate = num

        if num_plate == 0:
            num_plate = " HJW 8264 "

        self.set_player_name(en_name)
        self.set_num_plate(num_plate, nationality)
    
    
    def create_char(self):
        name = self.enter_character_name()
        gen = self.enter_char_gender()
        self.pc = Character()
        self.pc.set_char_name(name)
        self.pc.set_pronouns(gen)
        
    def display_game_state(self):
        clear_screen()
        print_tab("__ GAME STATE __")
       
        print_tab("Preston           : " + str(self.preston))
        print_tab("Sec Guard         : " + str(self.sec_gar ))
        print_tab("Time Changed      : " + str(self.time_changed))
        print_tab("Phone call        : " + str(self.called))
        print_tab("Bin Full          : " + str(self.full_bin ))
       
        print_tab("Got Key           : " + str(self.got_key))
        print_tab("Locker 21         : " + str(self.locker_21_empty))
        print_tab("Boxes             : " + str(self.boxes))
        print_tab("Game Over         : " + str(self.game_over))
 
        print_tab("Sec Guard Ang     : " + str(self.sec_gar_level))
        print_tab("Wait              : " + str(self.wait))
        
        print_tab("\n\t__ PLAYER INFO __")
        print_tab("Player Name       : " + str(self.player_name))
        print_tab("Number Plate      : " + str(self.number_plate))
        print_tab("Number Plate Unfor: " + str(self.unformated_plate))
        print_tab("Courier           : " + str(self.courier))
        
        print_tab("\n\t__ CHARACTER INFO __")
        print_tab("Character Name    : " + str(self.pc.character_name))
        print_tab("Char Name         : " + str(self.pc.char_name))
        print_tab("Gender            : " + str(self.pc.gender ))
        print_tab("Pro 1             : " + str(self.pc.pronoun1))
        print_tab("Pro 2             : " + str(self.pc.pronoun2))
        print_tab("Pro 3             : " + str(self.pc.pronoun3))
        print_tab("Title             : " + str(self.pc.title))
        print_tab("Preston First     : " + str(self.pc.p_name))
        self.pc.display_inventory()
        self.display_ob_list()
        
       
    # ENTER CHARACTER NAME    
    def enter_character_name(self):
        
        correct = False
        while not correct:
            clear_screen()
            printNew()
            print_tab(pr_colour("l_blue","-- GAME SETUP --") + "\n")
            character_name = input("\tPlease enter your "+ pr_colour( "l_yellow","Characters name") +": ")
                       
            
            val2 = False
            while not val2:
                clear_screen()
                printNew()
                print_tab(pr_colour("l_blue","-- GAME SETUP --") + "\n")
                print_tab("You have entered: " + pr_colour("l_blue", character_name))
                val = input("\tIs this correct? (Y/N): ")
                
                val = san_text(val)
                
                if val == "y":
                    correct = True
                    val2 = True
                elif val == "n":
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
            printNew()
            print_tab(pr_colour("l_blue","-- GAME SETUP --") + "\n")
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
        self.char_name = "Timmy"
        
        
    def set_char_name(self, c_name):
        self.character_name = pr_colour( "l_blue" , c_name )
        self.char_name = c_name

    def get_char_name(self):
        return self.character_name
    
    def set_pronouns(self, gen):
        self.gender = gen
        
        if gen == "male":
            self.pronoun1 = "his"
            self.pronoun2 = "he"
            self.pronoun3 = "him"
            self.title = "Mr"
            self.p_name = "James"
            self.bi_gen = "man"
        else:
            self.pronoun1 = "her"
            self.pronoun2 = "she"
            self.pronoun3 = "her"
            self.title = "Miss"
            self.p_name = "Gina"
            self.bi_gen = "woman"
    
    def get_pronouns(self):
        return self.pronoun1, self.pronoun2, self.pronoun3
    
    def add_inventory(self, item):
        self.inventory.append(item)
        print_tab(pr_colour("yellow","\n\t+1 [{}] has been added to your inventory".format(item)))

    def remove_inventory(self, item):
        try:
            ind = self.inventory.index(item)
            use_item = self.inventory.pop(ind)
        except:
            print_tab("(No such item in your Inventory)")
            use_item = False
        finally:
            return use_item

    def check_inventory(self, item_name):
        check = False
        for item in self.inventory:
            if item == item_name:
                check = True
        
        return check

    def display_inventory(self):
        printNew()
        print_tab("-- INVENTROY --\n")
        if len(self.inventory) > 0:

            for item in self.inventory:
                print_tab(pr_colour("yellow","- " + item + "\n"))
            
        else:
            print_tab("Inventory is empty")
           

    def print_all(self):
        clear_screen()
        print_tab("\n\tCharacter Name: {}".format(self.character_name))
        print_tab("Gender: {}\n\tPronoun 1: {}\n\tPronoun 2: {}\n".format(self.gender, self.pronoun1, self.pronoun2))
        self.display_inventory()
