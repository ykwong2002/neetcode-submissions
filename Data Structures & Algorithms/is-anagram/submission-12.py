class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = [0] * 26
        t_count = [0] * 26

        # initialise the count arrays
        for char in s:
            s_count[ord(char) - ord('a')] += 1
        for char in t:
            t_count[ord(char) - ord('a')] += 1
        
        return s_count == t_count
"""
Goal: return true if s and t are anagrams, else false
- anagrams: they have same character counts
- can use a dictionary (freqmap)
    - but since only lowercase english alphabets, can use array of 26 chars ( one for each letter)
    - value at that index is the count
"""