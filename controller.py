from tkinter import *
from model import Model
from view import View

class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view 
        self.view.OKButton.bind("<Button>", self.userTurn)
        self.view.nextButton.bind("<Button>", self.compTurn)
        
    def showBoard(self):
        self.view.displayBoard()
    
    def displayUserInputFields(self):
        self.view.displayInputFields()
        
    def displayOKButton(self):
        self.view.displayOKButton()
    
    def changeBoard(self, x, y, character):
        self.view.setBoardValue(x, y, character)
    
    def checkIfGameOver(self):
        currentRow1 = self.view.row1.get()
        row1List = list(currentRow1)
        currentRow2 = self.view.row2.get()
        row2List = list(currentRow2)
        currentRow3 = self.view.row3.get()
        row3List = list(currentRow3)

        if row1List[0] == row1List[2] == row1List[4]:
            return True, row1List[0]
        elif row2List[0] == row2List[2] == row2List[4]:
            return True, row2List[0]
        elif row3List[0] == row3List[2] == row3List[4]:
            return True, row3List[0]
        elif row1List[0] == row2List[0] == row3List[0]:
            return True, row1List[0]
        elif row1List[2] == row2List[2] == row3List[2]:
            return True, row1List[2]
        elif row1List[4] == row2List[4] == row3List[4]:
            return True, row1List[4]
        elif row1List[0] == row2List[2] == row3List[4]:
            return True, row1List[0]
        elif row1List[4] == row2List[2] == row3List[0]:
            return True, row1List[4]
        else:
            return False, " "
    
    def endGame(self, character):
        if character == "X":
            self.view.displayLoseMessage()
        elif character == "O":
            self.view.displayWinMessage()
    
    def userTurn(self, event):
        row = self.view.userRow.get()
        col = self.view.userCol.get()

        userRow = row
        userCol = (2 * col) - 2

        if userRow == 1:
            currentRow1 = self.view.row1.get()
            currentRow1List = list(currentRow1)
            if currentRow1List[userCol] == "X" or currentRow1List[userCol] == "O":
                self.view.displayInvalidInput()
            else:
                self.changeBoard(userRow, userCol, "O")
                self.view.forgetInputFields()
                self.view.forgetOKButton()
                self.view.displayNextButton()

        elif userRow == 2:
            currentRow2 = self.view.row2.get()
            currentRow2List = list(currentRow2)
            if currentRow2List[userCol] == "X" or currentRow2List[userCol] == "O":
                self.view.displayInvalidInput()
            else:
                self.changeBoard(userRow, userCol, "O")
                self.view.forgetInputFields()
                self.view.forgetOKButton()
                self.view.displayNextButton()

        elif userRow == 3:
            currentRow3 = self.view.row3.get()
            currentRow3List = list(currentRow3)
            if currentRow3List[userCol] == "X" or currentRow3List[userCol] == "O":
                self.view.displayInvalidInput()
            else:
                self.changeBoard(userRow, userCol, "O")
                self.view.forgetInputFields()
                self.view.forgetOKButton()
                self.view.displayNextButton()
        
        result, character = self.checkIfGameOver()
        if result:
            if character == "X" or character == "O":
                self.endGame(character)
    
    def compTurn(self, event):
        self.view.forgetNextButton()
        compRow, compCol = self.model.compEntry()

        if compRow == 1:
            currentRow1 = self.view.row1.get()
            currentRow1List = list(currentRow1)
            while currentRow1List[compCol] == "X" or currentRow1List[compCol] == "O":
                self.model.invalidEntry()

            self.changeBoard(compRow, compCol, "X")
            self.displayUserInputFields()
            self.displayOKButton()

        elif compRow == 2:
            currentRow2 = self.view.row2.get()
            currentRow2List = list(currentRow2)
            while currentRow2List[compCol] == "X" or currentRow2List[compCol] == "O":
                self.model.invalidEntry()

            self.changeBoard(compRow, compCol, "X")
            self.displayUserInputFields()
            self.displayOKButton()
        
        elif compRow == 3:
            currentRow3 = self.view.row3.get()
            currentRow3List = list(currentRow3)
            while currentRow3List[compCol] == "X" or currentRow3List[compCol] == "O":
                self.model.invalidEntry()
            
            self.changeBoard(compRow, compCol, "X")
            self.displayUserInputFields()
            self.displayOKButton()
        
        result, character = self.checkIfGameOver()
        if result:
            if character == "X" or character == "O":
                self.endGame(character)