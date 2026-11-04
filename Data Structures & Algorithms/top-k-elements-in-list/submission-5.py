class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create frequency map
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        sorted_freq = sorted(freq_map.items(), key = lambda x: x[1], reverse = True)

        res = []

        for i in range(k):
            res.append(sorted_freq[i][0])
        
        return res