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
        
        # Create TextList manager instance 
        self.textList_manager = TextListManager()
        # Create calculator instance
        self.calculator = Calculate()
        
        # Number button list
        self.numButtonList = ["numButton_0", "numButton_1", "numButton_2", "numButton_3",
                         "numButton_4", "numButton_5", "numButton_6", "numButton_7",
                         "numButton_8", "numButton_9", "dotButton"]
        
        # Calculate button list
        self.calButtonList = ["addButton", "subButton", "mulButton", "divButton", "openButton", "closeButton"]
        
    
        # Number button clicked
        for button in self.numButtonList :
            button = getattr(self, button) # Use string, Access button instance
            button.clicked.connect(lambda ch, btn=button: self.textButtonClicked(btn.text())) 
        
        # Calculate button clicked
        for button in self.calButtonList :
            button = getattr(self, button) # Use string, Access button instance
            button.clicked.connect(lambda ch, btn=button: self.textButtonClicked(btn.text()))
        
        # "=" Button clicked
        self.sumButton.clicked.connect(self.sumButtonClicked)
        # "AC" Button clicked
        self.acButton.clicked.connect(self.acButtonClicked)
        # "C" Button clicked
        self.cButton.clicked.connect(self.cButtonClicked)
        # Screen reset to "0"
        self.calScreen.setText("0")
        # Result screen reset
        self.resultScreen.setText("")
        self.resultScreen.setReadOnly(True)


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
 
 
    # '=' button pressed
    def sumButtonClicked(self):
        # No Complete 
        if self.textList_manager.textList[-1] in '+-*÷(':
            pass
        
        # Complete
        else :
            # 1. Create process List
            #    combine numbers, confirm minus
            self.textList_manager.addProcessList()
            
            # 2. calculate 후 return 
            result = self.calculator.infixCalculate(self.textList_manager.processTextList)
            
            # 3. Screen setText
            self.calScreen.setText(str(result))
            
            # 4. Add result screen text
            expression = self.textList_manager.listToString()
            
            current_text = self.resultScreen.toPlainText()
            new_text = current_text + expression + '=' + str(result) + '\n'
            
            self.resultScreen.setPlainText(new_text)
            
            # 4. textList 초기화
            self.textList_manager.resetList()

        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    myWindows = WindowClass()
    
    myWindows.show()
    
    sys.exit(app.exec_())

