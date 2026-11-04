class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        # Create freq array of t
        freq_t = {}
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1

        # Sliding window for s
        freq_s = {}
        l = 0
        shortest = len(s) + 1
        shortest_substring = ""

        required = len(freq_t)
        formed = 0

        for r in range(len(s)):
            # expand window
            if s[r] in freq_t:
                freq_s[s[r]] = freq_s.get(s[r], 0) + 1
                if freq_s[s[r]] == freq_t[s[r]]:
                    formed += 1

            # shrink window when valid
            while formed == required:
                if (r - l + 1) < shortest:
                    shortest = r - l + 1
                    shortest_substring = s[l : r + 1]   # FIXED

                if s[l] in freq_t:
                    freq_s[s[l]] -= 1
                    if freq_s[s[l]] < freq_t[s[l]]:
                        formed -= 1   # NEW
                l += 1

        return shortest_substring
"""
Goal: find shortest substring of s such that all letters of t is inside
- if len(s) < len(t): return ""

- create freq array of t
- create freq array of s (empty)
- use fixed length sliding window on s
    - while freq of t is in sliding window, increase l pointer and update shortest
    - increment the r pointer until freq t in sliding window, then increase l pointer

freq_t = {
    X:1,
    Y:1,
    Z:1
}

freq_s = {
    X:1

}

0   1   2 
X   Y   Z   
l
    r
shortest = 4
shortest_substring = ""
"""