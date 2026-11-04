class Solution:

    def encode(self, strs: List[str]) -> str:
        # length + # + string
        s = ""
        for word in strs:
            s += str(len(word)) + "#" + word
        return s

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0 # front pointer
        j = 0 # back pointer

        while i < len(s):
            j = i
            while s[j] != "#": # find the length before #
                j += 1
            length = int(s[i:j])
            i = j + 1 # move front pointer to start of word
            j = i + length # move back pointer to end of word

            result.append(s[i:j]) # add word to result list
            i = j + 1 # move front pointer to next number
            i = j
        
        return result
