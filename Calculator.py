### 계산기
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from TextListManager import TextListManager
from Calculate import Calculate

from_class = uic.loadUiType("Calculator.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.setWindowTitle("PyQt Calculator")
        
        # TextList manager instance 
        self.textList_manager = TextListManager()
        
        
        # Number button list
        self.numButtonList = ["numButton_0", "numButton_1", "numButton_2", "numButton_3",
                         "numButton_4", "numButton_5", "numButton_6", "numButton_7",
                         "numButton_8", "numButton_9", "dotButton"]
        
        # Calculate button list
        self.calButtonList = ["addButton", "subButton", "mulButton", "divButton"]
        
    
        # Number button clicked
        for button in self.numButtonList :
            button = getattr(self, button) # Use string, Access button instance
            button.clicked.connect(lambda ch, btn=button: self.textButtonClicked(btn.text())) 
        
        # Calculate button clicked
        for button in self.calButtonList :
            button = getattr(self, button) # Use string, Access button instance
            button.clicked.connect(lambda ch, btn=button: self.textButtonClicked(btn.text()))
        
        # "=" Button clicked
        self.sumButton.clicked.connect(lambda: self.sumButtonClicked(self.sumButton.text()))
        # "AC" Button clicked
        self.acButton.clicked.connect(self.acButtonClicked)
        # "C" Button clicked
        self.cButton.clicked.connect(self.cButtonClicked)
        # Screen reset to "0"
        self.calScreen.setText("0")


    def textButtonClicked(self, text):
        # Add text to list
        self.textList_manager.addList(text)
        
        # To take a Screen, Convert String
        result = self.textList_manager.listToString()
        
        # Screen setText
        self.calScreen.setText(result)


    def acButtonClicked(self):
        self.textList_manager.resetList()
        # To take a Screen, Convert String
        result = self.textList_manager.listToString()
        
        # Screen setText
        self.calScreen.setText(result)
        
        
    def cButtonClicked(self):
        self.textList_manager.removeList()
        
        # To take a Screen, Convert String
        result = self.textList_manager.listToString()
        
        # Screen setText
        self.calScreen.setText(result)
        
    
        
        
    def sumButtonClicked(self, text):
        if (self.textList_manager.textList[-1] != "+-*÷" ):
            pass #게산식 추가
        else:
            pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    myWindows = WindowClass()
    
    myWindows.show()
    
    sys.exit(app.exec_())
    
# numButton_0 ~ numButton_9
# dotButton
# sumButton
# addButton
# divButton
# mulButton
# subButton
# calScreen
# resultScreen
