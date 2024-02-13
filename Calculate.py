# Calculate.py

class Calculate:
    def __init__(self):
        pass

    
    # Only calculate
    def infixCalculate(self, textList):
        # 입력된 숫자를 기반으로 중위표현식 계산 로직 생성
        
        # 각 부호별 연산 정의
        def applyOperator(ops, values):
            operator = ops.pop()
            right = values.pop()
            left = values.pop()
            if operator == '+': values.append(left + right)
            elif operator == '-': values.append(left - right)
            elif operator == '*': values.append(left * right)
            elif operator == '÷': values.append(left / right)

        # 우선순위
        def priority(op):
            if op in ('+', '-'): return 1
            if op in ('*', '÷'): return 2
            return 0


        operators = []
        operands = []
        i = 0

        while i < len(textList):
            if textList[i] == ' ':
                i += 1
                continue
            elif textList[i].isdigit():
                val = 0
                while i < len(textList) and textList[i].isdigit():
                    val = (val * 10) + int(textList[i])
                    i += 1
                operands.append(val)
                continue
            elif textList[i] == '(':
                operators.append(textList[i])
            elif textList[i] == ')':
                while operators and operators[-1] != '(':
                    applyOperator(operators, operands)
                operators.pop()  # Remove '('
            else:
                while (operators and operators[-1] != '(' and
                    priority(operators[-1]) >= property(textList[i])):
                    applyOperator(operators, operands)
                operators.append(textList[i])
            i += 1

        while operators:
            applyOperator(operators, operands)

        return operands[-1]
    
