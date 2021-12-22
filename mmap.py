class mind_map:
    
    def __init__(self, width, hieght):
        self.map_list = []
        h_hieght = int(hieght/2)
        h_width = int(width/2)
        
        for i in range(h_hieght):
            row = []
            row.append(" ")
            odd = True
            for j in range(width):
                if odd:
                    row.append("1")
                    odd = False
                else:
                    row.append("-")
                    odd = True 
                
            self.map_list.append(row)
            
            odd = True
            row2 = []
            for j in range (width):
                if odd:
                    row2.append(" ")
                    odd = False
                else:
                    row2.append("|")
                    odd = True 
                
            self.map_list.append(row2)    

    # def make_map(self):
    #     print("word")
        
    #     map = []
    #     print(map)
        
    #     for i in range(5):
    #         row = []
    #         for j in range(6):
    #             row.append(" 1 ")   
    #         map.append(row)
        
    #     print(map)

    def display_map(self):
        # print("")
        
        for i, row in enumerate(self.map_list):
            print("")
            for j, item in enumerate(row):
                print(item  ,end="")

def all_characters():
    print()
    
    for i in range(20):
        # if i%10 == 9:
            
        #     print("", end="")
            
            
        print(i , " : ", chr(i), " ")

def all_characters_2():
    print()
    # -*- coding: utf-8 -*- 
    for i in range(0xB3, 0xDA):
        print(chr(i).decode('cp437'))

    # without decoding (see comment by J.F.Sebastian)
    print(''.join(map(chr, range(0xb3, 0xda))))


def test():
    chars = {
    'a': '┌',
    'b': '┐',
    'c': '┘',
    'd': '└',
    'e': '─',
    'f': '│',
    'g': '┴',
    'h': '├',
    'i': '┬',
    'j': '┤',
    'k': '╷',
    'l': '┼'
    }
    print("")
    print(chars)

if __name__ =="__main__":
    
    myMap = mind_map(12,10)
    myMap.display_map()
    
    # all_characters_2()
    
    test()
    
    top1 = ["┌─────┐"]
    
    top2 = ["┌──┴──┐"]
    
    mid1 = ["│     │"]
           
    midL = ["┤     │"]
    
    midR = ["│     ├"]
    
    mid2 = ["┤     ├"]
    
    bot1 = ["└─────┘"]
    
    bot2 = ["└──┬──┘"]
    
    empty = ["       "]
   
