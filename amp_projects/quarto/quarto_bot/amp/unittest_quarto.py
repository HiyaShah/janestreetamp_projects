
import quarto
import unittest

class Test(unittest.TestCase):
    def test_winner(self):
        b = quarto.Board()
        
        b.matrix[0][3] = "gggg"
        b.matrix[1][2] = "gggg"
        b.matrix[2][1] = "gfff"
        b.matrix[3][0] = "gjff"
        self.assertEqual(b.winner("g"),"g")
    
if __name__ == '__main__':
    unittest.main()