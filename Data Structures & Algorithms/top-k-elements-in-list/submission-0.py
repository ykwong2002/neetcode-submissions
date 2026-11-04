class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        
        freq = list(d.items())
        sorted_freq = tuple(sorted(freq, key = lambda x: x[1], reverse = True))
        output = []
        for i in range(k):
            output.append(sorted_freq[i][0])

        return output