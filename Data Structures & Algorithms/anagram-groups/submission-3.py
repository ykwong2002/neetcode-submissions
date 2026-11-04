class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = {} # stores (mapping : list of words)

        for word in strs:
            mapping = [0] * 26
            for char in word:
                mapping[ord(char) - ord('a')] += 1
            if tuple(mapping) in d:
                d[tuple(mapping)].append(word)
            else:
                d[tuple(mapping)] = [word]
        
        return list(d.values())


        # result list = []
        # create dictionary d (mapping : list of words)
        # loop through all strs:
        #     create a mapping of letters in str
        #     if mapping in d: add str to list of words
        #     else: create new mapping
        
        # return the values of d in one list