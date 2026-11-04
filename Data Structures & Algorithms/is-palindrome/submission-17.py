class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1

        while l < r:
            # skip non-alphanum chars
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
"""
Goal: return true if string is palindrome
- initialise l and r pointers
- check if they are the same
"""