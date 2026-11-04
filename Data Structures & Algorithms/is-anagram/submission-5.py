class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Create an array for each letter
        s_dict = [0] * 26
        t_dict = [0] * 26

        for i in range(len(s)):
            s_dict[ord(s[i]) - ord('a')] += 1
            t_dict[ord(t[i]) - ord('a')] += 1
        
        return s_dict == t_dict
