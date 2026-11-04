class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = [0] * 26
        t_freq = [0] * 26

        for char in s:
            s_freq[ord(char) - ord('a')] += 1
        
        for char in t:
            t_freq[ord(char) - ord('a')] += 1
        
        return s_freq == t_freq
"""
Goal: check if 2 strings are anagram so each other
- create a frequency array for both strings
- compare equality at the end
"""