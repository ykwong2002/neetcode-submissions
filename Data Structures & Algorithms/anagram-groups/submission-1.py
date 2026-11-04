class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for string in strs:
            count = [0] * 26
            for letter in string:
                count[ord(letter) - ord('a')] += 1
            count = tuple(count)
            
            if count not in d:
                d[count] = [string]
            else:
                d[count].append(string)
        
        return [list(group) for group in d.values()]

        # iterate through the list
        # for each string, create a hashtable (anagrams will have same hashtable)
        # if hashtable has been created before, lump it in the same list as the one with same letters using index

