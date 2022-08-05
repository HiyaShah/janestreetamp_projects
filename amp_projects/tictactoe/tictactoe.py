class Board:
  """Represents a tic tac toe board"""
  count = 0

  def __init__(self, dim):
    """Creates a dim by dim size tictactoe board
    """
    if dim>0:
      self.dim = dim #dimension of matrix
    self.matrix = [[" "]*self.dim for i in range(self.dim)] #matrix is under abstraction

  @staticmethod
  def row_str(row):
    return " "+" | ".join(row) +" \n"

  def __str__(self):
    string_row = [Board.row_str(row) for row in self.matrix]
    hrule = ["---"*self.dim +"-"*(self.dim-1)+"\n" for i in range(self.dim)]
    # return hrule.join(string_row)
    grid = ""
    for i in range(len(string_row)):
      grid+=(string_row[i])
      if i<len(string_row)-1:
        grid+=(hrule[i])
    return grid

  def _winner(self,x_or_o):
    "Checks for a winner given either an x or o to check (not to be used by the user)"
    flatten_matrix = [val for row in self.matrix for val in row]
    #check rows
    if (any(flatten_matrix[i:self.dim+i]==[x_or_o]*self.dim for i in range(0,len(flatten_matrix),self.dim))):
      return(x_or_o)
    #check columns
    if any((all(flatten_matrix[i] == x_or_o for i in range(column,len(flatten_matrix),self.dim))) for column in range(self.dim)):
      return(x_or_o)

    #check left diagonals
    if (all(self.matrix[i][i] == x_or_o for i in range(self.dim))):
      return(x_or_o)

    #check right diagonals
    if all(self.matrix[i][self.dim-i-1] == x_or_o for i in range(self.dim)):
      return(x_or_o)
    return None

  def play(self, row_coord, col_coord):
    """
    Plays by placing either x or o token at the coordinate given (if valid) in the tic tac toe game
    Input format: row, column
    Checks for a winner

    """
    #function updates board state in self.matrix to token
    #self.dim is dimension of matrix
    #later will implement winner
    #take into account if input is a different type


    # while any(x==" " for x in self.matrix[i] for i in range(self.dim)):
    #add either x or o to a certain coordinate by updating the state

    #check rows/col/diagonals -- make sure to scales to other dimensions

    x_o = ["x","o"]
    try:
      if self.matrix[row_coord-1][col_coord-1] == " ":
        self.matrix[row_coord-1][col_coord-1] = x_o[Board.count]
        if self._winner("x") != None: print("X WINS")
        if self._winner("o") != None: print("O WINS")
      else:
        print("Coordinate is taken. Try Again.")
      if Board.count == 0: Board.count=1
      else: Board.count = 0
    except TypeError:
      print(f"coordinate inputs must be integers between 1 and {self.dim}. Try again.")
    except IndentationError:
      print(f"coordinate inputs must be integers between 1 and {self.dim}. Try Again.")
    return self.matrix




  def __repr__(self):
    return self.__str__()

b = Board(3)
(b.play(1,1))
(b.play(2,3))
(b.play(2,2))
b.play(1,2)
b.play(3,3)

print(b)

