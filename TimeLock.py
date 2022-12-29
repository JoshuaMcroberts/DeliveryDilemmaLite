
from datetime import datetime, timedelta
from time import sleep
import sys
# from colorama import *
import os
from NumberDisplay import *
import ArtDisplay

def convert_timedelta(duration):
    days, seconds = duration.days, duration.seconds
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return days, hours, minutes, seconds



def countdown(openTime, padLeft, padTop):
    now = datetime.now()

    dif = openTime - now
    days, hours, mins, secs  = convert_timedelta(dif)

    firstdisplay("{}{}:{}{}:{}{}:{}{}".format("0" if days < 10 else "",days, "0" if hours < 10 else "",hours, "0" if mins < 10 else "",mins, "0" if secs < 10 else "",secs), padLeft, padTop)
    #firstdisplay("{}{}:{}{}:{}{}:{}{}".format("0" if days < 10 else "",days, "0" if hours < 10 else "",hours, "0" if mins < 10 else "",mins, "0" if secs < 10 else "",secs))

    while (days !=0 or hours != 0  or mins != 0 or secs != 0):
        if secs != 0:
            secs -= 1
        else:
            if mins !=0:
                mins -= 1
                secs = 59
            else:
                if hours != 0:
                    hours -= 1 
                    mins = 59
                    secs = 59
                else:
                    if days != 0:
                        days -= 1
                        hours = 23  
                        mins = 59
                        secs = 59
            
            
        sleep(.998)
        # clear()
        # print("Days: {}{} Hours: {}{} Minutes: {}{} Seconds: {}{}".format("0" if days < 10 else "",days, "0" if hours < 10 else "",hours, "0" if mins < 10 else "",mins, "0" if secs < 10 else "",secs))
        display("{}{}:{}{}:{}{}:{}{}".format("0" if days < 10 else "",days, "0" if hours < 10 else "",hours, "0" if mins < 10 else "",mins, "0" if secs < 10 else "",secs), padLeft, padTop)


def dialling():
    for i in range(2):
        ast = 0 
        p_ast = ""
        sys.stdout.write("\033[K")
        while ast < 6:
           
            p_ast = p_ast + "∗ "
            print("\tPhone Dialling " + p_ast , end="\r")
            sleep(0.4)
            ast += 1
    sleep(0.5)


def pos( x, y ):
    return '\x1b[' + str(y) + ';' + str(x) + 'H'

def clear():
    os.system('cls||clear')

def main():
    init()
    print( Fore.RED + pos(30,10) + "Red here"+ Fore.YELLOW + pos(10,5) + "Yellow here")

def getCountPadding(cols, lines):
    
    
# print("window Size Cols:{}, Lines:{}".format(cols,lines))

    padLeft = (cols - 126)/2
    padTop = (lines- 9)/2
    
    padLeft = int(padLeft)
    padTop = int(padTop)
    
    return padLeft, padTop
    

def lockScreen(openTime):
    clear()
    cols, lines = os.get_terminal_size()
    
    ArtDisplay.introArt(cols, lines)
    padLeft, padTop = getCountPadding(cols, lines)
    
    countdown(openTime, padLeft,padTop+3)

def timeCheck(testing):
    present = datetime.now()
    
    test = datetime.now() + timedelta(seconds=15)
    c_date = datetime(2022,12,24,23,59,59,00)
    
    if testing:
        openTime = test
    else:
        openTime = c_date
        
    if  openTime > present:
        lockScreen(openTime)
    else:
        lockScreen(test)


if (__name__ == "__main__"):
    
    # dialling()
  
    # main()
    
    
    # clear()
    # cols, lines = os.get_terminal_size()
    # ArtDisplay.introArt(cols, lines)
    # padLeft, padTop = getCountPadding(cols, lines)
    # countdown(padLeft,padTop+3)
    present = datetime.now()
    
    test = datetime(2022, 12,22, 22, 25, 30)
    c_date = datetime(2022,12,24,23,59,59,00)
    openTime = test
    
    if  openTime > present:
        lockScreen(openTime)
    clear()
    print("Straight to fun world")
    