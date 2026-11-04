class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0 # left pointer
        result = 0

        for r in range(len(s)): # continuously move right pointer
            while s[r] in charSet:
                charSet.remove(s[l]) # remove leftmost char to continue valid sliding window
                l += 1
            charSet.add(s[r])
            result = max(result, r - l + 1)
        
        return result
