from tkinter import *

class View:
    
    def __init__(self, screen):
        self.screen = screen
        self.row1 = StringVar()
        self.row2 = StringVar()
        self.row3 = StringVar()
        
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
    
    
