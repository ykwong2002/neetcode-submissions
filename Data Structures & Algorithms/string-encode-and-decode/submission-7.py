class Solution:

    def encode(self, strs: List[str]) -> str:
        # (len of string)#(string)
        s = ""
        for word in strs:
            s += str(len(word)) + "#" + word
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0, 0
        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1
            length = int(s[l:r])  # Extract the length
            l = r + 1  # Move `l` to the start of the actual string
            res.append(s[l:l + length])  # Extract the word
            l += length  # Move `l` to the next encoded segment
    
        return res
        # result = []
        # left pointer = 0
        # right pointer = 0
        # while right pointer != len(s):
        #     while right pointer is not "#":
        #         right pointer += 1
        #     length = int(slice of left to right pointer)
        #     left pointer = right pointer + 1
        #     right pointer = left pointer
        #     for i in range(length):
        #         move right pointer
        #     slice out the word
        #     add word to result
