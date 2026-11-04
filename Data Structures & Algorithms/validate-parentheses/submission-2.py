class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        stack = []

        for char in s:
            if char in d.keys():
                stack.append(char)
            elif stack and char in d.values() and d.get(stack[-1]) == char:
                stack.pop(-1)
            else:
                return False
        
        return True if not stack else False