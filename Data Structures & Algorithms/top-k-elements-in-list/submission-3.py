class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create mapping for num to freq
        d = {}
        for num in nums:
            d[num] = 1 + d.get(num, 0)
        
        # create heap to maintain only top k elements
        heap = []
        for num in d.keys():
            heapq.heappush(heap, (d[num], num)) # (freq, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for pair in heap:
            result.append(pair[1])
        
        return result