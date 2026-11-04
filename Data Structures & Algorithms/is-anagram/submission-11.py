class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = [0] * 26
        t_count = [0] * 26

        # initialise values
        for c in s:
            s_count[ord(c) - ord('a')] += 1
        for c in t:
            t_count[ord(c) - ord('a')] += 1
        
        return s_count == t_count

"""
Goal: return True is s and t are anagrams
- anagram --> same number of each char
- maintain an array of counts (since only lowercase english letters)
    - for both s and t
- compare if they are the same
"""