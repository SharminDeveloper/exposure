class Exposure:
    def __init__(self,
                 main= [
        [1,1,0,0,0,0,0,1,0],
        [0,1,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,1,0,0],
        [0,1,0,0,1,0,1,1,0],
        [1,0,1,1,0,0,0,1,1],
        [1,0,0,0,0,1,0,1,0],
        [1,0,1,1,0,1,1,0,0],
        [1,0,0,1,0,1,1,1,0],
        [1,1,1,1,0,0,0,0,0],
    ]):    
        self.main = main
        self.expose = [[False for item2 in item] for item in self.main]
        self.previous_blocks = []
    def block(self,pattern,row,column):
        if row == 'nothing' or column == 'nothing':
            return 'nothing'
        binary = pattern[row][column]
        return binary
    def above_index(self,row,column):
        if row == 0:
            return ['nothing','nothing']
        row -= 1
        return [row,column]
    def below_index(self,row,column):
        if row == len(self.main)-1:
            return ['nothing','nothing']
        row+=1
        return [row,column]
    def right_index(self,row,column):
        if column == len(self.main[0])-1 :
            return ['nothing','nothing']
        column+=1
        return [row,column]
    def left_index(self,row,column):
        if column == 0:
            return ['nothing','nothing']
        column-=1
        return [row,column]
    def push(self,pattern,row,column,item):
        del pattern[row][column]
        pattern[row].insert(column,item)
        return pattern
    def check_around(self,row,column):
        Above = self.above_index(row,column)
        Below = self.below_index(row,column)
        Right = self.right_index(row,column)
        Left = self.left_index(row,column)
        if self.block(self.main,Above[0],Above[1]) == 1 and (Above not in self.previous_blocks):
            self.previous_blocks.append(Above)
            self.expose = self.push(self.expose,Above[0],Above[1],True)
            self.check_around(Above[0],Above[1])
        if self.block(self.main,Below[0],Below[1]) == 1 and (Below not in self.previous_blocks):
            self.previous_blocks.append(Below)
            self.expose = self.push(self.expose,Below[0],Below[1],True)
            self.check_around(Below[0],Below[1])
        if self.block(self.main,Right[0],Right[1]) == 1 and (Right not in self.previous_blocks):
            self.previous_blocks.append(Right)
            self.expose = self.push(self.expose,Right[0],Right[1],True)
            self.check_around(Right[0],Right[1])
        if self.block(self.main,Left[0],Left[1]) == 1 and (Left not in self.previous_blocks):
            self.previous_blocks.append(Left)
            self.expose = self.push(self.expose,Left[0],Left[1],True)
            self.check_around(Left[0],Left[1])    
    def run(self):    
        for row_index in range(len(self.main)):
            row = self.main[row_index]
            for column_index in range(len(row)): 
                if column_index == 0 or column_index == len(row)-1 or row_index == 0 or row_index == len(self.main)-1:
                    if self.block(self.main,row_index,column_index) == 1 :
                        self.expose = self.push(self.expose,row_index,column_index,True)
                        self.check_around(row_index,column_index)
        for row_check_index in range(len(self.expose)):
            row_check = self.expose[row_check_index]
            for status_index in range(len(row_check)):
                status=row_check[status_index]
                if status == True:
                    self.expose = self.push(self.expose,row_check_index,status_index,1)
                elif status ==False:
                    self.expose = self.push(self.expose,row_check_index,status_index,0)
    def print_entered_pattern(self):
        for row in self.main:
            print(row)
    def print_outcome_pattern(self):
        for row in self.expose:
            print(row)