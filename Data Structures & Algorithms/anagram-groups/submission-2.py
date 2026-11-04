class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create mapping for hastable : list of words
        d = {}

        for word in strs:
            # create hashtable for each individual word (anagrams will have same hashtable)
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1 # increment count of that letter
            # convert key into tuple (immutable)
            count = tuple(count)
            # check if hashtable is already in d
            if count in d:
                d[count].append(word)
            else:
                d[count] = [word]
        
        return [anagramList for anagramList in d.values()]


        