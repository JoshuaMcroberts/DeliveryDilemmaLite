from libraries import *
from game import N_game


def warehouse(game = N_game()):
    loop = True
    while loop:
        if(game.game_over == False):
            game.game_map.pre = game.game_map.player_enter((2,1),game.game_map.pre)   
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- WAREHOUSE --")+"\n")
            print_tab("The warehouse is a cavernous open space with concrete floors painted a pale blue colour.")
            print_tab("Red lines clearly mark out walk ways from fork lift drive paths. The warehouse appears to")
            print_tab("have been broken down into sections to the front of the warehouse there are two plastic ")
            print_tab("sheeting covered holes in the wall, the space behind them is clear however after that on")
            print_tab("the wall can be found the word " + pr_colour("l_blue", "Sorting Area") + ". Looking to the opposite side of the room")
            print_tab("you can see six smaller gaps in he wall covered by the same plastic sheeting as the others.")
            print_tab("The wall beside this area reads " + pr_colour("l_blue", "Loading Bay") + ". Next to you there is a desk that has been")
            print_tab("labelled " + pr_colour("l_blue", "Parcel Repair") + ". This seems to be were damaged parcels go when they need fixing. ")
            print_tab("The last feature of the warehouse is a window surround " + pr_colour("l_blue", "Office") + " in the near right hand corner. ")
            var = san_input()  
        
            # Navigation IF  
            if var  == "sortingarea":
                shelves(game)
            
            elif var == "parcelrepair":
                damaged_parcel_area(game)
                    
            elif var == "loadingbay":
                loading_bay(game)
                
            elif var == "office":
                office(game)
            
            else:
                hint = "Look around for Uncle Jock's Parcel"
                loop = game.basic_game_func(var, hint)
        else:
            loop = False
            
def shelves(game = N_game()):
    
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((2,0),game.game_map.pre)   
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- SORTING AREA --") + "\n")
        print_tab("The sorting area is broken down into postcodes and forwarding piles. Some to be shipped to other")
        print_tab("distribution centres and others to be delivered to the local area. In the forwarding section ")
        print_tab("there are a number of parcels to be sent however only four of them match the size of the parcel")
        print_tab("you are looking for. Have a look around at the parcels. You may need a " + pr_colour("l_blue","Hint") + " to start your search.")
        var, num = item_input()
    
        if str(type(num)) != "<class 'int'>":
            
            var = san_text(var + str(num))
        
        if var == "parcel" and num < 5 and num > 0:
            boxes(1 ,num, game)
        
        else:
            hint = "Type: Parcel 1 "
            loop = game.basic_game_func(var, hint)


def damaged_parcel_area(game = N_game()):
    
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((2,2),game.game_map.pre)   
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- PARCEL REPAIR STATION --") + "\n")
        print_tab("On the desk sits two parcels that seem a little worst for wear. The " + pr_colour("l_blue", "Parcel 1") + " seems to have")
        print_tab("been dropped as one of the corners has the characteristic signs of landing face first. ")
        print_tab(pr_colour("l_blue", "Parcel 2") + " seems to have been crashed by another parcel significantly heavier then if could ")
        print_tab("withstand. All around its side are the wrinkles in the cardboard formed when it buckled")
        print_tab("under the weight which also seems to have caused the corners to spilt.")
        var = san_input()
              
        if var == "parcel1":
            
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- PARCEL 1 --") + "\n")
            print_tab("The address label on the parcel reads:\n")
            print_tab("\t┌────────────────────┐")
            print_tab("\t│ Hollie Walker      │")
            print_tab("\t│ New Chester Road   │")
            print_tab("\t│ Ellesmere Port     │")
            print_tab("\t│ Cheshire           │")
            print_tab("\t│ CH66 1QW           │")
            print_tab("\t│ United Kingdom     │")
            print_tab("\t└────────────────────┘\n")
            print_tab("Not Uncle Jock's Parcel, Lets keep looking")
            pause()
            game.set_boxes(1)
            office_empty(game)
            
        elif var == "parcel2":
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- PARCEL 2 --") + "\n")
            print_tab("The address on this label appears to be ripped:\n")
            print_tab("\t           ─────────┐")
            print_tab("\t         _\Roberts  │")
            print_tab("\t        /raney Road │")
            print_tab("\t       __\derry     │")
            print_tab("\t      /rn           │")
            print_tab("\t     /JG            │")
            print_tab("\t    /ern Ireland    │")
            print_tab("\t   ─────────────────┘\n")
            print_tab("Not Uncle Jock's Parcel, Lets keep looking")
            pause()
            game.set_boxes(2)
            office_empty(game)
            
        else:
            hint = "Don't lick icy lamp posts"
            loop = game.basic_game_func(var, hint)
            
