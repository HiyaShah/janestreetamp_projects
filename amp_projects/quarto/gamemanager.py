
from quarto import Board

class GameManagement:
  "Manages the TicTacToe Game State"

  def __init__(self, dim, player1_name, player2_name):
    self.board = Board()
    self.board.execute(player1_name, player2_name)



class Token:

  "Initializes Token"

  def __init__(self,color, shape, height, hole):
    """
    Initializes a token with color, shape, height, and hole in binary form (0 or 1)
    """
    possible_num = [0,1]
    if color in possible_num and shape in possible_num and height in possible_num and hole in possible_num:
        self.color = color
        self.shape = shape
        self.height = height
        self.hole = hole
    else:
        raise "inputs must be binary: 0 or 1"

  def __str__(self):
    return f"Color: {self.color} \n Shape: {self.shape} \n Height: {self.height} \n Hole: {self.hole}"

game = GameManagement(3, player1_name="Jim", player2_name="Todd")