class mind_map:
    
    def __init__(self):
        self.map_list = [[0, 0, 1, 11, 2],
                         [9, 10, 8, 12, 0],
                         [5, 7, 15, 14, 0],
                         [0, 0, 4, 13, 2],
                         [0, 0, 1, 7, 2]]
        
        self.printable_map = []
        
        
        
            
    def print_map(self):
        print("")
        for row in self.map_list:
            n_row = []
            for room in row:
                box = make_box(room)
                n_row.append(box)
                
            self.printable_map.append(n_row)
        
        # print(self.printable_map)
        
        p_map = ""
        for row in self.printable_map:
            top = ""
            mid = ""
            bot = ""
            
            for part in row:
                top = top + part[0]
                mid = mid + part[1]
                bot = bot + part[2]
                
            p_map = p_map + top + "\n" + mid + "\n" + bot + "\n"
            
        print(p_map)

                               

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

def make_box(num):
    
    top_1 = "┌─────┐"
    top_2 = "┌──┴──┐"
    
    mid_1 = "│     │" 
    mid_l = "┤     │"
    mid_r = "│     ├"
    mid_2 = "┤     ├"
    
    p_m_1 = "│  X  │" 
    p_m_l = "┤  X  │"
    p_m_r = "│  X  ├"
    p_m_2 = "┤  X  ├"
    
    bot_1 = "└─────┘"
    bot_2 = "└──┬──┘"
    empty = "       "
    
    box_code = str(bin(num))
    box_code = box_code[2 : : ]
    
    while len(box_code) < 5:
        box_code = "0" + box_code
    
    player = box_code[0]
    bottom = box_code[1]
    top = box_code[2]
    left = box_code[3]
    right = box_code[4]
    
    
    box =  []
    if player == "0" and bottom == "0" and top == "0" and left == "0" and right == "0":
        box = [empty, empty, empty]
    else:
        
        # Box Top
        if top == "0":
            box.append(top_1)
        else:
            box.append(top_2)
        
        if player == "0":
            
            if left == "0" and right == "0":
                box.append(mid_1)
            elif left == "0" and right == "1":
                box.append(mid_r)
            elif left == "1" and right == "0":
                box.append(mid_l)   
            elif left == "1" and right == "1":
                box.append(mid_2)
        else:
            if left == "0" and right == "0":
                box.append(p_m_1)
            elif left == "0" and right == "1":
                box.append(p_m_r)
            elif left == "1" and right == "0":
                box.append(p_m_l)   
            elif left == "1" and right == "1":
                box.append(p_m_2)
        
        if bottom == "0":
            box.append(bot_1)
        else:
            box.append(bot_2)
            
    # for parts in box:    
    #     print(parts)
    return box

def make_boxes():
    top_1 = "┌─────┐"
    top_2 = "┌──┴──┐"
    
    mid_1 = "│     │" 
    mid_l = "┤     │"
    mid_r = "│     ├"
    mid_2 = "┤     ├"
    
    p_m_1 = "│  X  │" 
    p_m_l = "┤  X  │"
    p_m_r = "│  X  ├"
    p_m_2 = "┤  X  ├"
    
    bot_1 = "└─────┘"
    bot_2 = "└──┬──┘"
    empty = "       "
    
    
    row1 = [top_1, top_1, top_1]
    row2 = [mid_r, mid_2, mid_l]
    row3 = [bot_1, bot_2, bot_2]
    row4 = [top_1, top_2, top_2]
    row5 = [mid_1, mid_r, mid_l]
    row6 = [bot_2, bot_2, bot_1]
    row7 = [top_2, top_2, top_1]
    row8 = [mid_r, mid_2, mid_l]
    row9 = [bot_1, bot_1, bot_1]    
    
    grid = [row1, row2, row3, row4, row5, row6, row7, row8, row9 ]
    
    for row in grid:
        print()
        for part in row:
            print(part, end="")

if __name__ =="__main__":
    
    myMap = mind_map()
    # myMap.display_map()
    
    # all_characters_2()
    
    # make_boxes()
    
    # for i in range(0,31):
    #     print("Box {}: ".format(i))
    #     make_box(i)
    #     print()
    
    myMap.print_map()
