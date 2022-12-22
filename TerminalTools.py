
from ctypes import alignment
from http.client import RESET_CONTENT
from TimeLock import *
from colorama import *
import os

def pos( x, y ):
    return '\x1b[' + str(y) + ';' + str(x) + 'H'

def zeroCursor():# not needed - check
    pos(0,0)

def clear():
    os.system('cls||clear')

def artPrint(list, x, y, alignment):
    i=0
    height = len(list)
    width = len(list[1])
    
    # if "R" in alignment:
    #     x = x - width
    #     if x < 0:
    #         x = 0
    #     print("right")
    # elif "B" in alignment:
    #     y = y - height
    #     if y < 0:
    #         y = 0
    #     print("bottom")
    


    for line in list:
        print(pos(x,y+i) + line)
        i += 1 
    print(Style.RESET_ALL+ "")

# a='3'

# bol = isinstance(a, int)

# if bol:
#     print(type(a))
# else:
#     print("nope")
def main():
    num = 7

    left = 11 - num
    threes = int(left/3)
    mods =  left%3

    startpos = (threes *10) + (threes * 24) + (mods * 12)

    print(startpos )

def getWinSize():
    # import os
    col, lines = os.get_terminal_size()
    print("Window Size Cols:{}, Lines:{}".format(col, lines))

def fullScreen():
    for l in range(4):
        for i in range(130):
            # print( Fore.RED + u"\u2588", end='')

            print(  Back.RED + "@", end='')
        print('')

    for l in range(10):
        for i in range(130):
            # print( Fore.RED + u"\u2588", end='')
            
            print(  Back.BLUE + "-", end='')
        print('')
    for l in range(16):
            for i in range(130):
                # print( Fore.RED + u"\u2588", end='')

                print(  Back.GREEN + "_", end='')
            print('')
    for l in range(4):
        for i in range(130):
            # print( Fore.RED + u"\u2588", end='')

            print(  Back.RED + "@", end='')
        print('')


def holly():
    hol = [
            Fore.GREEN+" _/\_      __/\__",
            Fore.GREEN+" )   (_   _) .' (",
            Fore.GREEN+" `) '.(  ) .'  (`",
            Fore.GREEN+"  `-._\\"+Fore.RED+"()"+Fore.GREEN+"/__(~`",
            Fore.GREEN+"      "+Fore.RED+"()()"+Fore.GREEN,
            Fore.GREEN+"     / |`\\",
            Fore.GREEN+"     ) : (",
            Fore.GREEN+"     `)_/`"
        ]

    for i in hol:
        print(i)
        print(Fore.WHITE, end='')
        

if __name__ == "__main__":

    # init()
    
    # getWinSize()
    # clear()

    fullScreen()
    # countdown()
    # holly()
    