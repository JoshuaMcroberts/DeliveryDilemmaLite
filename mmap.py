from libraries import *

class mind_map:
    
    def __init__(self):
        self.map_list = [[0, 0, 1, 11, 2],
                         [9, 10, 8, 12, 0],
                         [5, 7, 15, 14, 0],
                         [0, 0, 4, 13, 2],
                         [0, 0, 1, 7, 2]]
        
        self.printable_map = []
        
    def player_enter(self, y, x):
        
        var = self.map_list[y] 
        ver =var[x]   
        var[x] = var[x] + 16
        # print(ver)
        # print(var[x])
        
    def player_exit(self, y, x):
        var = self.map_list[y] 
        ver =var[x]   
        var[x] = var[x] - 16
        # print(ver)
        # print(var[x])
            
    def print_map(self):
        print("")
        self.printable_map = []
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
            ext = ""
            for part in row:
                top = top + part[0]
                mid = mid + part[1]
                bot = bot + part[2]
                ext = ext + part[3]
                
            p_map = p_map + top + "\n" + mid + "\n" + bot + "\n" + ext + "\n"
            
        print(p_map)


def make_box(num):
    
    top_1 = " ┌─────┐ "
    top_2 = " ┌──┴──┐ "
    
    mid_1 = " │     │ " 
    mid_l = "─┤     │ "
    mid_r = " │     ├─"
    mid_2 = "─┤     ├─"
    
    p_m_1 = " │  " + pr_colour("l_green","X") +"  │ " 
    p_m_l = "─┤  " + pr_colour("l_green","X") +"  │ "
    p_m_r = " │  " + pr_colour("l_green","X") +"  ├─"
    p_m_2 = "─┤  " + pr_colour("l_green","X") +"  ├─"
    
    bot_1 = " └─────┘ "
    bot_2 = " └──┬──┘ "
    
    extra = "    │    "
    empty = "         "
    
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
        box = [empty, empty, empty, empty]
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
            box.append(empty)
        else:
            box.append(bot_2)
            box.append(extra)
            
    # for parts in box:    
    #     print(parts)
    return box

if __name__ =="__main__":
    
    myMap = mind_map()
    myMap.print_map()
    myMap.player_enter(2,1)
    clear_screen()
    myMap.print_map()
    pause()
    myMap.player_exit(2,1)
    myMap.player_enter(2,2)
    clear_screen()
    myMap.print_map()
    pause()