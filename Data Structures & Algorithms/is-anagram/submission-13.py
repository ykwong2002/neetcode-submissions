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
Goal: return boolean if s and t are anagrams
- anagram means number of each letter are the same, order can be diff
- since s and t only have lowercase letters, 26 chars max (a-z)
- initialise freq array of chars
- compare both freq arrays
"""