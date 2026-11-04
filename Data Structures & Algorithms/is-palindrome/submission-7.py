class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        
        return True

"""
Goal: Check if string is palindrome
- only consider alphanumeric vals
- dont care about uppser/lower case

initialise l and r pointer
while l < r:
    ensure l is valid alphanum and l < r
    ensure r is valid alphanum and r > l
    if l != r:
        return False
    move pointers
"""