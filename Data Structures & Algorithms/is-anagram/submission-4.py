class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = [0] * 26
        t_map = [0] * 26
        
        for char in s:
            s_map[ord(char) - ord('a')] += 1
        
        for char in t:
            t_map[ord(char) - ord('a')] += 1
        
        return s_map == t_map