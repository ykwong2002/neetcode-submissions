class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        # iterate through each word and encode using number of letters
        for word in strs:
            s += str(len(word)) + "#" + word
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        # go through all the encoded characters
        while i < len(s):
            j = i # back pointer = front pointer
            
            # get the length of the word
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            i = j + 1 # move front pointer to start of word (after #)
            j = i + length # move back pointer to end of word
            res.append(s[i:j])
            i = j # move front pointer to back pointer (in case reach end of string to break out of while loop)

        return res
        