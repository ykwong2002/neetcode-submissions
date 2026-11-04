class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Goal: return k most frequent numbers in nums
        e.g if k = 2, return the most frequent AND second most frequent

        - bucket sort
            - feature of each bucket is the number of times it has appeared
        
        - n is length of list
        - initialise 1d array of length n (at most a number can appear n times), each index has an empty list

        """
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res