class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                number2, number1 = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(number1 + number2)
                elif token == "-":
                    stack.append(number1 - number2)
                elif token == "*":
                    stack.append(number1 * number2)
                elif token == "/":
                    stack.append(int(number1 / number2))
        return stack[0]

        