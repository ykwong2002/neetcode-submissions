class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n < 2:
            return n
        
        count = {}
        longest = 0
        l, r = 0, 0

        for r in range(n):
            # Increase count of s[r]
            count[s[r]] = 1 + count.get(s[r], 0)
            # Check if window is valid
            while ((r - l + 1) - max(count.values()) > k):
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest


"""
Goal: find length of longest substring where i replace k characters to get all the same char
- sliding window (l, r starting at 0)
- keep hashmap of count of letters
- number of char to replace for each window = length of substring - max count of letters (since we only replace the less frequent chars)
- if number of char to replace > k, shift left pointer until valid again
X   Y   Y   X
l
            r
maxf = 2
res = 2
count = {
    x: ,
    y: 2
}

"""