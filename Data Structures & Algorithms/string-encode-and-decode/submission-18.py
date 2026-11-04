class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += "#"
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0

        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1 # keep moving right pointer until the separator
            curr_word_length = int(s[l:r])
            l = r + 1 # move l to the start of the word
            r = l + curr_word_length # move r to the char after end of the word
            res.append(s[l:r])
            l = r
        return res



"""
goal: find a way to encode and decode the strings
- any character can be a part of a string, so need some form of a separator --> #
encode:
- can attach the length of the string within the encoding itself
e.g. home --> 4#home
4   #   h   o   m   e
    ^
- move pointer until # --> gets me the length e.g. 4
- increment pointer by 1 --> gets me to the start of the word
- increment pointer by length --> gets me to end of the word
- increment pointer by 1 --> starts the next number
"""