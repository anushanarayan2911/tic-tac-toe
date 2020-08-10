from tkinter import *
from model import Model
from view import View

class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view 
        
    def showBoard(self):
        self.view.displayBoard()
    
    
