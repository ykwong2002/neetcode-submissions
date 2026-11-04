class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if s and t are the same length
        if len(s) != len(t):
            return False
        
        # initialise hash table
        count = [0] * 26

        # else they must be of the same length
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for num in count:
            if num != 0:
                return False
        return True