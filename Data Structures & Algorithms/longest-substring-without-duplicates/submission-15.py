class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        longest = 0
        l = 0

        for r in range(len(s)):
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            unique.add(s[r])
            longest = max(longest, (r - l + 1))

        return longest
"""
Goal: return length of longest substring containing only unique chars
- sliding window
- maintain a set() to contain unique chars
- initialise longest substring to 0
- initiate sliding window, at each window:
    - check if the r exists in the set
    - if it doesnt, add to set
    - else if it does, while r exists in set: remove l from set and increment
    - update max substring

0   1   2   3   4   5   6
z   x   y   z   x   y   z
l
        r
max = 1
set: z  x
"""