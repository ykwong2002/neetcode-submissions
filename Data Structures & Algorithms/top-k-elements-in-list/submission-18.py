class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        freq = [[] for i in range(len(nums) + 1)]
        print(d)
        for num, count in d.items():
            print("num", num)
            print("count", count)
            freq[count].append(num)
        
        result = []
        for i in range(len(freq) - 1, -1, -1):
            for number in freq[i]:
                result.append(number)
                if len(result) == k:
                    return result
"""
Goal: return a list containing k most frequent elements
- create a frequency hashmap for all the numbers
- use bucket sort:
    - create a list of lists of size len(nums), each list represents the number that appears that number of times
    - e.g if the number "3" appeared 5 times, it will be added to the list at index 5
"""