"""
File: crapsgui.py
Project 9.7
Pops up a window that allows the user to play the game of craps.
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from craps import Player

class CrapsGUI(EasyFrame):
   
    def __init__(self):
        """Creates the player, and sets up the Images and labels
        for the two dice to be displayed, the text area for the
        game state, and the two command buttons."""
        EasyFrame.__init__(self, title = "Craps Game")
        self.setSize(220, 200)
        # Instantiate the model and initial values of the dice
        self.player = Player()
        self.v1 = 1
        self.v2 = 1
        # Add labels and buttons to the view
        self.dieLabel1 = self.addLabel("", row = 0,
                                       column = 0,
                                       sticky = "NSEW")
        self.dieLabel2 = self.addLabel("", row = 0,
                                       column = 1,
                                       sticky = "NSEW",
                                       columnspan = 2)
        self.stateArea = self.addTextArea("", row = 1, column = 0,
                                        columnspan = 2, width = 15,
                                        height = 5)
        self.rollButton = self.addButton(row = 2, column = 0,
                                         text = "Roll",
                                         command = self.nextRoll)
        self.addButton(row = 2, column = 1,
                       text = "New game",
                       command = self.newGame)
        self.refreshImages()

    def nextRoll(self):
        """Rolls the dice and updates the view with
        the results."""
        (self.v1, self.v2) = self.player.rollDice()
        total = self.v1 + self.v2
        self.stateArea.appendText("Total = " + str(total) + "\n")
        self.refreshImages()
        if self.player.isWinner():
            self.stateArea.appendText("You won!")
            self.rollButton["state"] = "disabled"
        elif self.player.isLoser():
            self.stateArea.appendText("You lose!")
            self.rollButton["state"] = "disabled"
            
    def newGame(self):
        """Create a new craps game and updates the view."""
        self.player = Player()
        self.v1 = 1
        self.v2 = 1
        self.stateArea.setText("")
        self.refreshImages()
        self.rollButton["state"] = "normal"
        
    def refreshImages(self):
        """Updates the images in the window."""
        fileName1 = "DICE/" + str(self.v1) + ".gif"
        fileName2 = "DICE/" + str(self.v2) + ".gif"
        self.image1 = PhotoImage(file = fileName1)
        self.dieLabel1["image"] = self.image1
        self.image2 = PhotoImage(file = fileName2)
        self.dieLabel2["image"] = self.image2

def main():
    CrapsGUI().mainloop()

if __name__ == "__main__":
    main()
