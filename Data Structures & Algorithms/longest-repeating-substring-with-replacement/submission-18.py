class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2:
            return len(s)

        l = 0
        counts = {}
        max_freq = 0
        longest = 0

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            max_freq = max(max_freq, counts[s[r]])
            
            # If the number of characters to replace (window_size - max_freq) > k
            if (r - l + 1) - max_freq > k:
                counts[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest