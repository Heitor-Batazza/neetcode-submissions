class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        while tokens != []:
            if tokens[0] not in operators:
                stack.append(int(tokens[0]))
                tokens.pop(0)
            elif tokens[0] in operators:
                number2 = stack.pop() 
                number1 = stack.pop() 
                
                if tokens[0] == "+":
                    stack.append(number1 + number2)
                elif tokens[0] == "-":
                    stack.append(number1 - number2)
                elif tokens[0] == "*":
                    stack.append(number1 * number2)
                elif tokens[0] == "/":
                    stack.append(int(number1 / number2))
                tokens.pop(0)

        return stack[0]

        