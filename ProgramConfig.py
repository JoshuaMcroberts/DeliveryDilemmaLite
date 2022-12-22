import os

from colorama import *
from ArtDisplay import *
from TerminalTools import clear, pos
from TimeLock import countdown


clear()
# print("{} = {} - 130\n{} = {} - 30".format(paddingL,cols,paddingT,lines))

def ConfigTest():
    clear()
    cols, lines = os.get_terminal_size()
    
    
# print("window Size Cols:{}, Lines:{}".format(cols,lines))

    padLeft = (cols - 130)/2
    padTop = (lines- 30)/2
    
       
    padLeft = int(padLeft)
    padTop = int(padTop)
    if padLeft%2 ==1:
       padLeft -=1 
    pTop = padTop +1
    # pLeft = padLeft +
    # print(Style.RESET_ALL+" ")
    iL = 0
    iC = 0
    lastC=0
    trip = False
    for y in range(lines):

        if y > padTop-1 and y < padTop +30:

            if iL <= 30:

                for x in range (cols):

                    if x > padLeft+1 and x < padLeft+1 + 130:
                        
                        if iC <129:
                            print(Style.RESET_ALL+"1",end="")
                        else:
                            print(Style.RESET_ALL+"2",end="")
                        iC += 1
                        trip =True
                    else:
                        print(Back.RED+"3",end="")
                    
                # print("000000000000000")
                print("")

            else:
                for x in range (cols):

                    if x > padLeft+1 and x < padLeft+1 + 130:
                        
                        if iC <129:
                            print(Style.RESET_ALL+"_",end="")
                        else:
                            print(Style.RESET_ALL+"+",end="")
                        iC += 1
                    else:
                        print(Back.RED+"=",end="")
                    
                # print("000000000000000")
                print("")

        else:   
            for x in range(cols):     
                print(Back.RED+ "-", end="")
        if trip:
            iL += 1
            trip= False
            lastC = iC
        
        iC = 0
       
    an1=cols-130
    an2=lines-30
    nice(padLeft+3, pTop)
    print(pos(padLeft,pTop)+"padLeft:{} padTop:{} Full Screen:{}x{} {}-130={} {}-30={}".format(padLeft,pTop,cols,lines,cols,an1,lines,an2))
    print(iL, lastC)


def CountdownUI():
    clear()
    cols, lines = os.get_terminal_size()
# print("window Size Cols:{}, Lines:{}".format(cols,lines))

    padLeft = (cols - 130)/2
    padTop = (lines- 30)/2
    
    padLeft = int(padLeft)
    padTop = int(padTop)
    
    if padLeft%2 ==1:
       padLeft -=1 
    
    # print(padLeft,padTop)
    # print(Style.RESET_ALL+" ")
    for y in range(lines):
        if y > padTop and y < padTop +30:
            for x in range (cols):
                if x > padLeft and x < padLeft + 130:
                    print(Style.RESET_ALL+" ",end="")
                else:
                    print(Back.RED+" ",end="")
            # print("000000000000000")
            print("")

        else:   
            for x in range(cols):     
                print(Back.RED+ " ", end="")
    # init()
    nice(padLeft, padTop)
    # pos(0,0)
    # nice1(padLeft+130, padTop+30)

    # countdown()
    # print(pos(100,10)+ "Here")
# init()
# paddingT = int(paddingT) +1
# paddingL = int(paddingL) +2
# print(pos(paddingL , paddingT) + "done")
# print(paddingL,paddingT)

# print( Fore.RED + pos(30,10) + "Red here"+ Fore.YELLOW + pos(10,5) + "Yellow here")

#

if __name__ =="__main__":
    ConfigTest()
    # CountdownUI()