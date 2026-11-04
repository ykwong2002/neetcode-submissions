class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s))
            encoded += " " # delimiter to signal end of length
            encoded += s

        return encoded
        # 5 Hello5 World

    def decode(self, s: str) -> List[str]:
        l, r = 0, 0 # pointers
        res = []
        
        while l < len(s):
            r = l
            # while still checking for length
            while s[r] != " ":
                r += 1
            length = int(s[l : r])
            l = r + 1 # shift left pointer to start of string
            res.append(s[l : l + length]) # append the string to result list

            l += length
        
        return res
"""
Hello - 5
World - 5

5,Hello,5,World
decode:
- start with number
- if next char is number, continue until i hit delimiter ,
- from the next char after delimter, move pointer to {{number}} index away
- continue the loop
"""