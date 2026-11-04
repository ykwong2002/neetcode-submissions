class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0, 0
        while l < len(s):
            r = l
            # find length of word
            while s[r] != "#":
                r += 1
            length_of_word = int(s[l:r])
            # move left pointer to start of word, right pointer to end of word
            l = r + 1
            res.append(s[l:l + length_of_word])
            l += length_of_word
        return res
            
