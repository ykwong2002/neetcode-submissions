class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {} # freq array : list of unique words that have this freq array

        # iterate through the list of words
        for word in strs:
            freq = [0] * 26 # at most only 26 lowercase eng chars
            for char in word:
                freq[ord(char) - ord("a")] += 1
            
            k = tuple(freq) # dictionary key must be immutable
            if k not in d:
                d[k] = []
            d[k].append(word)
        
        return list(d.values())
            



"""
goal: group all the lowercase strings with the same chars and char counts into one group, output order does not matter
- duplicates should be preserved, empty strings count

brute force method:
- sort every single word
- for each word, go through the rest of the array and group the same ones together (anagrams will look EXACTLY THE SAME)
- TC: O(nlogn) --> sorting
- SC: O(1) --> in place sorting

optimal solution:
- use dictionary to store unique freq arrays k:v, unique freq array:list of the words that have this freq array
- for each word, create the freq array --> at most 26 lowercase english chars
- if this freq array is not in the dictionary, initialise it with a list that contains this word
- else if this freq array already exists, then append it to the value list

{[1  0   1   0 ...   0   1] : ["act"]
}
"""