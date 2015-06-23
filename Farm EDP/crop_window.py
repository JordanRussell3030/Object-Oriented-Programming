import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class CropWindow(QMainWindow):
    """This class creates a main window to observe the growth of a simulation"""
    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop Simulator") # set window title

def main():
    crop_simulation = QApplication(sys.argv) #create new application
    crop_window = CropWindow() #create new instance of window
    crop_window.show() #makes it visible
    crop_window.raise_() #raise to top of window stack
    crop_simulation.exec_() #monitor app for events

if __name__ == "__main__":
    main()
