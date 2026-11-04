class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        unique = set(s) # list of all unique characters

        # create hashmap (char : count)
        d = {}
        for c in unique:
            d[c] = 0
        
        l = 0 # left pointer
        result = 0

        for r in range(len(s)):
            window_length = r - l + 1
            d[s[r]] += 1
            if window_length - max(d.values()) > k: # if not valid, move left pointer
                d[s[l]] -= 1
                l += 1
            else:
                result = max(result, window_length)

        return result

            