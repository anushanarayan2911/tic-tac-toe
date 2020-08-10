from tkinter import *
from model import Model
from view import View

class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view 
        self.view.OKButton.bind("<Button>", self.userTurn)
        
    def showBoard(self):
        self.view.displayBoard()
    
    def displayUserInputFields(self):
        self.view.displayInputFields()
        
    def displayOKButton(self):
        self.view.displayOKButton()
    
    def changeBoard(self, x, y, character):
        self.view.setBoardValue(x, y, character)
    
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
        