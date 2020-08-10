from tkinter import *
from view import View
from model import Model
from controller import Controller

def main():
    screen = Tk()
    screen.title("Tic Tac Toe")
    screen.geometry("500x500")

    model = Model()
    view = View(screen)
    controller = Controller(model, view)

    controller.showBoard()
    controller.displayUserInputFields()
    controller.displayOKButton()

    screen.mainloop()

if __name__ == "__main__":
    main()