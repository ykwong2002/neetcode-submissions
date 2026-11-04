class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for c in s:
            if c.isalnum():
                cleaned += c
        
        cleaned = cleaned.lower()

        return cleaned == cleaned[::-1]

"""
Goal: Check if string is palindrome
- only consider alphanumeric vals
- dont care about uppser/lower case

clean:
- remove all non-alphanum vals (check ascii or use isalnum())
- convert all to lower case (.lower())
- return if s == s[::-1]
"""