def loading_bay(game = N_game()):
    
    loop = True
    while loop:
        game.game_map.pre = game.game_map.player_enter((1,3),game.game_map.pre)   
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- LOADING BAY --") + "\n")
        print_tab("The loading bay has a fairly simple layout. A wheeled cage trolley can be easily wheeled from")
        print_tab("the sorting area to the smaller entrances which then allows for easy loading of the delivery")
        print_tab("vans when they are getting ready for their delivery runs. There is a single " + pr_colour("l_blue", "Roller Cage"))
        print_tab("sitting off to the side of one of the loading areas.")
        var = san_input()

        if var == "rollercage":
            rollercage(game)
        
        else:
            hint = "Don't lick icy lamp posts"
            loop = game.basic_game_func(var, hint)


def rollercage(game = N_game()):
    
    loop = True
    while loop:  
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- ROLLER CAGE --") + "\n")
        print_tab("Three parcel lie in an almost tower like structure in the bottom of the Roller Cage. Most of ")
        print_tab("the labels are obscured. You can take a closer look at each parcel to see its shipping label.")
        print_tab("You may need a " + pr_colour("l_blue","Hint") + " to start your search.")
        var, num = item_input()

        if str(type(num)) != "<class 'int'>":
            
            var = san_text(var + str(num))

        if var == "parcel" and num <4 and num > 0:
            boxes( 2 ,num, game)
        
        else:
            hint = "Type: Parcel 1 "
            loop = game.basic_game_func(var, hint)


def office(game = N_game()):
    
    loop = True
    while loop:
        if(game.game_over == False):
            game.game_map.pre = game.game_map.player_enter((0,3),game.game_map.pre)   
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- WAREHOUSE OFFICE --") + "\n")
            
            if game.worker == True:
                print_tab("As you get closer to the office you see there is someone inside it. They would recognise ")
                print_tab("instantly that you weren't supposed to be here. You best search elsewhere until they leave. ")
                pause()
                loop = False
            else:
                print_tab("You enter the office and find cluttered space. On a table in the back of the room semi-ordered ")
                print_tab("stacks of paper climb the wall. Three of the four sides of the boxy room have glass windows ")
                print_tab("that span the length of the side. The bottom edges of the window frames are coated with a thin")
                print_tab("layer of dust which appears to have been disturbed in places where people have lent against it.")
                print_tab("On a table that faces into the warehouse sits a " + pr_colour("l_blue","Computer") + " with it password and username handily")
                print_tab("stored on a post-it note stuck to the top left-hand corner of the screen. ")
                var = san_input()

                if var == "computer":
                    computer(game)
                
                else:
                    hint = "Don't lick icy lamp posts"
                    loop = game.basic_game_func(var, hint)
        else:
            loop = False
       

