from colorama import *
from time import sleep
import TerminalTools
import random
from libraries import *
# FR = Fore.RED + Style.NORMAL
# FY = Fore.YELLOW + Style.NORMAL
# FBL = Fore.BLUE + Style.NORMAL
# FG = Fore.GREEN + Style.NORMAL
# FW = Fore.WHITE + Style.NORMAL
# FGY = Fore.BLACK + Style.BRIGHT # Fore.WHITE + Style.DIM
# SB = Style.BRIGHT
# SN = Style.NORMAL
# SD = Style.DIM
# RS = Style.RESET_ALL

FR = '\033[38;5;9m'
FY = '\033[38;5;178m'
FDY = '\033[38;5;94m'
FBL = '\033[38;5;26m'
FLB = '\033[38;5;74m'
FG = '\033[38;5;2m'
FW = '\033[38;5;15m'
FGY = '\033[38;5;241m'
RS = '\033[00m'


def ascii_del_dil():
    deldil =[
            RS+FLB + "      ____       __ _                         ____  _ __                              ",
            FLB + "     / __ \___  / /_/   _____  _______  __   / __ \/_/ /__  ____ ___  ____ ___  ____ _",
            FLB + "    / / / / _ \/ / / | / / _ \/ ___/ / / /  / / / / / / _ \/ __ `__ \/ __ `__ \/ __ `/",
            FLB + "   / /_/ /  __/ / /| |/ /  __/ /  / /_/ /  / /_/ / / /  __/ / / / / / / / / / / /_/ / ",
            FLB + "  /_____/\___/_/_/ |___/\___/_/   \__, /  /_____/_/_/\___/_/ /_/ /_/_/ /_/ /_/\__,_/  ",
            FLB + "                                 /____/                                               "]
    cols, lines = screen_size()
    sleep(1)
    printText(FLB+"Welcome to..."+RS,int(cols/2 - (len(deldil[0])/2)-2), int(lines/2-(len(deldil)/2)-2))
    sleep(1)
    printArt(deldil, int(cols/2 - (len(deldil[0])/2)+4), int(lines/2-(len(deldil)/2)))
    sleep(1)
    printText("",int(cols/2 - (len(deldil[0])/2)+20), int(lines/2-(len(deldil)/2)+5))
def text(name):
    
    nln =[
    RS+FG+" _  _     _     _                    _  _            _ ",
    FG+"| \| |___| |_  | |   ___ _ _  __ _  | \| |_____ __ _| |",
    FG+"| .` / _ \  _| | |__/ _ \ ' \/ _` | | .` / _ \ V  V /_|",
    FG+"|_|\_\___/\__| |____\___/_||_\__, | |_|\_\___/\_/\_/(_)",
    FG+"                             |___/                     "]
    
    mc=[
    RS+FY+" __  __                     ___ _        _    _                 _ ",
    FY+"|  \/  |___ _ _ _ _ _  _   / __| |_  _ _(_)__| |_ _ __  __ _ __| |",
    FY+"| |\/| / -_) '_| '_| || | | (__| ' \| '_| (_-<  _| '  \/ _` (_-<_|",
    FY+"|_|  |_\___|_| |_|  \_, |  \___|_||_|_| |_/__/\__|_|_|_\__,_/__(_)",
    FY+"                    |__/                                          "] 
       
    wftt = [ 
    RS+FR+"__      __    _ _      __           _   _          _____ _               _ ",
    FR+"\ \    / /_ _(_) |_   / _|___ _ _  | |_| |_  ___  |_   _(_)_ __  ___ _ _| |",
    FR+" \ \/\/ / _` | |  _| |  _/ _ \ '_| |  _| ' \/ -_)   | | | | '  \/ -_) '_|_|",
    FR+"  \_/\_/\__,_|_|\__| |_| \___/_|    \__|_||_\___|   |_| |_|_|_|_\___|_| (_)",
    FR+"                                                                           "]  
    
    
    if name == 1:
        return nln 
    elif name == 2:
        return wftt
    else:
       return mc
  
    
def holly(dir):
    holTR = [
        RS+FG+" _/\_       __/\__",
        FG+" ) . (_    _) .  (",
        FG+" `) '.(    ) .' (`",
        FG+"   `-._\\"+FR+"()"+FG+"/__(~`",
        FR+"       ()()",
        FG+"      / |`\\",
        FG+"      ) : (",
        FG+"      `)_/`"
    ]

    holBL = [
        FG+"         __",
        FG+"       _/ (_",
        FG+"       ) : (",
        FG+"       \ | /",
        FG+"      __"+FR+"()()"+FG+"_",
        FG+"   .~)  /"+FR+"()"+FG+"\ '-._", 
        FG+" .) .'_(    )_'. (.",
        FG+" )_ '_(      )_' _(",
        FG+"   \/          \/",
    ]

    if dir == "TR":
        hol = holTR
    else:
        hol = holBL
    
    return hol
    # for i in hol:
    #     print(i + Style.RESET_ALL)

