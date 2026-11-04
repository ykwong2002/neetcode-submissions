class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        unique = set(s) # unique set of letters in s

        # create dictionary of count (letter : count)
        d = {}
        for char in unique:
            d[char] = 0 # initialise count

        l = 0 # left pointer
        result = 0

        for r in range(len(s)):
            d[s[r]] += 1
            window_length = r - l + 1
            if window_length - max(d.values()) > k: # not valid window (not enough k to change)
                d[s[l]] -= 1
                l += 1
            else:
                result = max(result, window_length)
        
        return result