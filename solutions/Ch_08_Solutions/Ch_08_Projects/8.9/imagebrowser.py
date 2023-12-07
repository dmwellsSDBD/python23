"""
File: imagebrowser.py
Project 8.9

Browser for image (.gif) files.
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
import tkinter.filedialog

class ImageBrowser(EasyFrame):

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Image Browser")

        self.imageLabel = self.addLabel(text = "", row = 0, column = 0,
                                        sticky = "NESW")
        self.addButton(text = "Find image", row = 1, column = 0,
                       command = self.findImage)

    def findImage(self):
        """Pops up an open file dialog, and if a file is
        selected, displays its image in the label and
        its pathname in the title bar."""
        fList = [("GIF files", "*.gif")]
        fileName = tkinter.filedialog.askopenfilename(parent = self,
                                                      filetypes = fList)
        if fileName != "":
            self.image = PhotoImage(file = fileName)
            self.imageLabel["image"] = self.image
            self.setTitle(fileName)

def main():
    """Instantiate and pop up the window."""
    ImageBrowser().mainloop()

if __name__ == "__main__":
    main()
