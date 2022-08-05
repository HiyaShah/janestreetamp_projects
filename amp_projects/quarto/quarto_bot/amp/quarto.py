import itertools
import random

class Board:
  """Creates a quarto board"""
  def __init__(self):
    """Creates a dim by dim size quarto board
    """
    self.dim = 4
    
    self.matrix = [["    "]*self.dim for i in range(self.dim)] #matrix is under abstraction
    self.tokens = self.create_tokens()
    
  "Representations of the Quarto Board"
  @staticmethod
  def row_str(row):
    "Helper method to turn each row into a string representation"
    return " "+" | ".join(row) +" \n"

  
  def __str__(self):
    "Creates a string representation of Board"
    string_row = [Board.row_str(row) for row in self.matrix]
    hrule = ["------"*self.dim +"-"*(self.dim-1)+"\n" for i in range(self.dim)]
    # return hrule.join(string_row)
    grid = ""
    for i in range(len(string_row)):
      grid+=(string_row[i])
      if i<len(string_row)-1:
        grid+=(hrule[i])
    return grid

  def __repr__(self):
    return self.__str__()
  
  def create_tokens(self):
        patterns = (list(itertools.product("01", repeat=4)))
        lst = [Token([int(color) for color in lst_colors]) for lst_colors in patterns]
        return lst

  def __getitem__(self,idx):
    return self.matrix[idx]

  
  def winner(self, letter):
    "Checks for a winner given the letter to check (not to be used by the user)"
    flatten_matrix = [val for row in self.matrix for val in row]

    #check rows 2.0
    if any(all(letter in elem for elem in flatten_matrix[i:self.dim+i]) for i in range(0,len(flatten_matrix),self.dim)):
      return(letter)

    #check columns 2.0
    if any((all(letter in flatten_matrix[i] for i in range(column,len(flatten_matrix),self.dim))) for column in range(self.dim)):
      return(letter)

    #check left diagonals
    if (all(letter in self.matrix[i][i] for i in range(self.dim))):
      return(letter)

    #check right diagonals
    if all(letter in self.matrix[i][self.dim-i-1] for i in range(self.dim)):
      return(letter)
    return None

  """
  Open Positions in Self.Matrix
  """
  def is_open_position(self,row_coord, col_coord):
    return self.matrix[row_coord-1][col_coord-1] == "    "
    
  def get_open_position(self):
    row = random.randint(1,4)
    col = random.randint(1,4)
    while self.is_open_position(row, col) is not True:
        row = random.randint(1,4)
        col = random.randint(1,4)
    return (row, col)

  def play(self, token, row_coord, col_coord):

    """
    Executes the play function by asking a user for row and column coordinates
    
    """

    print(self)
    if self.is_open_position(row_coord, col_coord):
      self.matrix[row_coord-1][col_coord-1] = token
      result= self.winner(token[0]) or self.winner(token[1]) or self.winner(token[2]) or self.winner(token[3])
      if result: 
        print(f"{result} won!")
      
      
  
  

class GameManagement:
    "Manages the Quarto Game State"
    
    def __init__(self):
        
        self.board = Board()
        self.player0 = Player()
        self.player1 = Player()
        self.counter = 0
        self.currentPlayer = self.player0

    def get_current_player(self):
      player = self.player0 if self.currentPlayer == 0 else self.player1
      self.currentPlayer = player
      return self.currentPlayer

    def update_current_player(self):
      self.counter = 0 if self.counter == 1 else 1

    def pick_and_play(self):
      piece = self.get_current_player().pick(self.board.tokens)
      self.get_current_player().play(piece, self.board)
      self.board.tokens.remove(piece)
    
    def random_solver(self):
      for i in range(16):
        self.pick_and_play()
    
    # def pick_and_play(self):
    #   piece = self.get_current_player().pick(self.board.tokens)
    #   coord = self.board.get_open_position()
    #   row, col = coord[0], coord[1]
    #   self.get_current_player().play(piece, row, col)
    #   self.board.tokens.remove(piece)
    

class Player:

  def __init__(self):
    pass

  def pick(self, board):
    "Picks a piece for the game from the valid remaining pieces"
    piece = random.choice(board) 
    return piece

  def play(self,piece,board):
    "Plays the piece on a free board square"
    print(board)
    coord = board.get_open_position()
    print(coord)
    row, col = coord[0], coord[1]
    board.matrix[row-1][col-1] = str(piece) 
    str_piece = str(piece)
    result= [board.winner(str_piece[i]) for i in range(0,4,1) if board.winner(str_piece[i]) is not None]
    if any(result): 
      print(f"{result} won!")
    print(board)
  
  
class SmartPlayer(Player):

  def __init__():
    super().__init__()
  
  def play():
    pass

  def win_strategy():
    pass

  def dont_lose_strategy():
    pass

  def game_tree():
    pass

  def pick():
    pass

class Token:

    "Initializes Token"

    def __init__(self, args):
        self.color = args[0]
        self.shape = args[1]
        self.height = args[2]
        self.hole = args[3]
        

    def __str__(self):
        color = "black" if self.color ==0 else "white"
        shape = "circle" if self.shape ==0 else "rectangle"
        height = "short" if self.height ==0 else "tall"
        hole = "no" if self.hole ==0 else "yes"
        return "{}{}{}{}".format(color[0],shape[0],height[0],hole[0])
        # return f"{self.color}{self.shape}{self.height}{self.hole}"

    def get_token(self):
      return (f"{self.color}{self.shape}{self.height}{self.hole}")

g = GameManagement()
g.random_solver()



  








