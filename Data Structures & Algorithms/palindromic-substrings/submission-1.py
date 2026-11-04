class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            # check odd length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            # check even length palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        
        return count
"""
Goal: return number of palindromic substrings
- even a single letter is considered a palindromic substring
- from each char, expand outward and add to count
"""