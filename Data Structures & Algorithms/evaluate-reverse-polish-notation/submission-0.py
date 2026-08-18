class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif token == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif token == '/':
                b = stack.pop()
                a = stack.pop()
                # Truncate toward zero
                result = int(a / b)
                stack.append(result)
            else:
                # It's a number
                stack.append(int(token))
        
        return stack[0]