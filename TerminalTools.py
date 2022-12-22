
# from ctypes import alignment
# from http.client import RESET_CONTENT
from TimeLock import *
# from colorama import *
import os

def pos( x, y ):
    return '\x1b[' + str(y) + ';' + str(x) + 'H'

def zeroCursor():# not needed - check
    pos(0,0)

def clear():
    os.system('cls||clear')

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
def setWinSize():
    os.terminal_size

if __name__ == "__main__":

    # init()
    
    getWinSize()
  
    