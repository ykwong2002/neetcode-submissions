class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        count = {} # keep track of frequencies
        max_freq = 0 # highest frequency
        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])

            # num of characters to change = sliding window length - max_freq
            change = (r - l + 1) - max_freq

            if change > k:
                count[s[l]] -= 1
                l += 1
            
            longest = max(longest, (r - l + 1))
            print(longest)
        
        return longest
"""
Goal: return length of longest substring consisting of only one char after replacing k chars
- sliding window
- the char to keep is the char with highest frequency in that window
- number of chars to change is (length of sliding window - max_freq)
- if number of chars to change > k: keep moving l pointer
- else, move right pointer

0   1   2   3   4   5   6
X   Y   Y   X
l
r
A: 4
B: 2
max = 5
"""