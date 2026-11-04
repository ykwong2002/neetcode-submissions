class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Goal: return k most frequent numbers in nums
        e.g if k = 2, return the most frequent AND second most frequent

        - hashmap
        Key : Val
        Integer : Count

        - sort the hashmap by count
        - return first k key val pairs
        """
        d = {}

        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        
        sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True) # Outputs a list of k, v pairs

        res = []

        for i in range(k):
            res.append(sorted_d[i][0])
        
        return res