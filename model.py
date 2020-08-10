import random

class Model:

    def randomRow(self):
        return random.randint(0, 2)
    
    def randomCol(self):
        return random.randint(0, 2)
    
    def compEntry(self):
        row = self.randomRow()
        col = self.randomCol()

        compRow = row
        compCol = 2 * col

        return compRow, compCol
    
    def invalidEntry(self):
        row = self.randomRow()
        col = self.randomCol()

        compRow = row
        compCol = 2 * col

        return compRow, compCol
    