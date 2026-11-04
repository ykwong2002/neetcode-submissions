class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Goal: given a list of strs, group the anagrams in sublists
        - anagram: same letters diff order
            - need to compare anagrams
        - calculate the anagram array of each index
        - group the same ones together in a dictionary
        - return as a list
        """
        d = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in d.keys():
                d[tuple(count)] = [s]
            else:
                d[tuple(count)].append(s)
        
        return list(d.values())
