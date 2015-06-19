from PyQt4.QtGui import *

class RadioButtonWidget(QWidget):
    """this class creates a group of radio buttons from a given list of labels"""
    #constructor
    def __init__(self, label, instruction, button_list):
        super().__init__()

        #create widgets
        self.title_label = QLabel(label)
        self.radio_group_box = QGroupBox(instruction)

        #4 mins 30 through task 2a
    



