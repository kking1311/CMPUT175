#----------------------------------------------------
# Lab 3: Numerical Tic Tac Toe class
# 
# Author: 
# Collaborators:
# References:
#----------------------------------------------------

class NumTicTacToe:
    def __init__(self):
        '''   
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [] # list of lists, where each internal list represents a row
        self.size = 3   # number of columns and rows of board
        
        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)      
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''
        # TO DO: delete pass and print out formatted board
        # e.g. an empty board should look like this:
        #    0   1   2  
        # 0    |   |   
        #   -----------
        # 1    |   |   
        #   -----------
        # 2    |   |           
        print("  0   1   2")
        for i, row in enumerate(self.board):
            print(i, end=' ')
            if i<2:
             for j, element in enumerate(row):
                 if j<2:
                   if element==0:
                     print("  |",end=' ')
                   else:
                      print(f"{element}|",end=' ')
                 else:
                     print(f"{element}", end='')
             # Print a newline after each row
             print("\n" + "  " + "-" * 9)
            else:
               last_line,new_last_line=self.board[len(self.board)-1],[]
               for e in last_line:
                  if e==0:
                     new_last_line.append(" ")
                  else:
                     new_last_line.append(e)
               print(f" {new_last_line[0]}| {new_last_line[1]} | {new_last_line[2]} ")

    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty, or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''
        return self.board[row][col] == 0
        

    def update(self, row, col, num):
        '''
        Assigns the integer, num, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           num (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        if self.squareIsEmpty(row, col): 
            self.board[row][col] = num   # updating the value at the particular square 
            return True
        return False


    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''
        result=0
        for i in range(len(self.board)):
           for j in range(len(self.board[i])):
              if self.squareIsEmpty(i,j)==False:
                 result=1
              else:
                 continue
        if result==1:
           return False
        else:
           return True


    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        for i in range(self.size):
            # Check row sum
            row_sum = 0 
            for j in range(self.size):
                row_sum += self.board[i][j]
            # Check column sum
            col_sum = 0
            for j in range(self.size):
                col_sum += self.board[j][i]
            # Check principal diagonal sum
            principalSum = 0
            for j in range(self.size):
                principalSum += self.board[j][j]
            # Check reverse diagonal sum
            reverseSum = 0
            for j in range(self.size):
                reverseSum += self.board[j][self.size - 1 - j]
            # If any of the sums is equal to 15, return True (we have a winner)
            if row_sum == 15 or col_sum == 15 or principalSum == 15 or reverseSum == 15:
                return True
    # If no winning conditions were met, return False (no winner yet)
        return False
    

if __name__ == "__main__":
    # TEST EACH METHOD THOROUGHLY HERE
    # suggested tests are provided as comments, but more tests may be required
    # start by creating empty board and checking the contents of the board attribute
    chance = NumTicTacToe()
    print('Contents of board attribute when object first created:')
    print(chance.board)
    # does the empty board display properly?
    chance.drawBoard()
    # assign a number to an empty square and display
    chance.update(2, 1, 5)
    chance.drawBoard()
    # try to assign a number to a non-empty square. What happens?
    if chance.update(2, 2, 3):
        print("Square updated.")
    else:
        print("Square cannot be updated.")
    chance.drawBoard()
    # check if the board has a winner. Should there be a winner after only 1 entry?
    if chance.isWinner():
        print("Winner!")
    else:
        print("No winner yet.")
    # check if the board is full. Should it be full after only 1 entry?
    if chance.boardFull():
        print("Board is full.")
    else:
        print("Board is not full yet.")
    # add values to the board so that any line adds up to 15. Display
    chance.update(0, 0, 6)
    chance.update(0, 1, 8)
    chance.update(0, 1, 1)
    chance.drawBoard()
    # check if the board has a winner
    if chance.isWinner():
        print("Winner!")
    else:
        print("No winner yet.")
    # check if the board is full
    if chance.boardFull():
        print("Board is full.")
    else:
        print("Board is not full yet.")
    # write additional tests, as needed