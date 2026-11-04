class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if length of s and t are different, return false
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            # count the number of each letter from s in this alphabet table
            count[ord(s[i]) - ord('a')] += 1
            # remove the number of each letter from t in this alphabet table
            count[ord(t[i]) - ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False
        return True