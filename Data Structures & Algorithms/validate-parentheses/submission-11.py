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
            elif char in d.values():
                if not stack:
                    return False
                latest = stack.pop()
                if d[latest] != char:
                    return False
        
        return not stack