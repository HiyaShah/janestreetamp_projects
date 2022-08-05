class Board:
  """Represents a tic tac toe board"""
  count = 0
  def __init__(self):
    """Creates a dim by dim size tictactoe board
    """
    self.dim = 4 #dimension of matrix
    self.matrix = [[" "]*self.dim for i in range(self.dim)] #matrix is under abstraction

  @staticmethod
  def row_str(row):
    "Helper method to turn each row into a string representation"
    return " "+" | ".join(row) +" \n"

  def __str__(self):
    "Creates a string representation of Board"
    string_row = [Board.row_str(row) for row in self.matrix]
    hrule = ["---"*self.dim +"-"*(self.dim-1)+"\n" for i in range(self.dim)]
    # return hrule.join(string_row)
    grid = ""
    for i in range(len(string_row)):
      grid+=(string_row[i])
      if i<len(string_row)-1:
        grid+=(hrule[i])
    return grid

  def winner(self,x_or_o):
    #other ways: dead state, checking only the last changed token
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

  def execute(self, name1, name2):

    """
    Executes the play function by asking a user for row and column coordinates
    Accepts names of both players
    
    """
    count = 0
    x_o = ["x","o"]
    while True:
      print(self)

      try:
        
        name = name1 if count == 0 else name2
        row_coord = input(f"{name}, please enter a row coordinate to place your token {x_o[count]}: ")
        col_coord = input(f"{name}, please enter a column coordinate to place your token {x_o[count]}: ")
        result = self.play(x_o[count], int(row_coord), int(col_coord))
        
        if result: 
          print(f"{result} won!")
          break

        count = 1 if count == 0 else 0 

      except TypeError:
        print(f"coordinate inputs must be integers between 1 and {self.dim}. Try again.")
      

  def play(self, token, row_coord, col_coord):

    """
    Plays by placing either x or o token at the coordinate given (if valid) in the tic tac toe game
    Input format: row, column
    Checks for a winner

    """

    if self.matrix[row_coord-1][col_coord-1] == " ":
      self.matrix[row_coord-1][col_coord-1] = token
      return self.winner(token)  
      
    else:
      print("Coordinate is taken. Try Again.")
      
     
      
  
  def __repr__(self):
    return self.__str__()


    
class GameManagement:
  "Manages the TicTacToe Game State"

  def __init__(self, dim, player1_name, player2_name):
    self.dim = dim
    self.player1_name = player1_name
    self.token1= "x"
    self.player2_name = player2_name
    self.token2 = "o"
    self.board = Board(self.dim)
    self.player1 = Player(self.player1_name)
    self.player2 = Player(self.player2_name)
    self.board.execute(player1_name, player2_name)



class Player:

  "Initializes Player"

  def __init__(self,name):
    self.name = name
    self.winning_streak = 0

  def __str__(self):
    return f"My name is {self.name} and I have a winning streak of {self.winning_streak}"

game = GameManagement(3, player1_name="Jim", player2_name="Todd")

  








