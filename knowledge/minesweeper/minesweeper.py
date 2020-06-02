import itertools
import random
import copy

class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return "{} = {self.count}".format(self.cells,self.count)

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        if len(self.cells)==count:
            return self.cells
        else:
            return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        if self.count==0:
            return self.cells
        else:
            return set()
        #raise NotImplementedError

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.cells.remove(cell)
            self.count-=1
            
        

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        #print("sdsdsd")
        if cell in self.cells:
            self.cells.remove(cell)
            #self.count-=1
        
        
        #raise NotImplementedError


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        #print("addde")
        self.safes.add(cell)
        
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        #print('*************************')
        self.mark_safe(cell)
        self.moves_made.add(cell)

#            
        #print('555555555')        
        if cell[0]==self.height-1:
                if (cell[1]>0) and (cell[1]<(self.width-1)):
                    sentence=Sentence(((cell[0],cell[1]+1),(cell[0],cell[1]-1),(cell[0]-1,cell[1]+1),(cell[0]-1,cell[1]-1),(cell[0]-1,cell[1])),count)
                    #self.knowledge.append(sentence)
                if (cell[1]==0):
                    sentence=Sentence(((cell[0],cell[1]+1),(cell[0]-1,cell[1]),(cell[0]-1,cell[1]+1)),count)
                    #self.knowledge.append(sentence)
                if (cell[1]==self.width-1):
                    sentence=Sentence(((cell[0],cell[1]-1),(cell[0]-1,cell[1]),(cell[0]-1,cell[1]-1)),count)
                    #self.knowledge.append(sentence)
                       
                       
        if cell[0]==0:
                if (cell[1]>0) and (cell[1]<(self.width-1)):
                    sentence=Sentence(((cell[0],cell[1]+1),(cell[0],cell[1]-1),(cell[0]+1,cell[1]+1),(cell[0]+1,cell[1]-1),(cell[0]+1,cell[1])),count)
                    #self.knowledge.append(sentence)
                if (cell[1]==0):
                    sentence=Sentence(((cell[0],cell[1]+1),(cell[0]+1,cell[1]),(cell[0]+1,cell[1]+1)),count)
                    #self.knowledge.append(sentence)
                if (cell[1]==self.width-1):
                    sentence=Sentence(((cell[0],cell[1]-1),(cell[0]+1,cell[1]),(cell[0]+1,cell[1]-1)),count)
                    #self.knowledge.append(sentence)
            
        if cell[1]==0:
                if cell[0]>0 and cell[0]<(self.height-1):
                    sentence=Sentence(((cell[0]-1,cell[1]),(cell[0]+1,cell[1]),(cell[0],cell[1]+1),(cell[0]-1,cell[1]+1),(cell[0]+1,cell[1]+1)),count)
                    #self.knowledge.append(sentence)
                
        if cell[1]==(self.width-1):
                if cell[0]==0:
                    Sentence(((cell[0]+1,cell[1]-1),(cell[0],cell[1]-1)),count)
                if cell[0]>0 and cell[0]<(self.height-1):
                    sentence=Sentence(((cell[0],cell[1]-1),(cell[0]-1,cell[1]),(cell[0]+1,cell[1]),(cell[0]+1,cell[1]-1),(cell[0]-1,cell[1]-1)),count)
                    #self.knowledge.append(sentence)
            
        if cell[0]>0 and cell[0]<(self.height-1) and cell[1]>0 and cell[1]<(self.width-1):
                sentence=Sentence(((cell[0],cell[1]-1),(cell[0],cell[1]+1),(cell[0]-1,cell[1]),(cell[0]-1,cell[1]+1),(cell[0]-1,cell[1]-1),
                   (cell[0]+1,cell[1]-1),(cell[0]+1,cell[1]),(cell[0]+1,cell[1]+1)),count)

            
        senc1l=[]
        senc2l=[]    
        print()    
        if len(self.knowledge)>1:
                
                lst=[]
                lst_=[]

                for sen in self.knowledge:#range(len(self.knowledge)):
                    if sentence.cells <= sen.cells and len(sentence.cells)>0:
                               #lst.append(sen)
                               #print(1)
                               senc1=copy.deepcopy(sen)
                               [senc1.cells.remove(cell) for cell in sentence.cells]
                               senc1.count-=sentence.count
                               #print("1:\t",senc1.cells,"\t",senc1.count)
                               senc1l.append(senc1)
                               #self.knowledge.append(senc)
                               
                    #if any of the sentences in knowledge is a subset of sentence
                    elif sen.cells <= sentence.cells and len(sen.cells)>0:
                               #print(2)
                               senc2=copy.deepcopy(sentence)
                               [senc2.cells.remove(cell) for cell in sen.cells]
                               senc2.count-=sen.count
                               #print("2:\t",senc2.cells,"\t",senc2.count)
                               senc2l.append(senc2)
                               #self.knowledge.append(senc)
                               #lst_.append(sen)
 
        if len(senc1l)>0:
            for sen in senc1l:
                self.knowledge.append(sen)
        if len(senc2l)>0:
            for sen in senc2l:
                self.knowledge.append(sen)
                
    
        for cel in self.safes:
            if cel in sentence.cells:
                #print("SENTENCE BEFORE SAFE:",sentence.cells,"/t",sentence.count) 
                #print("safe:",cel)
                

                sentence.cells.remove(cel)
        self.knowledge.append(sentence)       
                
        mines=[]
        safes=[]

            #add the full sentence
        
        for sen in self.knowledge:
            if len(sen.cells)==0:
                self.knowledge.remove(sen)
        for sen in self.knowledge:
            if sen.count==len(sen.cells) and sen.count>0:
            #if list(list(sen.values()))[0]==len(list(list(sen.keys())[0])) and len(list(list(sen.keys())[0]))>0:
                #print("mark1")
                for cel in sen.cells:
                    
                    mines.append(cel)
                    
            elif sen.count==0 and len(sen.cells)>0:
                #print("mark2")
                for cel in sen.cells:
                    
                    safes.append(cel)
                    #self.mark_safe(cel)
        #print("mine list: ",mines)    
        #print("safe list: ",safes)    
        for mine in set(mines):
            self.mark_mine(mine)
        for safe in set(safes):
            self.mark_safe(safe)
                    #print("self.knowledge: ",self.knowledge)
            
        
        
        #print("SENTENCE:",sentence.cells,"/t",sentence.count) 
        #raise NotImplementedError

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        #print ("safes: ", self.safes)
        #print ("mines: ", self.mines)
        #print ("knowledge: ", self.knowledge)
        
        for cell in self.safes:
            if not (cell in self.safes.intersection(self.moves_made)):
                #print('return', cell)
                return cell
        
        
        
        #raise NotImplementedError

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
#        
        cell=tuple((random.randrange(self.height),random.randrange(self.width)))

        while cell in self.mines or cell in self.moves_made:
            cell=tuple((random.randrange(self.height),random.randrange(self.width)))
        
        
        return cell

        