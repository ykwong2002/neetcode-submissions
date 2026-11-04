class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        smallest_k = max(piles)

        while l <= r:
            k = (l + r) // 2
            total_time = 0

            for p in piles:
                total_time += math.ceil(p / k)
            
            if total_time <= h:
                smallest_k = k
                r = k - 1
            else:
                l = k + 1
        
        return smallest_k

            

"""
Goal: find minimum eating rate k to eat all bananas in h hours
- minimum speed is 1, maximum speed is max of the piles
- we need to search for ideal speed, not element
- initialise l = 1, r = max of piles
- while l <= r, find cumulative time taken to eat all bananas by pile
    - if meets requirement (< h), check left
    - else, check right
"""