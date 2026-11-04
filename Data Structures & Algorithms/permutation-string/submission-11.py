class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Exception
        if len(s1) > len(s2):
            return False
        
        # Create freq array of s1
        s1_freq = [0] * 26
        for c in s1:
            s1_freq[ord(c) - ord('a')] += 1

        # Sliding window of FIXED LENGTH in s2
        for l in range(0, len(s2) - len(s1) + 1):
            r = l + len(s1)
            s2_freq = [0] * 26
            for i in range(l, r):
                s2_freq[ord(s2[i]) - ord('a')] += 1
            
            if s1_freq == s2_freq:
                return True
        
        return False
            


            


"""
Goal: check if a permutation of s1 exists in s2
- create freq array of s1
- use sliding window of FIXED LENGTH (s1.length) in s2
- maintain running count of freq in the sliding window
- if sliding window freq array == s1 freq array, return true
"""