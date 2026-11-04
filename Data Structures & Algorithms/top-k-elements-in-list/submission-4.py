class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        pairs = sorted(d.items(), key=lambda x: x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(pairs[i][0])
        
        return res
        # create dictionary d (num : freq)
        # loop through nums:
        #     if num in d: increment freq
        #     else: initialise
        
        # sort d.items() based on key = freq, reverse = True
        # res list []
        # get k highest nums based on freq