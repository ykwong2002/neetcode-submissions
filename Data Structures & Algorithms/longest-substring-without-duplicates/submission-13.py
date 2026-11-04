class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        l, r = 0, 0
        longest = 1
        unique = set()
        while r < len(s):
            if s[r] not in unique:
                unique.add(s[r])
                r += 1
            else:
                while s[r] in unique:
                    unique.remove(s[l])
                    l += 1
        
            longest = max(longest, len(unique))
            print("Unique: ", unique)
        
        return longest

"""
Goal: return length of longest substring without duplicate chars
d   v   d   f
    l
                r
longest = 3
unique = , v, d, f
"""