def bell(dir):
    # FR = Fore.RED
    # FY = Fore.YELLOW
    # SB = Style.BRIGHT
    # SN = Style.NORMAL
    # SD = Style.DIM

    belCL = [

    FY+"  (o:.._",
    FY+"  >     '`.", 
    FY+" /    "+FR+"__..."+FY+"\\",
    FY+"'  "+FR+".-'__....\\"+FY,  
    FY+" \\"+FR+"' -'"+FY+"_...--.;", 
    FR+"  \\'"+FY+".'"+FDY+"  \\\\_ "+FY+"  `.",
    FY+"   /     "+ FDY+"(_)"+FY+"   /",
    FY+"   |         .'",
    FY+"    '-...--'`",

    ]

    belCR =[
           FY+"        _..:o)",
           FY+"     .`'     <",
           FY+"    /"+FR+"...__    "+FY+"\\",
           FR+"   /....__'-.  "+FY+"'",
           FY+"  ;.--..._"+FR+"'- '"+FY+"/",
           FY+".`    "+FDY+"_//"+FY+" '."+FR+"'/",
           FY+"\\    "+FDY+"(_)"+FY+"    \\",
           FY+" '.         |",
           FY+"   `'--...-'",
    ]

    if dir == "L":
        bel = belCL
    else:
        bel = belCR

    return bel
    # for i in belCR:
    #     print(i + Style.RESET_ALL)



def bobbles():
    F1 = FR
    F2 = FG
    F3 = FBL
    F4 = FW
    F5 = FGY #FW
    F6 = FY #FGY

    bob = [

              "        ()",
              "       vvvv",
              "     .-\"==\"-.",
              "   .'___     `.",
              "  / /_/_/      \     ____",
              " | /_/_/        |  .%%%%%%.",
              " |              | /%/_/%%%%\_",
              "  \         .::::.%%%%%%%%(_{}-o",
              "   `.     .::::::::%%%%%%%%/",
              "     `-._/:/_/::::::\%%%%%'",
              "     o-0_)::::::::::|\"\"\"\"",
              "         \::::::::::/",
              "          `::::::::'",
              "            `````'",  
    ]

    bobC = [

              F6+"        ()",
              F6+"       ^^^^ ",
           F2+"     .-"+F6+"\"==\""+F2+"-.",
                F2+"   .'"+F5+"___"+F2+"     `.",
                F2+"  / "+F5+"/_/_/"+F2+"      \     "+F3+"____",
                F2+" | "+F5+"/_/_/"+F2+"        |  "+F3+".%%%%%%.",
                F2+" |              | "+F3+"/%"+F5+"/_/"+F3+"%%%%\\"+F4+"_",
                F2+"  \         "+F1+".::::."+F3+"%%%%%%%%"+F4+"(_{}-o",
                F2+"   `.     "+F1+".::::::::"+F3+"%%%%%%%%/",
                F2+"     `-."+F6+"_"+F1+SN+"/:"+F5+"/_/"+F1+"::::::\\"+F3+"%%%%%'",
                F1+"     "+F6+"o-0_)"+F1+SN+"::::::::::|"+F3+"\"\"\"\"",
                F1+"         \::::::::::/",
                F1+"          `::::::::'",
                F1+"            `````'",  
    ]

    for i in bobC:
        print(i + Style.RESET_ALL)
        

def box():
    boX =[RS +"0000000000",
    RS+"0000000000",
    RS+"0000000000",
    RS+"0000000000",
    RS+"0000000000",
    ]
    return boX


def DisplayAll():
    bel = bell("L")
    printArt(bel)
    bel = bell("R")
    printArt(bel)
    holly()
    bobbles()

def printArt(art, x, y):
    l=0
    for i in art:
        print(TerminalTools.pos(x, y+l) + i + RS)
        l +=1

def nice(x,y):
    hol = holly("TR")
   
    printArt(box(), x, y , "TR") 
    
def nice1(x,y):
    bel = bell("T")
   
    printArt(bel, x, y, "BR" ) 
    # print(x,y)

def printText(text, col, line):
    print(TerminalTools.pos(col, line)+ text)

def introArt(cols, lines):
    
    padLeft = int((cols - 130)/2)
    padTop = int((lines - 30)/2)
    centreLeft = int(cols/2)
    centreTop = int(lines/2)
    RightHol = holly("TR")
    RightBel = bell("T")
    LeftHol = holly("R")
    LeftBel = bell("L")
    printArt(RightBel, padLeft+115, padTop-3)
    printArt(RightHol, padLeft+115, padTop+26)
    printArt(LeftBel, padLeft-2, padTop+26)
    printArt(LeftHol, padLeft-2, padTop-3)
    option = random.randrange(1,4)
    
    textArt = text(option)
    printArt(textArt,centreLeft-(int(len(textArt[3])/2-4)), padTop+5 )
    message = "This program will unlock on Christmas day"
    message3 = "I hope you can wait that long!"
    message2 ="Close the window Exit"
    printText(message , centreLeft-(int(len(message)/2)), padTop+26)
    printText(message3 , centreLeft-(int(len(message3)/2)), padTop+28)
    printText(message2 , centreLeft-(int(len(message2)/2)), padTop+30)
    # printText(str(cols)+" " +str(lines),20,10 )
if __name__ == "__main__":

    # init()
    # DisplayAll()
    # bell()
    # clear()
    # introArt(cols, lines)
    # printArt(hol,45, 7 ) 
    print("No Main Functions running")
    
    

  
