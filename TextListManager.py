# TextListManager.py
from Validator import Validator

class TextListManager:
    def __init__(self, validator=Validator):
        self.validator = validator
        self.textList = ["0"]
    
    # Judgment condition and correction
    def preprocess_text(self, text):
        
        operator = ["+", "-", "*", "÷"]
        
        # Judgment Operator, Operand 
        isOperator = text in operator # 새로 들어온 텍스트가 연산자인가?
        beforeIsOperator = self.textList[-1] in operator # 전 텍스트가 연산자인가?
        
        # Operator process       
        if isOperator and beforeIsOperator: # 새로 들어온 텍스트도 연산자이고, 전 텍스트도 연산자이면
            if (text == self.textList[-1]): # 두 연산자가 같다면 리스트에 추가 안함
                return False
            else: # 두 연산자가 다르다면
                if (text == '-'): # 들어온 텍스트가 '-'라면
                    return True
                else: # 들어온 텍스트가 '-'가 아니라면
                    self.removeList() # 마지막 값을 지우고 대체
                    return True
                
                
        # Operand process
        else: 
            # 현재 입력이 연산자이지만 직전 입력이 연산자가 아니거나,
            # 현재 입력이 피연산자인 경우
            if (len(self.textList) == 1): # 리스트에 초기값이 있는데, 
                if (self.textList[-1] == "0"): # 리스트 초기값이 0이라면
                    if (isOperator):
                        return True
                    
                    elif (text != "0"): # 입력 텍스트가 0이 아닌 경우에만 append
                        self.textList = [] # 리스트를 비운 후 append
                        return True
                    
                    else: # 입력 텍스트가 0이면
                        return False
                
                else: # 리스트 길이가 1이지만 값은 0이 아니다.
                        return True
            
            else:
                return True
            
        
    # text input list 
    def addList(self, text):
        # Text must pass, append
        if (self.preprocess_text(text)):
            self.textList.append(text)
            
        # check List
        print(self.textList)
        
    
    # text Input remove list
    def removeList(self):
        if (len(self.textList) == 1 and self.textList[-1] == 0):
            self.textList = ["0"]
        elif (len(self.textList) == 0):
            self.textList = ["0"]
        else:
            top = self.textList.pop() # last element remove
            print("Top element remove", top)
            if (len(self.textList) == 0):
                self.textList = ["0"]
    
    
    # All text delete
    def resetList(self):
        self.textList = ["0"]
    
    
    # Text convert to String
    def listToString(self):
        result = ""
        
        for str in self.textList:
            result += str
        
        return result
 
    