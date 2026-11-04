class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d = [0] * 26 # at most 26 lower case english letters

        # go through s to populate d first
        for char in s:
            d[ord(char) - ord('a')] += 1
        
        # go through t
        for char in t:
            d[ord(char) - ord('a')] -= 1
        
        return d == [0]*26
"""
- compare s and t: compare freq of each letter
- if s and t not same length: definitely not anagram

brute force:
- sort both s and t
- from the start of each string, compare each index
- TC: O(nlogn)
- SC: O(1)
s   aaccerr
    ^
t   aaccerr
    ^

optimal method:
- for each string:
    - store a freq count
    - check if [0 0 0 0 ...]
- compare the freq counts
- TC: O(n)
- SC: O(1) # at most only 26 unique chars
"""