def computer(game = N_game()):
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- COMPUTER --")+"\n")
    print_tab("You unlock the computer to find a parcel management system loaded on the screen. On the display ")
    print_tab("different numbers show how many parcels will be shipped to each of the surrounding towns. ")
    s_pause()
    
    print_tab("You select the search function and enter the tracking number of Uncle Jocks parcel.")
    s_pause()
    
    print_tab("An incorrect value error appears on the screen and then blinks out.")
    s_pause()
    
    print_tab("You try entering the parcel ID number and immediately an item record opens up.")
    s_pause()
    
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- PARCEL RECORD --") + "\n")
    print_tab("┌──────────────────────────────────────────────────────────────┐")
    print_tab("│ Parcel Number:    B42 8472 3189 6439 10                      │")
    print_tab("│                                                              │")
    print_tab("│ Tracking Number:  A2K6U9-2893-G2GU96                         │")
    print_tab("│                                                              │")
    print_tab("│ Delivery Address: Jock Thistlewaite Angus MacTavish III      │")
    print_tab("│                   3 Pennyworth Rd                            │")
    print_tab("│                   Aderfeldy                                  │")
    print_tab("│                   Perthshire                                 │")
    print_tab("│                   BXA2XW                                     │")
    print_tab("│                                                              │")
    print_tab("│ Delivery Date:    Tomorrow - 24/12/2021                      │")
    print_tab("│                                                              │")
    print_tab("│ Current Location: In Vehicle for delivery                    │")
    print_tab("└──────────────────────────────────────────────────────────────┘")
    pause()
    
    
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- COMPUTER --")+"\n")
    print_tab("After skimming over the details you realise that the parcel in no longer in the warehouse but ")
    print_tab("instead in a vehicle waiting to be delivered.")
    s_pause()
    
    print_tab("You select the Current Location field and a vehicle record opens.")
    s_pause()
    
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- VEHICLE RECORD --") + "\n")
    print_tab("┌───────────────────────────────┐")
    print_tab("│ Vehicle ID:    00001372       │")
    # print_tab("│                               │")
    print_tab("│ Driver Name:   Sidney         │")
    print_tab("│ Miles:         100,263        │")
    print_tab("│                               │")
    print_tab("│ Serviced Last: 30/09/2021     │")
    print_tab("│ MOT due:       22/01/2022     │")
    print_tab("│                               │")
    print_tab("│ REG:          " + game.unformated_plate + "      │")
    print_tab("└───────────────────────────────┘")
    pause()
    
    clear_screen()
    print("")
    print_tab(pr_colour("l_blue","-- COMPUTER --")+"\n")
    print_tab("You now have the vehicle information. "+ game.player_name +" it is up to you! ")
    s_pause()
    
    game.set_new_ob("Find Uncle Jock's Parcel in the Vehicle with the REG: " + game.number_plate )
    
    s_pause()
    loop = True
    while loop:
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- COMPUTER --")+"\n")
        print_tab("Did you find Uncle Jock's parcel in the delivery vehicle? Type YES to continue.")
        var = san_input()

        if var == "yes":
            loop = False

        elif var == "hint":
            print("")
            hint = "Call the game maker if you can't find the"
            print("\tHint -", end="")                                                                         
            print_tab(hint)
            pause()
             
        else:
            print("")
            print_tab("Incorrect entry try again")
            pause()
    
    game.game_over = True
    
    
    
