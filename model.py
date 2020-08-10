import random

class Model:

    def randomRow(self):
        return random.randint(0, 2)
    
    def randomCol(self):
        return random.randint(0, 2)
    
    def compEntry(self):
        row = self.randomRow() + 1
        col = self.randomCol() + 1

        compRow = row 
        compCol = (2 * col) - 2

        return compRow, compCol