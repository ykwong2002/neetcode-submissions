class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            freq = [0] * 26

            # initialise frequency array of the current string
            for char in s:
                freq[ord(char) - ord('a')] += 1
            
            # check if the freq array exists as a key
            if tuple(freq) in d:
                d[tuple(freq)].append(s)
            else:
                d[tuple(freq)] = [s]
        
        return [value for value in d.values()]

"""
Goal: return a list of lists (groups of anagrams)
- hashmap:
    key: frequency tuple
    value: list of strings
- for each string, find the frequency list, convert to tuple, check if it exists in the hashmap
- if exists, add it to the list
- if does not exist, initialise it
- return all the values of the hashmap wrapped in a list
"""