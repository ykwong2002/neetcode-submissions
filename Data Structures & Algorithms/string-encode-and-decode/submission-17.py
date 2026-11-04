class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))
            result += "#"
            result += s
            result += "#"
        return result

    def decode(self, s: str) -> List[str]:
        l, r  = 0, 0
        result = []
        while r < len(s): # ensures we know when to stop at the end of the string
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            l = r + 1
            r = l + length
            word = s[l:r]
            result.append(word)
            l = r + 1
            r = l
        
        return result

"""
Goal: find a way to encode and decode a string
encode: use a delimiter "#" to separate the length of a string and the actual string
0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15
5   #   H   e   l   l   o   #   5   #   W   o   r   l   d   #
        l
                            r

decode:
l and r pointer start at index 0
keep moving r pointer until reach #
convert l to right slice into an integer --> 5
move l pointer to r + 1
move r pointer to l + length
slice and decode the word
move l pointer to r pointer
"""