# TextListManager.py

class TextListManager:
    def __init__(self):
        self.textList = ["0"]
        self.processTextList = []
        self.operator = ["+", "-", "*", "÷"]
    
    
    # Judgment condition and correction
    def preprocess_text(self, text):
        
        # Judgment Operator, Operand 
        isOperator = text in self.operator # 새로 들어온 텍스트가 연산자인가?
        beforeIsOperator = self.textList[-1] in self.operator # 전 텍스트가 연산자인가?
        
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
    
    
    # Combine text numbers (operand)
    def combineNumbers(self, text_list):
        combined_list = []
        current_number = ""

        for item in text_list:
            if item.isdigit():  # 아이템이 숫자 문자열인 경우
                current_number += item  # 현재 숫자 문자열에 추가
            else:  # 아이템이 연산자인 경우
                if current_number:  # 현재 숫자 문자열이 비어있지 않다면
                    combined_list.append(current_number)  # 현재까지의 숫자 문자열을 리스트에 추가
                    current_number = ""  # 현재 숫자 문자열을 초기화
                combined_list.append(item)  # 연산자를 리스트에 추가

        if current_number:  # 마지막에 남은 숫자 문자열이 있다면 리스트에 추가
            combined_list.append(current_number)

        print(combined_list)
        return combined_list
    
    
    
    # '-'가 음수 부호인지, 연산자인지 판단
    def confirmMinus(self, process_list):
        result = []
        i = 0

        while i < len(process_list):
            token = process_list[i]
            next_token = process_list[i + 1] if i + 1 < len(process_list) else None

            # 첫 토큰이 '-'이거나, 연산자 뒤에 '-'가 오는 경우 음수 부호로 처리
            if token == '-' and (i == 0 or (i > 0 and process_list[i - 1] in self.operator)):
                result.append('-' + next_token)
                i += 2  # 다음 토큰도 처리했으므로 인덱스 2 증가
            elif next_token == '-' and token in self.operator:
                # 다음 토큰이 '-'이고, 현재 토큰이 연산자인 경우
                result.append(token)  # 현재 연산자를 결과에 추가
                result.append('-' + process_list[i + 2])  # 음수 부호와 다음 숫자를 결합
                i += 3  # 다음 숫자까지 처리했으므로 인덱스 3 증가
            else:
                result.append(token)
                i += 1

        print(result)
        return result

    
    
    # 리스트를 숫자 합치고, 마이너스 부호 판단해서 최종 list 생성
    def addProcessList(self):
        self.processTextList = self.combineNumbers(self.textList)
        self.processTextList = self.confirmMinus(self.processTextList)
        