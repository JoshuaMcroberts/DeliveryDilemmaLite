from libraries import *

class Plan:
    
    def __init__(self):
        self.map_list = [[0, 0, 1, 11, 2],
                         [9, 10, 8, 12, 0],
                         [5, 7, 15, 14, 0],
                         [0, 0, 4, 13, 2],
                         [0, 0, 1, 7, 2]]
        
        self.visited = [[0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]]
        
        self.set_list = [[16, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]]
        
        self.pre = (0,0)
    
    def print_set(self):
        for row in self.set_list:
            print(row)
            
    def print_visited(self):
        for row in self.visited:
            print(row)
    
    def print_map(self):
        for row in self.map_list:
            print(row)
    
      
    def player_enter(self, c_tup, p_tup):
        
        c_y = c_tup[0]
        c_x = c_tup[1]
        p_y = p_tup[0]
        p_x = p_tup[1]
                
        # check visisted for if
        n_ver = self.visited[c_y]
        
        if n_ver[c_x] == 0:
            
            
            # Visited Val  
            n_ver = self.visited[c_y]
            n_ver[c_x] = 1
            
            
            
            # Default Room Val
            var = self.map_list[c_y] 
            ver = var[c_x]   
            n_ver = self.set_list[c_y]
            n_ver[c_x] = ver
            
            # self.print_set()
           
            
            # Discover Neigbouring Rooms
            
            str_bin = int_bin(ver)
            
            bottom = str_bin[1]
            top = str_bin[2]
            left = str_bin[3]
            right = str_bin[4]
            
            # ERROR in THIS LOGIC
            
            # Bottom Check/Set 
            y_n = c_y + 1
            x_n = c_x 
            if y_n < len(self.set_list): 
                
                row = self.visited[y_n]
                bot_val = row[x_n]
                
                if bottom == "1" and bot_val == 0:
                    loc = self.set_list[y_n]
                    loc[x_n] = 4
                
            # Top Check/Set 
            y_n = c_y - 1
            x_n = c_x 
            if y_n >= 0: 
            
                row = self.visited[y_n]
                top_val = row[x_n]
                
                if top == "1" and top_val == 0:
                    loc = self.set_list[y_n]
                    loc[x_n] = 8
            
            # Right Check/Set 
            y_n = c_y
            x_n = c_x + 1
            if x_n < len(self.set_list[0]): 
                
                row = self.visited[y_n]
                rig_val = row[x_n]
        
                if right == "1" and rig_val == 0:
                    loc = self.set_list[y_n]
                    loc[x_n] = 2
                    
            # Left Check/Set
            y_n = c_y
            x_n = c_x - 1 
            if x_n >= 0:  
                
                row = self.visited[y_n]
                lef_val = row[x_n]
            
                if left == "1" and lef_val == 0:
                    loc = self.set_list[y_n]
                    loc[x_n] = 1
        
        # Player Presence
        var = self.set_list[c_y] 
        var[c_x] = var[c_x] + 16
        
        # Exit Previous Room
        p_y = p_tup[0]
        p_x = p_tup[1]
        
        var = self.set_list[p_y] 
        ver = var[p_x]   
        var [p_x] = var[p_x] - 16
        p_tup = (c_y, c_x)
        
        return p_tup
        
    def player_exit(self, tup):
        
        y = tup[0]
        x = tup[1]
        
        var = self.set_list[y] 
        ver =var[x]   
        var[x] = var[x] - 16
        # print(ver)
        # print(var[x])
            
    def print_map(self):
        print("")
        self.printable_map = []
        for row in self.set_list:
            n_row = []
            for room in row:
                box = make_box(room)
                n_row.append(box)
                
            self.printable_map.append(n_row)
        
        p_map = "\t      ────────────────  MAP  ────────────────\n\t┌─────────────────────────────────────────────────┐\n"
        for row in self.printable_map:
            top = "\t│  "
            mid = "\t│  "
            bot = "\t│  "
            ext = "\t│  "
            for part in row:
                ext = ext + part[0]
                top = top + part[1]
                mid = mid + part[2]
                bot = bot + part[3]
                    
            p_map = p_map + ext + "  │\n" + top + "  │\n" + mid + "  │\n" + bot + "  │\n" 
        p_map = p_map + "\t└─────────────────────────────────────────────────┘"
        print(p_map)

def box_numbers():
    for i in range(0, 32):
        box = make_box(i)
        p_box =""
        part = ""
        for part in box:
            p_box = p_box +"\n"+ part
        
        print()
        print("Box {}: {}".format(i, p_box))
def int_bin(num):
        box_code = str(bin(num))
        box_code = box_code[2 : : ]
    
        while len(box_code) < 5:
            box_code = "0" + box_code
        
        return box_code
    
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
    
    # p_m_1 = " │  X  │ " 
    # p_m_l = "─┤  X  │ "
    # p_m_r = " │  X  ├─"
    # p_m_2 = "─┤  X  ├─"
    
    a = " ┌─\─/─┐"
    b = " │  X  │"
    c = " └─/─\─┘"
    
    bot_1 = " └─────┘ "
    bot_2 = " └──┬──┘ "
    
    extra = "    │    "
    empty = "         "
    
    box_code = int_bin(num)
    
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
            box.append(empty)
            box.append(top_1)
        else:
            box.append(extra)
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

def pause_():
    input("Press Enter to continue...")

if __name__ =="__main__":
    
    pre = (0,0)
    myMap = Plan()
    # myMap.print_map()
    # myMap.player_enter((2,1))
    # clear_screen()
    # myMap.print_map()
    # pause_()
    
    pre = myMap.player_enter((3,2), pre)
    clear_screen()
    myMap.print_map()
    pause_()
    
    pre = myMap.player_enter((2,2), pre)
    clear_screen()
    myMap.print_map()
    pause_()
    
    pre = myMap.player_enter((2,3), pre)
    clear_screen()
    myMap.print_map()
    pause_()
    
    pre = myMap.player_enter((3,3), pre)
    clear_screen()
    myMap.print_map()
    pause_()
