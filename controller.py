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
    
    def displayStartingStatements(self):
        self.view.displayStartingStatements()
    
    def displayUserInputFields(self):
        self.view.displayInputFields()
        
    def displayOKButton(self):
        self.view.displayOKButton()
    
    def displayNextButton(self):
        self.view.displayNextButton()
    
    def forgetOKButton(self):
        self.view.forgetOKButton()
    
    def forgetNextButton(self):
        self.view.forgetNextButton()
    
    def forgetInvalidInputMessage(self):
        self.view.forgetInvalidInputMessage()
    
    def forgetStartingStatements(self):
        self.view.forgetStartingStatements()
    
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
        self.forgetStartingStatements()
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
                self.forgetInvalidInputMessage()
                self.changeBoard(userRow, userCol, "O")
                self.view.forgetInputFields()
                self.forgetOKButton()
                self.displayNextButton()

        elif userRow == 2:
            currentRow2 = self.view.row2.get()
            currentRow2List = list(currentRow2)
            if currentRow2List[userCol] == "X" or currentRow2List[userCol] == "O":
                self.view.displayInvalidInput()
            else:
                self.forgetInvalidInputMessage()
                self.changeBoard(userRow, userCol, "O")
                self.view.forgetInputFields()
                self.forgetOKButton()
                self.displayNextButton()

        elif userRow == 3:
            currentRow3 = self.view.row3.get()
            currentRow3List = list(currentRow3)
            if currentRow3List[userCol] == "X" or currentRow3List[userCol] == "O":
                self.view.displayInvalidInput()
            else:
                self.forgetInvalidInputMessage()
                self.changeBoard(userRow, userCol, "O")
                self.view.forgetInputFields()
                self.forgetOKButton()
                self.displayNextButton()
        
        result, character = self.checkIfGameOver()
        if result:
            if character == "X" or character == "O":
                self.forgetNextButton()
                self.endGame(character)
        
        elif result == False:
            currentRow1 = self.view.row1.get()
            currentRow1List = list(currentRow1)
            currentRow2 = self.view.row2.get()
            currentRow2List = list(currentRow2)
            currentRow3 = self.view.row3.get()
            currentRow3List = list(currentRow3)
            currentBoardList = []
            counter = 0

            for i in range(len(currentRow1List)):
                currentBoardList.append(currentRow1List[i])
            for j in range(len(currentRow2List)):
                currentBoardList.append(currentRow2List[j])
            for k in range(len(currentRow3List)):
                currentBoardList.append(currentRow3List[k])
            
            for n in range(len(currentBoardList)):
                if currentBoardList[n] == "_":
                    counter += 1

            if counter == 0:
                self.view.displayTieMessage()
                self.forgetNextButton()

    
    def checkForValidCompInput(self, x, y):
        if x == 1:
            currentRow1 = self.view.row1.get()
            row1List = list(currentRow1)
            if row1List[y] == "O" or row1List[y] == "X":
                return False
        
        elif x == 2:
            currentRow2 = self.view.row2.get()
            row2List = list(currentRow2)
            if row2List[y] == "O" or row2List[y] == "X":
                return False
        
        elif x == 3:
            currentRow3 = self.view.row3.get()
            row3List = list(currentRow3)
            if row3List[y] == "O" or row3List[y] == "X":
                return False
        
        else:
            return True

    def compTurn(self, event):
        compRow, compCol = self.model.compEntry()

        while self.checkForValidCompInput(compRow, compCol) == False:
            compRow, compCol = self.model.compEntry()

        self.changeBoard(compRow, compCol, "X")
        self.displayUserInputFields()
        self.displayOKButton()

        self.forgetNextButton()

        result, character = self.checkIfGameOver()
        if result:
            if character == "X" or character == "O":
                self.endGame(character)
                self.view.forgetInputFields()
                self.forgetOKButton()

        elif result == False:
            
            currentRow1 = self.view.row1.get()
            currentRow1List = list(currentRow1)
            currentRow2 = self.view.row2.get()
            currentRow2List = list(currentRow2)
            currentRow3 = self.view.row3.get()
            currentRow3List = list(currentRow3)
            currentBoardList = []
            counter = 0

            for i in range(len(currentRow1List)):
                currentBoardList.append(currentRow1List[i])
            for j in range(len(currentRow2List)):
                currentBoardList.append(currentRow2List[j])
            for k in range(len(currentRow3List)):
                currentBoardList.append(currentRow3List[k])
            
            for n in range(len(currentBoardList)):
                if currentBoardList[n] == "_":
                    counter += 1

            if counter == 0:
                self.view.displayTieMessage()
                self.view.forgetInputFields()
                self.forgetOKButton()