class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        # initialise freq map
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        freq_arr = [[] for i in range(len(nums) + 1)] # index i contains all the numbers with freq i
        for val, count in d.items():
            freq_arr[count].append(val)
        
        res = []
        for i in range(len(freq_arr) - 1, 0, -1):
            for num in freq_arr[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        


"""
goal: return k most frequent elements inside array nums

brute force:
- create a freq map of all unique numbers in nums
- sort by the frequency (desc)
- take the first k keys
- TC: O(nlogn)
- SC: O(n)

optimal solution:
- create a freq map of all unique numbers in nums
- create list of lists, where each index i stores the numbers that appear i times
- start from the back of this list
- TC: O(n)
- SC: O(n)
"""