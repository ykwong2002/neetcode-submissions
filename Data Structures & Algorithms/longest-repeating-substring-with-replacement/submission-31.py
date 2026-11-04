class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        count = {} # keep track of frequencies
        max_freq = 0 # highest frequency
        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])
            
            # num of chars to change = length of sliding window - max_freq
            change = (r - l + 1) - max_freq
            if change > k:
                count[s[l]] -= 1
                l += 1
            
            longest = max(longest, (r - l + 1))
        
        return longest

"""
Goal: return LENGTH of longets substring containing only 1 unique char, after at most k replacements
- use sliding window
- in sliding window, char to keep is the dominating char (highest freq)
- number of chars to change = (r - l + 1) - (freq of dominating char)
- if number of chars to change > k:
    - decrement left pointer count
    - move left pointer
"""