class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # l is min k, r is max k
        res = r # max k

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas / k) # round up to eat all bananas in the pile
            
            if hours <= h: # if can finish in time, res shld be the smaller k
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res
            
            
        