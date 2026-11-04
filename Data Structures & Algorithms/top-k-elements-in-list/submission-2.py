class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create mapping of num : freq
        count = {}

        # create frequency mapping, default 0
        for num in nums:
            count[num] = 1 + count.get(num, 0) 
        
        # create heap, push a tuple of (freq, num) in. freq in front so it pops by freq
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            # maintain only k tuples inside
            if len(heap) > k:
                heapq.heappop(heap)
        
        # output list
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

