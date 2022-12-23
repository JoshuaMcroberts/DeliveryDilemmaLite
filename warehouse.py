from libraries import *
from game import N_game


def warehouse(game = N_game()):
    loop = True
    while loop:
        if(game.game_over == False):
            game.game_map.pre = game.game_map.player_enter((2,1),game.game_map.pre)   
            clear_screen()
            printNew()
            print_tab(pr_colour("l_blue","-- WAREHOUSE --")+"\n")
            print_tab("The warehouse is a cavernous open space with concrete floors painted a pale blue colour.")
            print_tab("Red lines clearly mark out walkways from fork lift drive paths. The warehouse appears to")
            print_tab("have been broken down into sections. To the front of the warehouse there are two plastic-")
            print_tab("sheeting, covered holes in the wall. The space behind them is clear, however after that on")
            print_tab("the wall can be found the word " + pr_colour("l_blue", "Sorting Area") + ". Looking to the opposite side of the room")
            print_tab("you can see six smaller gaps in the wall covered by the same plastic sheeting as the others.")
            print_tab("The wall beside this area reads " + pr_colour("l_blue", "Loading Bay") + ". Next to you there is a desk that has been")
            print_tab("labelled " + pr_colour("l_blue", "Parcel Repair") + ". This seems to be where damaged parcels go when they need fixing. ")
            print_tab("The last feature of the warehouse is a window surrounded " + pr_colour("l_blue", "Office") + " in the near right hand corner. ")
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
        printNew()
        print_tab(pr_colour("l_blue","-- SORTING AREA --") + "\n")
        print_tab("The sorting area is broken down into postcodes and forwarding piles. Some to be shipped to ")
        print_tab("other distribution centres and others to be delivered to the local area. In the forwarding  ")
        print_tab("section there are a number of parcels to be sent however only four of them match the size of ")
        print_tab("the parcel you are looking for. Have a look around at the parcels. You may need a " + pr_colour("l_blue","Hint") + " to ")
        print_tab("start your search.")
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
        printNew()
        print_tab(pr_colour("l_blue","-- PARCEL REPAIR STATION --") + "\n")
        print_tab("On the desk sit two parcels that seem a little worse for wear. " + pr_colour("l_blue", "Parcel 1") + " seems to have")
        print_tab("been dropped as one of the corners has the characteristic signs of landing face first. ")
        print_tab(pr_colour("l_blue", "Parcel 2") + " seems to have been crushed by another parcel that was significantly heavier then ")
        print_tab("it could withstand. All around its side are the wrinkles in the cardboard formed when it ")
        print_tab("buckled under the weight which also seems to have caused the corners to split.")
        var = san_input()
              
        if var == "parcel1":
            
            clear_screen()
            printNew()
            print_tab(pr_colour("l_blue","-- PARCEL 1 --") + "\n")
            print_tab("The address label on the parcel reads:\n")
            print_tab("\t┌───────────────────────┐")
            print_tab("\t│ F Flintstone          │")
            print_tab("\t│ 342 Gravelpit Terrace │")
            print_tab("\t│ Bedrock               │")
            print_tab("\t│ ST0N EDR              │")
            print_tab("\t│ Unknown               │")
            print_tab("\t└───────────────────────┘\n")
            print_tab("Not Uncle Jock's Parcel, Let's keep looking")
            pause()
            game.set_boxes(1)
            office_empty(game)
            
        elif var == "parcel2":
            clear_screen()
            printNew()
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
            print_tab("Not Uncle Jock's Parcel, Let's keep looking")
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
        printNew()
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
        printNew()
        print_tab(pr_colour("l_blue","-- ROLLER CAGE --") + "\n")
        print_tab("Three parcels lie in an almost tower like structure in the bottom of the Roller Cage. Most of ")
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
            printNew()
            print_tab(pr_colour("l_blue","-- WAREHOUSE OFFICE --") + "\n")
            
            if game.worker == True:
                print_tab("As you get closer to the office you see there is someone inside it. They would recognise ")
                print_tab("instantly that you weren't supposed to be here. You best search elsewhere until they leave. ")
                pause()
                loop = False
            else:
                print_tab("You enter the office and find a cluttered space. On a table in the back of the room semi-ordered ")
                print_tab("stacks of paper climb the wall. Three of the four sides of the boxy room have glass windows ")
                print_tab("that span the length of the side. The bottom edges of the window frames are coated with a thin")
                print_tab("layer of dust which appears to have been disturbed in places where people have lent against it.")
                print_tab("On a table that faces into the warehouse sits a " + pr_colour("l_blue","Computer") + " with its password and username handily")
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
    printNew()
    print_tab(pr_colour("l_blue","-- COMPUTER --")+"\n")
    print_tab("You unlock the computer to find a parcel management system loaded on the screen. On the  ")
    print_tab("display different numbers show how many parcels will be shipped to each of the surrounding  ")
    print_tab("towns.")
    s_pause()
    
    print_tab("You select the search function and enter the tracking number of Uncle Jocks parcel.")
    s_pause()
    
    print_tab("An incorrect value error appears on the screen and then blinks out.")
    s_pause()
    
    print_tab("You try entering the parcel ID number and immediately an item record opens up.")
    s_pause()
    
    clear_screen()
    printNew()
    print_tab(pr_colour("l_blue","-- PARCEL RECORD --") + "\n")
    print_tab("┌──────────────────────────────────────────────────────────────┐")
    print_tab("│ Parcel Number:    B42 8472 3189 6439 10                      │")
    print_tab("│                                                              │")
    print_tab("│ Tracking Number:  A2K6U9-2893-G2GU96                         │")
    print_tab("│                                                              │")
    print_tab("│ Delivery Address: Jock Thistlewaite Angus MacTavish III      │")
    print_tab("│                   3 Pennyworth Rd                            │")
    print_tab("│                   Aberfeldy                                  │")
    print_tab("│                   Perthshire                                 │")
    print_tab("│                   BXA2XW                                     │")
    print_tab("│                                                              │")
    print_tab("│ Delivery Date:    Tomorrow - 24/12/2022                      │")
    print_tab("│                                                              │")
    print_tab("│ Current Location: In Vehicle for delivery                    │")
    print_tab("└──────────────────────────────────────────────────────────────┘")
    pause()
    
    
    clear_screen()
    printNew()
    print_tab(pr_colour("l_blue","-- COMPUTER --")+"\n")
    print_tab("After skimming over the details you realise that the parcel is no longer in the warehouse ")
    print_tab("but instead is in a vehicle waiting to be delivered.")
    s_pause()
    
    print_tab("You select the Current Location field and a vehicle record opens.")
    s_pause()
    
    clear_screen()
    printNew()
    print_tab(pr_colour("l_blue","-- VEHICLE RECORD --") + "\n")
    print_tab("┌───────────────────────────────┐")
    print_tab("│ Vehicle ID:    00001372       │")
    # print_tab("│                               │")
    print_tab("│ Driver Name:   Sidney         │")
    print_tab("│ Miles:         100,263        │")
    print_tab("│                               │")
    print_tab("│ Serviced Last: 30/09/2022     │")
    print_tab("│ MOT due:       19/01/2023     │")
    print_tab("│                               │")
    print_tab("│ REG:          " + game.unformated_plate + "      │")
    print_tab("└───────────────────────────────┘")
    pause()
    
    clear_screen()
    printNew()
    print_tab(pr_colour("l_blue","-- COMPUTER --")+"\n")
    print_tab("You now have the vehicle information. "+ game.player_name +" it is up to you! ")
    s_pause()
    
    game.set_new_ob("Find Uncle Jock's Parcel in a Vehicle with REG: "+'\033[00m' + game.number_plate )
    
    s_pause()
    loop = True
    while loop:
        clear_screen()
        printNew()
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
            printNew()
            print_tab(pr_colour("l_blue","-- PARCEL "+ str(num) +" --") + "\n")
            print_tab("The address label on the parcel reads:\n")
            print_tab("\t┌────────────────────┐")
            print_tab("\t│ J Watson           │")
            print_tab("\t│ 221b Baker St      │")
            print_tab("\t│ London             │")
            print_tab("\t│ NW1 6XE            │")
            print_tab("\t│ United Kingdom     │")
            print_tab("\t└────────────────────┘\n")
            print_tab("Not Uncle Jock's Parcel, Let's keep looking")
            pause()
            game.set_boxes(3)
                    

        elif num == 2:
            clear_screen()
            printNew()
            print_tab(pr_colour("l_blue","-- PARCEL "+ str(num) +" --") + "\n")
            print_tab("The address label on the parcel reads:\n")
            print_tab("\t┌─────────────────────┐")
            print_tab("\t│ M Banks             │")
            print_tab("\t│ 17 Cherry Tree Lane │")
            print_tab("\t│ London              │")
            print_tab("\t│ EN6 2QG             │")
            print_tab("\t│ United Kingdom      │")
            print_tab("\t└─────────────────────┘\n")
            print_tab("Not Uncle Jock's Parcel, Let's keep looking")
            pause()
            game.set_boxes(4)
                        
        elif num == 3:
            clear_screen()
            printNew()
            print_tab(pr_colour("l_blue","-- PARCEL "+ str(num) +" --") + "\n")
            print_tab("The address label on the parcel reads:\n")
            print_tab("\t┌─────────────────────┐")
            print_tab("\t│ H Poirot            │")
            print_tab("\t│ Apt. 56B            │")
            print_tab("\t│ Whitehaven Mansions │")
            print_tab("\t│ Sandhurst Square    │")
            print_tab("\t│ London              │")
            print_tab("\t│ EC1M 6EU            │")
            print_tab("\t│ United Kingdom      │")
            print_tab("\t└─────────────────────┘\n")
            print_tab("Not Uncle Jock's Parcel, Let's keep looking")
            pause()
            game.set_boxes(5)
                        
        elif num == 4:
            clear_screen()
            printNew()
            print_tab(pr_colour("l_blue","-- PARCEL "+ str(num) +" --") + "\n")
            print_tab("The address label on the parcel reads:\n")
            print_tab("\t┌────────────────────┐")
            print_tab("\t│ P Bear             │")
            print_tab("\t│ 32 Windsor Gardens │")
            print_tab("\t│ London             │")
            print_tab("\t│ W9 3RG             │")
            print_tab("\t│ United Kingdom     │")
            print_tab("\t└────────────────────┘\n")
            print_tab("Not Uncle Jock's Parcel, Let's keep looking")
            pause()
            game.set_boxes(6)
        office_empty(game)
    else:
        if num == 1 :
            clear_screen()
            printNew()
            print_tab(pr_colour("l_blue","-- PARCEL "+ str(num) +" --") + "\n")
            print_tab("The address label on the parcel reads:\n")
            print_tab("\t┌────────────────────┐")
            print_tab("\t│ D Duck             │")
            print_tab("\t│ 1313 Webfoot Walk  │")
            print_tab("\t│ Duckburg           │")
            print_tab("\t│ CA 95125           │")
            print_tab("\t│ USA                │")
            print_tab("\t└────────────────────┘\n")
            print_tab("Not Uncle Jock's Parcel, Let's keep looking")
            pause()
            game.set_boxes(7)
 
        elif num == 2:
            clear_screen()
            printNew()
            print_tab(pr_colour("l_blue","-- PARCEL "+ str(num) +" --") + "\n")
            print_tab("The address label on the parcel reads:\n")
            print_tab("\t┌────────────────────────┐")
            print_tab("\t│ R Tyler                │")
            print_tab("\t│ Flat 48 Bucknall House │")
            print_tab("\t│ Powell Estate          │")
            print_tab("\t│ London                 │")
            print_tab("\t│ SE15 7GO               │")
            print_tab("\t│ United Kingdom         │")
            print_tab("\t└────────────────────────┘\n")
            print_tab("Not Uncle Jock's Parcel, Let's keep looking")
            pause()
            game.set_boxes(8)
       
        elif num == 3:
            clear_screen()
            printNew()
            print_tab(pr_colour("l_blue","-- PARCEL "+ str(num) +" --") + "\n")
            print_tab("The address label on the parcel reads:\n")
            print_tab("\t┌────────────────────┐")
            print_tab("\t│ J Brady            │")
            print_tab("\t│ 4222 Clinton Way   │")
            print_tab("\t│ Los Angeles        │")
            print_tab("\t│ CA 12297           │")
            print_tab("\t│ USA                │")
            print_tab("\t└────────────────────┘\n")
            print_tab("Not Uncle Jock's Parcel, Let's keep looking")
            pause()
            game.set_boxes(9)
        office_empty(game)

def office_empty(game = N_game()):
    empty = game.check_boxes()
    if empty == True:
        clear_screen()
        printNew()
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
    computer(game)
    # warehouse(game)