class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                num_1 = stack.pop()
                num_2 = stack.pop()
                stack.append(num_1 + num_2)
            elif token == "-":
                num_1 = stack.pop()
                num_2 = stack.pop()
                stack.append(num_2 - num_1)
            elif token == "*":
                num_1 = stack.pop()
                num_2 = stack.pop()
                stack.append(num_1 * num_2)
            elif token == "/":
                num_1 = stack.pop()
                num_2 = stack.pop()
                stack.append(int(num_2 / num_1))
            else:
                stack.append(int(token))
        return stack[0]
"""
Goal: evaluate RPN expression.
- if num, push onto stack
- if operator, take out last 2 numbers, perform op, push answer onto stack
"""