def boxes( opt , num, game = N_game() ):
    
    if opt == 1:
        
        if num == 1 :
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- PARCEL "+ str(num) +" --") + "\n")
            print_tab("The address label on the parcel reads:\n")
            print_tab("\t┌────────────────────┐")
            print_tab("\t│ Bradley Reid       │")
            print_tab("\t│ 25 Terrace Rd      │")
            print_tab("\t│ Aberystwyth        │")
            print_tab("\t│ Dyfed              │")
            print_tab("\t│ SY23 1NP           │")
            print_tab("\t│ United Kingdom     │")
            print_tab("\t└────────────────────┘\n")
            print_tab("Not Uncle Jock's Parcel, Lets keep looking")
            pause()
            game.set_boxes(3)
                    

        elif num == 2:
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- PARCEL "+ str(num) +" --") + "\n")
            print_tab("The address label on the parcel reads:\n")
            print_tab("\t┌────────────────────┐")
            print_tab("\t│ Mark Powell        │")
            print_tab("\t│ 8 Lynwood Close    │")
            print_tab("\t│ Ashton-under-Lyne  │")
            print_tab("\t│ Tameside           │")
            print_tab("\t│ OL7 9SS            │")
            print_tab("\t│ United Kingdom     │")
            print_tab("\t└────────────────────┘\n")
            print_tab("Not Uncle Jock's Parcel, Lets keep looking")
            pause()
            game.set_boxes(4)
                        
        elif num == 3:
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- PARCEL "+ str(num) +" --") + "\n")
            print_tab("The address label on the parcel reads:\n")
            print_tab("\t┌────────────────────┐")
            print_tab("\t│ Mandy Matthews     │")
            print_tab("\t│ College Green      │")
            print_tab("\t│ Bristol            │")
            print_tab("\t│ City of Bristol    │")
            print_tab("\t│ BS1 5TA            │")
            print_tab("\t│ United Kingdom     │")
            print_tab("\t└────────────────────┘\n")
            print_tab("Not Uncle Jock's Parcel, Lets keep looking")
            pause()
            game.set_boxes(5)
                        
        elif num == 4:
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- PARCEL "+ str(num) +" --") + "\n")
            print_tab("The address label on the parcel reads:\n")
            print_tab("\t┌────────────────────┐")
            print_tab("\t│ Bethany Hunt       │")
            print_tab("\t│ 56 Hambro Hill     │")
            print_tab("\t│ Rayleigh           │")
            print_tab("\t│ Essex              │")
            print_tab("\t│ SS6 8BW            │")
            print_tab("\t│ United Kingdom     │")
            print_tab("\t└────────────────────┘\n")
            print_tab("Not Uncle Jock's Parcel, Lets keep looking")
            pause()
            game.set_boxes(6)
        office_empty(game)
    else:
        if num == 1 :
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- PARCEL "+ str(num) +" --") + "\n")
            print_tab("The address label on the parcel reads:\n")
            print_tab("\t┌────────────────────┐")
            print_tab("\t│ Donna Reynolds     │")
            print_tab("\t│ 27 Manor Way       │")
            print_tab("\t│ Borehamwood        │")
            print_tab("\t│ Hertfordshire      │")
            print_tab("\t│ WD6 1QJ            │")
            print_tab("\t│ United Kingdom     │")
            print_tab("\t└────────────────────┘\n")
            print_tab("Not Uncle Jock's Parcel, Lets keep looking")
            pause()
            game.set_boxes(7)
 
        elif num == 2:
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- PARCEL "+ str(num) +" --") + "\n")
            print_tab("The address label on the parcel reads:\n")
            print_tab("\t┌────────────────────┐")
            print_tab("\t│ Yvonne Price       │")
            print_tab("\t│ 15-16 High St      │")
            print_tab("\t│ Swansea            │")
            print_tab("\t│ Glamorgan          │")
            print_tab("\t│ SA1 1LF            │")
            print_tab("\t│ United Kingdom     │")
            print_tab("\t└────────────────────┘\n")
            print_tab("Not Uncle Jock's Parcel, Lets keep looking")
            pause()
            game.set_boxes(8)
       
        elif num == 3:
            clear_screen()
            print("")
            print_tab(pr_colour("l_blue","-- PARCEL "+ str(num) +" --") + "\n")
            print_tab("The address label on the parcel reads:\n")
            print_tab("\t┌────────────────────┐")
            print_tab("\t│ David Graham       │")
            print_tab("\t│ 14 St Thomas Rd    │")
            print_tab("\t│ Brentwood          │")
            print_tab("\t│ Essex              │")
            print_tab("\t│ CM14 4DB           │")
            print_tab("\t│ United Kingdom     │")
            print_tab("\t└────────────────────┘\n")
            print_tab("Not Uncle Jock's Parcel, Lets keep looking")
            pause()
            game.set_boxes(9)
        office_empty(game)

def office_empty(game = N_game()):
    empty = game.check_boxes()
    if empty == True:
        clear_screen()
        print("")
        print_tab(pr_colour("l_blue","-- SEARCHING --") + "\n")
        print_tab("As you set down the parcel you are looking at you glance across the warehouse to the office.")
        print_tab("You notice the worker that was in the office has left it and is heading out the door to the ")
        print_tab("main building. Now is your chance to have a look inside.")
        game.set_new_ob("Search the Office")
        game.worker = False
        pause()
            

if __name__ == "__main__":
    game = N_game()
    game.set_num_plate(" KLZ 9890 ")
    # computer(game)
    warehouse(game)