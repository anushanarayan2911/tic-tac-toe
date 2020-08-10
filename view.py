from tkinter import *

class View:
    
    def __init__(self, screen):
        self.screen = screen
        self.row1 = StringVar()
        self.row2 = StringVar()
        self.row3 = StringVar()
        self.promptRowEntry = Label(self.screen, text = "Enter Row")
        self.promptColEntry = Label(self.screen, text = "Enter Column")
        self.userRow = IntVar()
        self.userCol = IntVar()
        self.OKButton = Button(self.screen, text = "OK")
        self.invalidInputMessage = Label(self.screen, text = "Invalid Input. Please enter another row/column above.")
        self.nextButton = Button(self.screen, text = "Next")
        self.userWinsGameMessage = Label(self.screen, text = "You win!")
        self.userLosesGameMessage = Label(self.screen, text = "You lose!")

    def displayBoard(self):
        dashes = ""
        for i in range(3):
            dashes += "_ "
        
        self.row1.set(dashes)
        self.row2.set(dashes)
        self.row3.set(dashes)

        self.row1Label = Label(self.screen, textvariable = self.row1)
        self.row2Label = Label(self.screen, textvariable = self.row2)
        self.row3Label = Label(self.screen, textvariable = self.row3)

        self.row1Label.pack()
        self.row2Label.pack()
        self.row3Label.pack()
    
    def displayInputFields(self):
        self.promptRowEntry.pack()
        self.rowInputField = Entry(self.screen, textvariable = self.userRow)
        self.rowInputField.pack()

        self.promptColEntry.pack()
        self.colInputField = Entry(self.screen, textvariable = self.userCol)      
        self.colInputField.pack()
        Label(self.screen, text = " ").pack()
    
    def displayOKButton(self):
        self.OKButton.pack()
    
    def displayNextButton(self):
        self.nextButton.pack()
    
    def displayInvalidInput(self):
        self.invalidInputMessage.pack()
    
    def displayWinMessage(self):
        self.userWinsGameMessage.pack()
    
    def displayLoseMessage(self):
        self.userLosesGameMessage.pack()

    def setBoardValue(self, x, y, character):
        if x == 1:
            currentRow1 = self.row1.get()
            currentRow1List = list(currentRow1)
            currentRow1List[y] = character

            updatedRow1List = "".join(currentRow1List)
            self.row1.set(updatedRow1List)

        elif x == 2:
            currentRow2 = self.row2.get()
            currentRow2List = list(currentRow2)
            currentRow2List[y] = character

            updatedRow2List = "".join(currentRow2List)
            self.row2.set(updatedRow2List)

        elif x == 3:
            currentRow3 = self.row3.get()
            currentRow3List = list(currentRow3)
            currentRow3List[y] = character

            updatedRow3List = "".join(currentRow3List)
            self.row3.set(updatedRow3List)
        
    def forgetInputFields(self):
        self.promptRowEntry.pack_forget()
        self.promptColEntry.pack_forget()
        self.rowInputField.pack_forget()
        self.colInputField.pack_forget()
    
    def forgetOKButton(self):
        self.OKButton.pack_forget()

    def forgetNextButton(self):
        self.nextButton.pack_forget()
    
    def forgetInvalidInputMessage(self):
        self.invalidInputMessage.pack_forget()