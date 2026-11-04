class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            freq_count = [0] * 26
            for c in s:
                freq_count[ord(c) - ord('a')] += 1
            
            if tuple(freq_count) in d.keys():
                d[tuple(freq_count)].append(s)
            else:
                d[tuple(freq_count)] = [s]
        
        return [l for l in d.values()]
"""
Goal: return list of lists. each inner list is a group of anagrams
- dictionary:
    - key: tuple(frequency)
    - value: list containing letters that fit the key

- for each str in strs:
    - get the freq_count, convert to tuple
    - check if tuple exists as a key in dictionary
    - if it does, append to end of list
    - else, initialise
"""