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

        # operator priority
        def priority(operator):
            if operator in ('+', '-'): return 1
            if operator in ('*', '÷'): return 2
            return 0


        operators = []
        operands = []
        i = 0

        while i < len(textList):
            token = textList[i]
        
            # operand process
            if token.lstrip('-').isdigit():
                # token이 음수 또는 숫자인 경우, 해당 값을 정수로 변환하여 operands 스택에 추가
                val = int(token)
                operands.append(val)
                i += 1
            
            elif token == '(':
                operators.append(token)
                i += 1
            
            elif token == ')':
                while operators and operators[-1] != '(':
                    applyOperator(operators, operands)
                operators.pop()  # '(' 제거
                i += 1
            
            else:  # 연산자 처리
                while (operators and operators[-1] != '(' and
                    priority(operators[-1]) >= priority(token)):
                    applyOperator(operators, operands)
                operators.append(token)
                i += 1


        while operators:
            applyOperator(operators, operands)

        return operands[-1]
    
