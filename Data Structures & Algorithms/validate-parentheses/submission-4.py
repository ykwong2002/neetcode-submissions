class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []

        for c in s:
            if c in d.values():
                stack.append(c)
            elif c in d.keys():
                if stack and stack[-1] == d[c]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False